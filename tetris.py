import copy
import logging
import curses

logging.basicConfig(filename='test.log', level=logging.DEBUG)


class Human(object):
    def __init__(self):
        self.name = 'Alex'


class AI(object):

    def __init__(self, weights=None):
        self.weights = weights or (-8, -18, -10.497, 16.432)

    def score_board(self, original_board, this_board):
        height_sum = get_height_sum(this_board)
        holes = get_holes(this_board)
        cumulative_holes = get_number_of_squares_above_holes(this_board)
        score_diff = this_board.score - original_board.score

        A, B, C, D = self.weights
        score = (
            (A * height_sum) +
            (B * holes) +
            (C * cumulative_holes) +
            (D * score_diff)
        )
        return score

    def get_moves(self, game_board, fun):
        max_score = -100000
        best_final_position = None
        falling_orientations = game_board.falling_shape.number_of_orientations
        next_orientations = game_board.next_shape.number_of_orientations
        for column_position in range(10):
            for orientation in range(falling_orientations):
                board = copy.deepcopy(game_board)
                falling_piece = board.falling_shape
                falling_piece.orientation = orientation
                falling_piece.move_to(column_position, 2)
                if board.shape_cannot_be_placed(falling_piece):
                    break
                fun.update_settled_pieces(board)  # clears out the old shadow locations
                fun.update_falling_piece(game_board)
                fun.update_shadow(board)
                fun.refresh_screen()
                if board.shape_cannot_be_placed(falling_piece):
                    break

                while not board.shape_cannot_be_placed(falling_piece):
                    falling_piece.lower_shape_by_one_row()
                falling_piece.raise_shape_by_one_row()
                board._settle_shape(falling_piece)
                for next_column_position in range(10):
                    for next_orientation in range(next_orientations):
                        falling_piece.color = 10
                        board2 = copy.deepcopy(board)
                        next_piece = board2.next_shape
                        board2.falling_shape = board2.next_shape
                        next_piece.orientation = next_orientation
                        next_piece.move_to(next_column_position, 2)
                        if board2.shape_cannot_be_placed(next_piece):
                            break
                        while not board2.shape_cannot_be_placed(next_piece):
                            next_piece.lower_shape_by_one_row()
                        next_piece.raise_shape_by_one_row()
                        board2._settle_shape(next_piece)

                        score = self.score_board(game_board, board2)
                        if score > max_score:
                            max_score = score
                            best_final_position = falling_piece

        return best_final_position


def get_holes(this_board):
    hole_count = 0
    for row in this_board.array:
        for cell in row:
            if cell and not _cell_below_is_occupied(cell, this_board.array):
                hole_count += 1
    return hole_count


def get_number_of_squares_above_holes(this_board):
    count = 0
    for column in range(this_board.num_columns):
        saw_hole = False
        for row in range(this_board.num_rows-1, 0, -1):
            cell = this_board.array[row][column]
            if cell:
                if saw_hole:
                    count += 1
            else:
                saw_hole = True
    return count


def _cell_below_is_occupied(cell, board):
    try:
        return board[cell.row_position + 1][cell.column_position]
    except IndexError:
        return True


def get_height_sum(this_board):
    return sum([20 - val.row_position for row in this_board.array for val in row if val])

from random import randint


class Block(object):
    """Represents one block in a tetris piece."""

    def __init__(self, row_position, column_position, color):
        self.row_position = row_position
        self.column_position = column_position
        self.color = color


class Shape(object):
    """The object representing a shape, including its position, orientation,
    color, and set of blocks it includes."""

    def __init__(self, column, row, color=None, orientation=None):
        self.column_position = column
        self.row_position = row
        self.color = color or self._get_random_color()
        if orientation is not None:
            self.orientation = orientation
        else:
            self.orientation = self._get_random_orientation()
        self.blocks = []
        self._initialize_blocks()

    def __eq__(self, other):
        return (self.row_position == other.row_position
                and self.column_position == other.column_position)

    def _get_random_orientation(self):
        return randint(0, self.number_of_orientations-1)

    @staticmethod
    def _get_random_color():
        return randint(1, 6)

    def _rotate(self, clockwise=True):
        rotate_amount = 1 if clockwise else -1
        self.orientation = (self.orientation + rotate_amount) % self.number_of_orientations
        self._rotate_blocks(self.orientation)

    @property
    def number_of_orientations(self):
        raise NotImplementedError

    @property
    def block_positions(self):
        """A dict of lists of the positions for each block in the Shape, for each orientation.
        Note: These are *relative* positions as compared to the base position of the current Shape.
        """
        raise NotImplementedError

    @property
    def bottom_blocks_for_orientations(self):
        """A dit of lists of the blocks on the bottom positions of the Shape, for each orientation."""
        bottom_blocks_for_orientation = {}
        for orientation in self.block_positions:
            bottom_blocks_for_orientation[orientation] = []
            for index, position in enumerate(self.block_positions[orientation]):
                if any([other_position[0] == position[0]
                        and other_position[1] > position[1]
                        for other_position in self.block_positions[orientation]]):
                    pass
                else:
                    bottom_blocks_for_orientation[orientation].append(self.blocks[index])
        return bottom_blocks_for_orientation

    @property
    def bottom_blocks(self):
        """The blocks currently on the bottom of the Shape."""
        return self.bottom_blocks_for_orientations[self.orientation]

    def _initialize_blocks(self):
        relative_block_positions = self.block_positions[self.orientation]
        self.blocks = [Block(self.row_position+diff[1],
                             self.column_position+diff[0],
                             self.color)
                       for diff in relative_block_positions]

    def _rotate_blocks(self, orientation):
        new_block_positions_diff = self.block_positions[orientation]
        for (index, diff) in enumerate(new_block_positions_diff):
            self.blocks[index].column_position = self.column_position + diff[0]
            self.blocks[index].row_position = self.row_position + diff[1]

    def lower_shape_by_one_row(self):
        """Moves shape down."""
        self._shift_by(columns=0, rows=1)

    def raise_shape_by_one_row(self):
        """Moves shape up."""
        self._shift_by(columns=0, rows=-1)

    def shift_shape_right_by_one_column(self):
        """Moves shape right."""
        self._shift_by(columns=1, rows=0)

    def shift_shape_left_by_one_column(self):
        """Moves shape left."""
        self._shift_by(columns=-1, rows=0)

    def _shift_by(self, columns, rows):
        self.column_position += columns
        self.row_position += rows
        for block in self.blocks:
            block.column_position += columns
            block.row_position += rows

    def move_to(self, column, row):
        """Move to given position and ensure orientation is correct."""
        self.column_position = column
        self.row_position = row
        self._rotate_blocks(self.orientation)

    def rotate_clockwise(self):
        """Rotate clockwise."""
        self._rotate(clockwise=True)

    def rotate_counterclockwise(self):
        """Rotate counterclockwise."""
        self._rotate(clockwise=False)

    @staticmethod
    def random(starting_column, starting_row):
        """Returns a randomly chosen piece at the given position."""
        rand = randint(0, 6)
        if rand == 0:
            new_piece = SquareShape(starting_column, starting_row)
        elif rand == 1:
            new_piece = LineShape(starting_column, starting_row)
        elif rand == 2:
            new_piece = SShape(starting_column, starting_row)
        elif rand == 3:
            new_piece = LShape(starting_column, starting_row)
        elif rand == 4:
            new_piece = TShape(starting_column, starting_row)
        elif rand == 5:
            new_piece = ZShape(starting_column, starting_row)
        elif rand == 6:
            new_piece = JShape(starting_column, starting_row)
        return new_piece


class SquareShape(Shape):
    """ Orientation:    0
        =====================
        Shape:      | 0*| 1 |
                    | 2 | 3 |
        * is the "base" location for the Shape. The block positions
          are offsets from this location.
    """
    @property
    def number_of_orientations(self):
        return 1

    @property
    def block_positions(self):
        return {
            0: [(0, 0), (1, 0), (0, 1), (1, 1)],
        }


class TShape(Shape):
    """ Orientation:    0           90              180               270
        ====================================================================
        Shape:      * | 0 |      * | 1 |          *                 * | 1 |
                  | 1 | 2 | 3 |    | 2 | 0 |    | 1 | 2 | 3 |     | 0 | 2 |
                                   | 3 |            | 0 |             | 3 |
    """
    @property
    def number_of_orientations(self):
        return 4

    @property
    def block_positions(self):
        return {
            0: [(1, 0), (0, 1), (1, 1), (2, 1)],
            1: [(2, 1), (1, 0), (1, 1), (1, 2)],
            2: [(1, 2), (0, 1), (1, 1), (2, 1)],
            3: [(0, 1), (1, 0), (1, 1), (1, 2)]
        }


class LineShape(Shape):
    """ Orientation:  0            90
        ======================================
        Shape:      | 0*|   | 0 | 1*| 2 | 3 |
                    | 1 |
                    | 2 |
                    | 3 |
    """
    @property
    def number_of_orientations(self):
        return 2

    @property
    def block_positions(self):
        return {
            0: [(0, 0), (0, 1), (0, 2), (0, 3)],
            1: [(-1, 0), (0, 0), (1, 0), (2, 0)],
        }


class SShape(Shape):
    """ Orientation:  0               90
        =====================================
        Shape:      | 0*|         * | 1 | 0 |
                    | 1 | 2 |   | 3 | 2 |
                        | 3 |
    """
    @property
    def number_of_orientations(self):
        return 2

    @property
    def block_positions(self):
        return {
            0: [(0, 0), (0, 1), (1, 1), (1, 2)],
            1: [(2, 0), (1, 0), (1, 1), (0, 1)],
        }


class ZShape(Shape):
    """ Orientation:  0               90
        =====================================
        Shape:        * | 0 |   | 0 | 1*|
                    | 2 | 1 |       | 2 | 3 |
                    | 3 |
    """
    @property
    def number_of_orientations(self):
        return 2

    @property
    def block_positions(self):
        return {
            0: [(1, 0), (1, 1), (0, 1), (0, 2)],
            1: [(-1, 0), (0, 0), (0, 1), (1, 1)],
        }


class LShape(Shape):
    """ Orientation:  0              90            180           270
        ====================================================================
        Shape:      | 0*|             *         | 3 | 2*|         * | 3 |
                    | 1 |       | 2 | 1 | 0 |       | 1 |   | 0 | 1 | 2 |
                    | 2 | 3 |   | 3 |               | 0 |
    """
    @property
    def number_of_orientations(self):
        return 4

    @property
    def block_positions(self):
        return {
            0: [(0, 0), (0, 1), (0, 2), (1, 2)],
            1: [(1, 1), (0, 1), (-1, 1), (-1, 2)],
            2: [(0, 2), (0, 1), (0, 0), (-1, 0)],
            3: [(-1, 1), (0, 1), (1, 1), (1, 0)]
        }


class JShape(Shape):
    """ Orientation:    0           90           180           270
        ====================================================================
        Shape:      * | 0 |   | 3*|           | 2*| 3 |   | 0*| 1 | 2 |
                      | 1 |   | 2 | 1 | 0 |   | 1 |               | 3 |
                  | 3 | 2 |                   | 0 |
    """
    @property
    def number_of_orientations(self):
        return 4

    @property
    def block_positions(self):
        return {
            0: [(1, 0), (1, 1), (1, 2), (0, 2)],
            1: [(2, 1), (1, 1), (0, 1), (0, 0)],
            2: [(0, 2), (0, 1), (0, 0), (1, 0)],
            3: [(0, 0), (1, 0), (2, 0), (2, 1)]
        }

import copy
import math

from tetris import Shape


NUM_COLUMNS = 10
NUM_ROWS = 20

STARTING_COLUMN = 4
STARTING_ROW = 0

PREVIEW_COLUMN = 12
PREVIEW_ROW = 1

BLOCK_WIDTH = 2
BORDER_WIDTH = 1

POINTS_PER_LINE = 20
POINTS_PER_LEVEL = 200


class Board(object):
    """Maintains the entire state of the game."""
    def __init__(self, columns=None, rows=None, level=None):
        self.num_rows = rows or NUM_ROWS
        self.num_columns = columns or NUM_COLUMNS
        self.array = [[None for _ in range(self.num_columns)] for _ in range(self.num_rows)]
        self.falling_shape = None
        self.next_shape = None
        self.score = 0
        self.level = level or 1

    def start_game(self):
        self.score = 0
        self.level = 1
        if self.next_shape is None:
            self.next_shape = Shape.random(PREVIEW_COLUMN, PREVIEW_ROW)
            self.new_shape()

    def end_game(self):
        raise GameOverError(score=self.score, level=self.level)

    def new_shape(self):
        self.falling_shape = self.next_shape
        self.falling_shape.move_to(STARTING_COLUMN, STARTING_ROW)
        self.next_shape = Shape.random(PREVIEW_COLUMN, PREVIEW_ROW)
        if self.shape_cannot_be_placed(self.falling_shape):
            self.next_shape = self.falling_shape
            self.falling_shape = None
            self.next_shape.move_to(PREVIEW_COLUMN, PREVIEW_ROW)
            self.end_game()

    def remove_completed_lines(self):
        rows_removed = []
        lowest_row_removed = 0
        for row in self.array:
            if all(row):
                lowest_row_removed = max(lowest_row_removed, row[0].row_position)
                rows_removed.append(copy.deepcopy(row))
                for block in row:
                    self.array[block.row_position][block.column_position] = None
        if len(rows_removed) > 0:
            points_earned = math.pow(2, len(rows_removed)-1) * POINTS_PER_LINE
            self.score += points_earned
            if self.score > POINTS_PER_LEVEL * self.level:
                self.level += 1

            for column_index in range(0, NUM_COLUMNS):
                for row_index in range(lowest_row_removed, 0, -1):
                    block = self.array[row_index][column_index]
                    if block:
                        # number of rows removed that were below this one
                        distance_to_drop = len(
                            [row for row in rows_removed if
                             row[0].row_position > block.row_position]
                        )
                        new_row_index = row_index + distance_to_drop
                        self.array[row_index][column_index] = None
                        self.array[new_row_index][column_index] = block
                        block.row_position = new_row_index

    def settle_falilng_shape(self):
        """Resolves the current falling shape."""
        if self.falling_shape:
            self._settle_shape(self.falling_shape)
            self.falling_shape = None
            self.new_shape()

    def _settle_shape(self, shape):
        """Adds shape to settled pieces array."""
        if shape:
            for block in shape.blocks:
                self.array[block.row_position][block.column_position] = block
        self.remove_completed_lines()

    def move_shape_left(self):
        """When the user hits the left arrow."""
        if self.falling_shape:
            self.falling_shape.shift_shape_left_by_one_column()
            if self.shape_cannot_be_placed(self.falling_shape):
                self.falling_shape.shift_shape_right_by_one_column()
                return False
            return True

    def move_shape_right(self):
        """When the user hits the right arrow."""
        if self.falling_shape:
            self.falling_shape.shift_shape_right_by_one_column()
            if self.shape_cannot_be_placed(self.falling_shape):
                self.falling_shape.shift_shape_left_by_one_column()
                return False
            return True

    def rotate_shape(self):
        """When the user hits the up arrow."""
        if self.falling_shape:
            self.falling_shape.rotate_clockwise()
            if self.shape_cannot_be_placed(self.falling_shape):
                self.falling_shape.rotate_counterclockwise()
                return False
            return True

    def let_shape_fall(self):
        """What happens during every `tick`. Also what happens when the user hits down arrow."""
        if self.falling_shape:
            self.falling_shape.lower_shape_by_one_row()
            if self.shape_cannot_be_placed(self.falling_shape):
                self.falling_shape.raise_shape_by_one_row()
                if self.shape_cannot_be_placed(self.falling_shape):
                    self.end_game()
                else:
                    self.settle_falilng_shape()
            return True

    def drop_shape(self):
        """When you hit the enter arrow and the piece goes all the way down."""
        if self.falling_shape:
            while not self.shape_cannot_be_placed(self.falling_shape):
                self.falling_shape.lower_shape_by_one_row()
            self.falling_shape.raise_shape_by_one_row()
            if self.shape_cannot_be_placed(self.falling_shape):
                self.end_game()
            else:
                self.settle_falilng_shape()
            return True

    def shape_cannot_be_placed(self, shape):
        for block in shape.blocks:
            if (block.column_position < 0 or
                    block.column_position >= NUM_COLUMNS or
                    block.row_position < 0 or
                    block.row_position >= NUM_ROWS or
                    self.array[block.row_position][block.column_position] is not None):
                return True
        return False


class BoardDrawer(object):
    def __init__(self):
        stdscr = curses.initscr()
        stdscr.nodelay(1)
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_RED)
        curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLUE)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_GREEN)
        curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_MAGENTA)
        curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_CYAN)
        curses.init_pair(6, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
        curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(10, 10, 10)
        curses.cbreak()
        stdscr.keypad(1)
        curses.nonl()
        curses.curs_set(0)
        curses.noecho()
        self.stdscr = stdscr

    def update_falling_piece(self, board):
        """Adds the currently falling pieces to the next stdscr to be drawn."""
        # actual game board: falling piece
        if board.falling_shape:
            for block in board.falling_shape.blocks:
                self.stdscr.addstr(
                    block.row_position+BORDER_WIDTH,
                    BLOCK_WIDTH*block.column_position+BORDER_WIDTH,
                    ' '*BLOCK_WIDTH,
                    curses.color_pair(block.color)
                )

    def update_settled_pieces(self, board):
        """Adds the already settled pieces to the next stdscr to be drawn."""
        # actual game board: settled pieces
        for (r_index, row) in enumerate(board.array):
            for (c_index, value) in enumerate(row):
                block = value
                if block:
                    color_pair = block.color
                else:
                    color_pair = 0
                self.stdscr.addstr(
                    r_index+BORDER_WIDTH,
                    c_index*BLOCK_WIDTH+BORDER_WIDTH,
                    ' '*BLOCK_WIDTH,
                    curses.color_pair(color_pair)
                )

    def update_shadow(self, board):
        """Adds the 'shadow' of the falling piece to the next stdscr to be drawn."""
        # where this piece will land
        shadow = copy.deepcopy(board.falling_shape)
        if shadow:
            while not board.shape_cannot_be_placed(shadow):
                shadow.lower_shape_by_one_row()
            shadow.raise_shape_by_one_row()
            for block in shadow.blocks:
                self.stdscr.addstr(
                    block.row_position+BORDER_WIDTH,
                    BLOCK_WIDTH*block.column_position+BORDER_WIDTH,
                    ' '*BLOCK_WIDTH,
                    curses.color_pair(8))

    def update_next_piece(self, board):
        """Adds the next piece to the next stdscr to be drawn."""
        # next piece
        if board.next_shape:
            for preview_row_offset in range(4):
                self.stdscr.addstr(
                    PREVIEW_ROW+preview_row_offset+BORDER_WIDTH,
                    (PREVIEW_COLUMN-1)*BLOCK_WIDTH+BORDER_WIDTH*2,
                    '    '*BLOCK_WIDTH,
                    curses.color_pair(0)
                )
            for block in board.next_shape.blocks:
                self.stdscr.addstr(
                    block.row_position+BORDER_WIDTH,
                    block.column_position*BLOCK_WIDTH+BORDER_WIDTH*2,
                    ' '*BLOCK_WIDTH,
                    curses.color_pair(block.color)
                )

    def update_score_and_level(self, board):
        """Adds the score and level to the next stdscr to be drawn."""
        # level
        self.stdscr.addstr(
            5+BORDER_WIDTH,
            PREVIEW_COLUMN*BLOCK_WIDTH-2+BORDER_WIDTH,
            'LEVEL: %d' % board.level,
            curses.color_pair(7)
        )
        # score
        self.stdscr.addstr(
            6+BORDER_WIDTH,
            PREVIEW_COLUMN*BLOCK_WIDTH-2+BORDER_WIDTH,
            'SCORE: %d' % board.score,
            curses.color_pair(7)
        )

    def clear_score(self):
        # level
        self.stdscr.addstr(
            5+BORDER_WIDTH,
            PREVIEW_COLUMN*BLOCK_WIDTH-2+BORDER_WIDTH,
            'LEVEL:              ',
            curses.color_pair(7)
        )
        # score
        self.stdscr.addstr(
            6+BORDER_WIDTH,
            PREVIEW_COLUMN*BLOCK_WIDTH-2+BORDER_WIDTH,
            'SCORE:              ',
            curses.color_pair(7)
        )

    def update_border(self):
        """Adds the border to the next stdscr to be drawn."""
        # side borders
        for row_position in range(NUM_ROWS+BORDER_WIDTH*2):
            self.stdscr.addstr(row_position, 0, '|', curses.color_pair(7))
            self.stdscr.addstr(row_position, NUM_COLUMNS*BLOCK_WIDTH+1, '|', curses.color_pair(7))
        # top and bottom borders
        for column_position in range(NUM_COLUMNS*BLOCK_WIDTH+BORDER_WIDTH*2):
            self.stdscr.addstr(0, column_position, '-', curses.color_pair(7))
            self.stdscr.addstr(NUM_ROWS+1, column_position, '-', curses.color_pair(7))

    def update(self, board):
        """Updates all visual board elements and then refreshes the screen."""
        self.update_border()
        self.update_score_and_level(board)
        self.update_next_piece(board)

        self.update_settled_pieces(board)

        self.update_falling_piece(board)
        self.update_shadow(board)

        self.refresh_screen()

    def refresh_screen(self):
        """Re-draws the current screen."""
        stdscr = self.stdscr
        stdscr.refresh()

    @staticmethod
    def return_screen_to_normal():
        """Undoes the weird settings to the terminal isn't screwed up when the game is over"""
        curses.endwin()


class GameOverError(Exception):
    def __init__(self, score, level):
        super(GameOverError).__init__(GameOverError)
        self.score = score
        self.level = level

import datetime
import math
import signal
import sys

LEVEL_ONE_TICK_LENGTHMS = 600


def main():
    start_new_game()


def start_new_game():
    game = Game()
    game.new_game()
    game.run_game()


class Game(object):
    """Manages the game and updating the screen."""

    def __init__(self, player=None):
        self.last_tick = None
        self.board = None
        self.board_drawer = None
        self.player = player or Human()

    def new_game(self):
        """Initializes a new game."""
        self.last_tick = None
        self.board = Board()
        self.board_drawer = BoardDrawer()
        self.board_drawer.clear_score()
        self.board.start_game()

    def pause_game(self):
        """Pauses or unpauses the game."""
        if self.last_tick:
            self.stop_ticking()
        else:
            self.start_ticking()

    def run_game(self):
        self.start_ticking()
        self._tick()
        while True:
            try:
                if isinstance(self.player, Human):
                    self.process_user_input()
                elif isinstance(self.player, AI):
                    self.process_ai_input()
                self.update()
            except GameOverError:
                self.end_game()
                return self.board.score

    def save_game(self):
        """Writes the state of the game to a file."""
        pass

    def load_game(self):
        """Loads a game from a file."""
        pass

    def end_game(self):
        """Ends the current game."""
        pass

    def exit(self):
        """Exits the program."""
        self.end_game()
        self.board_drawer.return_screen_to_normal()
        print('Game Over! Final Score: {}'.format(int(self.board.score)))
        sys.exit(0)

    def start_ticking(self):
        self.last_tick = datetime.datetime.now()

    def stop_ticking(self):
        self.last_tick = None

    def update(self):
        current_time = datetime.datetime.now()
        tick_multiplier = math.pow(0.9, self.board.level-1)
        tick_threshold = datetime.timedelta(milliseconds=LEVEL_ONE_TICK_LENGTHMS*tick_multiplier)
        if self.last_tick and current_time - self.last_tick > tick_threshold:
            self.last_tick = current_time
            self._tick()

    def _tick(self):
        self.board.let_shape_fall()
        self.board_drawer.update(self.board)

    def process_ai_input(self):
        move = self.player.get_moves(self.board, self.board_drawer)
        if move:
            self.board.falling_shape.orientation = move.orientation
            self.board.falling_shape.move_to(move.column_position, move.row_position)
            self.board_drawer.update(self.board)
        else:
            self.end_game()

    def process_user_input(self):
        user_input = self.board_drawer.stdscr.getch()
        moves = {
            curses.KEY_RIGHT: self.board.move_shape_right,
            curses.KEY_LEFT: self.board.move_shape_left,
            curses.KEY_UP: self.board.rotate_shape,
            curses.KEY_DOWN: self.board.let_shape_fall,
            curses.KEY_ENTER: self.board.drop_shape,
            10: self.board.drop_shape,
            13: self.board.drop_shape,
            112: self.pause_game,
            113: self.exit,
        }
        move_fn = moves.get(user_input)
        if move_fn:
            piece_moved = move_fn()
            if piece_moved:
                self.board_drawer.update(self.board)


def signal_handler(signal, frame):
    BoardDrawer.return_screen_to_normal()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':
    main()
