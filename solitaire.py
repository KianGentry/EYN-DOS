"Credit to 'shomikj' on GitHub for this code!"

class Card:
    def __init__(self, param_rank):
        self.rank = param_rank
        self.str_rank = ['A  ', '2  ', '3  ', '4  ', '5  ', '6  ', '7  ', '8  ', '9  ', '10 ', 'J  ', 'Q  ', 'K  ']
        self.visible = False

    def __str__(self):
        if self.visible:
            return self.str_rank[self.rank-1]
        else:
            return '-  '

    def hide(self):
        self.visible = False

    def show(self):
        self.visible = True
class Card_Stack:
    def __init__(self):
        self.cards = []

    def __len__(self):
        return len(self.cards)

    def top(self):
        if not self.empty():
            return self.cards[-1]
        else:
            return None

    def empty(self):
        return len(self) == 0
class Tableau(Card_Stack):
    def __init__(self):
        Card_Stack.__init__(self)

    def valid(self, new):
        threshold = 14
        if self.top():
            threshold = self.top().rank

        for c in new:
            if (c.visible) and (c.rank == threshold-1):
                threshold = c.rank
            else:
                return False
        return True

    def add(self, new):
        for c in new:
            self.cards.append(c)

    def view_cards(self, i):
        if (i >= 0) and (i < len(self)):
            return self.cards[i:]
        else:
            return []

    def remove_cards(self, i):
        if (i >= 0) and (i < len(self)):
            for c in range(i, len(self)):
                if not self.cards[c].visible:
                    return []

            answer = self.cards[i:]
            self.cards = self.cards[:i]

            if not self.empty():
                self.top().show()

            return answer
        else:
            return []

    def next_spot(self, i):
        return (i == len(self))

    def last_spot(self, i):
        return (i == len(self)-1)

    def get_str(self, i):
        if i < len(self.cards):
            return str(self.cards[i])
        else:
            return '   '
class Foundation(Card_Stack):
    def __init__(self):
        Card_Stack.__init__(self)

    def valid(self, c):
        threshold = 0
        if self.top():
            threshold = self.top().rank

        return (c.rank == threshold+1)

    def add(self, c):
        if not self.empty():
            self.cards[-1].hide()
        self.cards.append(c)

    def __str__(self):
        if self.empty():
            return '-  '
        else:
            return str(self.top())

    def full(self):
        if not (len(self) == 13):
            return False

        for i in range(1,14):
            if not (self.cards[i].rank == i):
                return False

        return True
from random import randint
class Deck(Card_Stack):
    def __init__(self):
        Card_Stack.__init__(self)

        for i in range(0, 4):
            for r in range(1, 14):
                c = Card(r)
                self.cards.append(c)

        self.shuffle()

        self.pointer = 0

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            j = randint(0, i)

            self.cards[i],self.cards[j] = self.cards[j],self.cards[i]

    def top(self):
        return self.cards[self.pointer]

    def increment(self):

        self.cards[self.pointer].hide()

        self.pointer += 1
        if (self.pointer >= len(self)):
            self.pointer = 0


        self.cards[self.pointer].show()


    def pop(self):
        answer = self.cards[self.pointer]

        del self.cards[self.pointer]
        self.cards[self.pointer].show()

        return answer
class Game:
    def __init__(self):
        self.tableaus = []
        self.foundations = []
        self.deck = Deck()

        for i in range(0, 7):
            self.tableaus.append(Tableau())

        for i in range(7, 0, -1):
            for j in range(0, i):
                self.tableaus[j].add([self.deck.pop()])
                self.tableaus[j].top().hide()

        self.deck.top().show()

        for t in self.tableaus:
            t.top().show()

        for i in range(0, 4):
            self.foundations.append(Foundation())

    def game_over(self):
        for f in self.foundations:
            if not f.full():
                return False
        return True

    def valid_row(self, str):
        if (len(str) == 2) or (len(str) == 3):
            if (str[0] == 'R'):
                return True

        return False

    def valid_col(self, str):
        return str in ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'F1', 'F2', 'F3', 'F4', 'D0']

    def valid_tableau(self, i):
        return (i >= 0) and (i < len(self.tableaus))

    def valid_foundation(self, i):
        return (i >= 0) and (i < len(self.foundations))

    def move(self, command):
        sequence = command.split()

        if (len(sequence) != 4):
            print("Invalid Command: format error")
            return False

        from_row = sequence[0]
        from_col = sequence[1]
        to_row = sequence[2]
        to_col = sequence[3]

        if not (self.valid_col(from_col) and self.valid_col(to_col) and self.valid_row(from_row) and self.valid_row(to_row)):
            print("Invalid Command: format error")
            return True

        if (from_row == 'R0') and (from_col == 'D0') and (to_row == 'R0') and (to_col == 'D0'):
            self.deck.increment()
            return True

        if (from_row == 'R0') and (from_col == 'D0') and ('T' == to_col[0]):
            to_row = int(to_row[1:]) - 1
            to_col = int(to_col[1:]) - 1

            if not self.valid_tableau(to_col):
                print("Invalid Command: tableau column error")
                return False

            if not self.tableaus[to_col].next_spot(to_row):
                print("Invalid Command: tableau row error")
                return False

            move_card = [self.deck.top()]
            if self.tableaus[to_col].valid(move_card):
                self.tableaus[to_col].add([self.deck.pop()])
                return True
            else:
                print("Invalid Command: can't move selected cards")
                return False

        if ('T' == from_col[0]) and ('T' == to_col[0]):
            from_col = int(from_col[1:]) - 1
            to_col = int(to_col[1:]) - 1
            from_row = int(from_row[1:]) - 1
            to_row = int(to_row[1:]) - 1

            if not self.valid_tableau(from_col) or not self.valid_tableau(to_col):
                print("Invalid Command: tableau column error")
                return False

            if not self.tableaus[to_col].next_spot(to_row):
                print("Invalid Command: destination tableau row error")
                return False

            if (self.tableaus[from_col].empty()) or (from_row < 0) or (from_row >= len(self.tableaus[from_col])):
                print("Invalid Command: source tableau row error")
                return False

            move_cards = self.tableaus[from_col].view_cards(from_row)
            if self.tableaus[to_col].valid(move_cards):
                self.tableaus[to_col].add(self.tableaus[from_col].remove_cards(from_row))
                return True
            else:
                print("Invalid Command: can't move selected cards")
                return False

        if (from_row == 'R0') and (from_col == 'D0') and (to_row == 'R0') and ('F' == to_col[0]):
            to_col = int(to_col[1:]) - 1

            if not self.valid_foundation(to_col):
                print("Invalid Command: foundation column error")
                return False

            move_card = self.deck.top()
            if (self.foundations[to_col].valid(move_card)):
                self.foundations[to_col].add(self.deck.pop())
                return True
            else:
                print("Invalid Command: can't move selected cards")
                return False

        if (from_col[0] == 'T') and (to_row == 'R0') and ('F' == to_col[0]):
            from_col = int(from_col[1:]) - 1
            to_col = int(to_col[1:]) - 1
            from_row = int(from_row[1:]) - 1

            if not self.valid_tableau(from_col):
                print("Invalid Command: source tableau column error")
                return False

            if not self.tableaus[from_col].last_spot(from_row):
                print("Invalid Command: source tableau row error")
                return False

            if not self.valid_foundation(to_col):
                print("Invalid Command: destination foundation column error")
                return False

            move_card = self.tableaus[from_col].top()
            if (self.foundations[to_col].valid(move_card)):
                move_card = self.tableaus[from_col].remove_cards(from_row)
                move_card = move_card[0]
                self.foundations[to_col].add(move_card)
                return True
            else:
                print("Invalid Command: can't move selected cards")
                return False

    def __str__(self):
        spot = '   '

        header = spot + 'D0 ' + spot + spot + 'F1 ' + 'F2 ' + 'F3 ' + 'F4 ' + '\n'

        header_cards = 'R0 ' + str(self.deck.top()) + spot + spot
        for f in self.foundations:
            header_cards += str(f)
        header_cards += '\n' + '\n'

        tableau_header = spot
        for i in range(0, 7):
            tableau_header += 'T' + str(i+1) + ' '
        tableau_header += '\n'

        tableau_str = ''
        max_len = max([len(i) for i in self.tableaus])
        for r in range(0, max_len+1):
            tableau_str += 'R' + str(r+1)
            if r < 9:
                tableau_str += ' '
            for t in self.tableaus:
                tableau_str += t.get_str(r)
            tableau_str += '\n'

        return header + header_cards + tableau_header + tableau_str
def main():
    game = Game()
    print()
    print("Welcome to Solitaire: Good Luck!")
    print()
    print("Game Instructions")
    print("Move Command Format: [Source Row] [Source Column] [Destination Row] [Destination Column]")
    print()
    print("Move Types and Examples")
    print("(1) New Deck Card: R0 D0 R0 D0")
    print("(2) Deck to Tableau: R0 D0 R8 T1")
    print("(3) Tableau to Tableau: R7 T1 R7 T2 (supports multiple cards)")
    print("(4) Deck to Foundation: R0 D0 R0 F1")
    print("(5) Tableau to Foundation: R7 T1 R0 F1 (supports 1 card only)")
    print("(6) Quit: quit")
    print()
    print(game)

    while not game.game_over():
        print()
        command = input("What is your move?: ")

        if (command == 'quit'):
            print()
            print("See you next time!")
            print()
            break

        result = False
        try:
            result = game.move(command)
        except:
            print()
            print("Invalid Command")
            print()

        if result:
            print(game)

if __name__ == "__main__":
    main()

"Credit to 'shomikj' on GitHub for this code!"
