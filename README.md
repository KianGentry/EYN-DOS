# Welcome to the EYN-DOS Instruction Manual! 

---

# ALERT - J.K Incorporated is asking for volunteers to help work on EYN-DOS & EYN-OS. Amateur knowledge of Python and TKinter is required. If you are interested, contact us at eyndos@gmail.com. #

---

This manual will go through crucial information regarding the use of EYN-DOS and everything included with the version of EYN-DOS we will be discussing today (1.9).

---

Commands:
---

"help" = Prints all commands available in EYN-DOS.

"listdir" = Lists all sub-directories.

"dir" = Lists all files in the current working directory (Including total size).

"run" = Gives you a prompt asking what file you want to run. Type "nul" to abort the command. Type the name of the file you want to run (Including the extension e.g: example.txt).

"end" = Gives you a prompt asking if you are sure you want to end your EYN-DOS session. Type "y" to end your session. Type "n" to abort the command.

"ver" = Prints the version number of EYN-DOS currently running.

"credits" = Lists the names and contributions of all the people that influenced development of EYN-DOS.

"cd" = Gives you a prompt asking what sub-directory you want to move to. Type "nul" to abort the command. Type the name of the directory you want to move to and you will be moved there.

"cdate" = Prints the current date. (D/M/Y)

"ctime" = Prints the current time. (H/M)

"read" = Gives you a prompt asking what file you want to read. Type "nul" to abort the command. Type the name of the file you want to read (Including the extension e.g: example.txt) to print the contents of the entered file.

"find" = Gives you a prompt asking what file you want to find. Type "nul" to abort the command. Type the name of the file you want to find (Including the extension e.g: example.txt) to print the path of the file you want to find. (Has to be in the current working directory or sub-directory)

"write" = Gives you a prompt of what you want to call your file (Including the extension e.g: example.txt). After typing the name of your file, you will be asked to type the contents of your file. Type "nul0" to exit the command and save the file.

"del" = Gives you a prompt asking what file you want to delete. Type "nul" to abort the command. Type the name of the file you want to delete (Including the extension e.g: example.txt) to delete it.

"size" = Gives you a prompt asking what file you want to know the size to. Type the name of the file you want to know the size to (Including the extension e.g: example.txt) to get the file size in kilobytes.

"clear" = Clears the screen of all text present in the terminal.

"count" = Gives you a prompt asking if you are sure if you want to proceed with counting. Type "n" to abort the command. Type "y" to proceed with the counting. This will infinitely count in the terminal until the terminal is forcefully shut down.

"cwd" = Prints the current working directory.

"md" = Gives you a prompt asking what you want to call your new sub-directory. After entering the name, the new directory will be created.

"copy" = Gives you a prompt asking what file you want to copy (Absolute file path). Next, you get another prompt asking where you want to paste your selected file (Directory path).

"echo" = Gives you a prompt asking what text you want printed into the terminal. After typing your message, it will be printed into the terminal.

"colortest" = Prints all colors available in EYN-DOS. If there is no color, (Monochrome) don't worry, it is most likely your terminal settings or lack of the "colorama" module being installed.

"terry" = Prints a tribute to a man that some love and some hate. Rest in peace.

"edit" = Gives you a prompt asking what file you want to edit. Type the file you want to edit (Including extension e.g: example.txt) to append the file (add text onto/edit).

"specs" = Prints all accquirable system specifications and information (e.g: system name, operating system, etc).

"dirsize" = Gives you a prompt asking what folder (directory) you want to know the size to. Type the name of the folder you want to know the size to to get the directory size in kilobytes.

"newver" = Downloads the newest version of EYN-DOS through GitHub (REQUIRES INTERNET CONNECTION).

"unzip" = Gives you a prompt asking what file you want to unzip. Type the (absolute) path to the zip file and strike enter. Then, another prompt will appear asking where you want to extract all the files/folders. Type the path to where you want to extract the contents of the zip file.

"zip" = Gives you a prompt asking what you want to call your zip file. Type the name you desire (Including the .zip extension). Then, you are given another prompt asking you to type all files you want contained inside your zip file. Type the names and extensions of the files you want to put inside your zip file.


"pyedit" = Simply opens the built-in Python editor.

"restart" = Gives you a prompt asking if you want to restart EYN-DOS. If you enter 'y', EYN-DOS will close and re-open into a fresh state. If you enter 'n', the command will be aborted and you'll go back to the EYN-DOS terminal.

"prevd" = Prints a list of all sub-directories in the previous directory.

"prevf" = Prints a list of all files in the previous directory.

"noneyn" = Gives you a prompt asking what non-EYN commmand you want to execute. Type any command from your host-system's terminal to execute it in EYN-DOS.

---

We may have some commands that aren't listed in this list. Find them yourself!

---

# Getting Started With EYN-DOS: 

---

EYN-DOS requires Python 3.x to function. Required modules will be listed below. EYN-DOS natively supports Windows Host Operating Systems and Linux Host Operating Systems.

---

Requried Modules:
---

- Colorama - Adds color support to EYN-DOS.

- Shutil - Used for copying and pasting files.

- OS - Included with Python. No external installation required.

- Platform - Included with Python. No external installation required.

- ZipFile - Included with Python. No external installation required.

Optional Modules:
---

- Requests - Used in the "newver" command to install the newest version of EYN-DOS.

- Tkinter - Used for graphical games and tests.

- Turtle - Used for graphical games.

---

EYN-DOS is designed to appeal to people who want a lightweight tool for interacting with their PC. EYN-DOS is also designed to appeal to nostalgia nerds (Such as Kian Gentry) who feel nostalgic about computers that ran Disk Operating Systems with a text-based GUI. 

Notes:
---

- You don't have to be from the era where you most feel nostalgia from. Many people born from the year 2000 and onwards feel nostalgic about computers that are double their age! This note was inspired by a letter from a viewer of a YouTube channel called LGR. He was a 13 year old viewer that wrote his physical letter on a computer twice his age. We saw this letter and thought, "New generations aren't going to lose nostalgia over older technology." This inspired J.K Incorporated to create a Disk Operating System that is regularly updated for newer generations.

# Let's Get Started: 

To run EYN-DOS, simply run the file named, "main.py".
Your main way of interacting with EYN-DOS is a small bit of input text that looks like this, "/main/}". This is the command-line.

The command-line is the main way of interacting with your PC through a terminal. You type words into the command-line to perform certain functions called commands. These commands can do various things such as read files, write files, and can do pretty much anything that can ever be coded into a function. Commands are what allow you to change things about your PC.

Games and tech demos:
---

- Invaders - Use the arrow keys to move left and right and spacebar to shoot. "Alien spacecrafts are invading! Quick, send forces to fight them off immediately!"

- Paintbrush - A test of a simple drawing system with a pointing device.

- Pong - A recreation of the classic Atari game that took the world by storm. Use the arrow keys to move your paddle up and down to try and hit the ball.

- Raycast Test - A test of a raycasting engine. Pretty self-explanatory. (Engine may be used for future projects. Don't tell anyone I said this!)

- Snake - Basic, classic Snake. Use the arrow keys to move and eat the apples.

- Solitiare - A command-line operated solitaire game. This version of solitaire uses a co-ordinate system in order to move the cards. For example, if a card was on slot A1 B1 and you wanted to move it to A1 B2, you would type "A1 B1 A1 B2".

# It's really that easy to use EYN-DOS!

If you have any issues or complaints about EYN-DOS or anything affiliated with said operating system, please don't hesitate to contact J.K Incorporated and the EYN-DOS team via E-Mail or Discord. E-Mail: eyndos@gmail.com, Discord: EYN-DOS Support#9295. Our E-Mail and Discord systems are automated but by sending the message "human" to the E-Mail or Discord account, you will be automatically redirected to talk with a J.K Incorporated representative right away.

---

# Thank you for reading this manual. We hope you have a splendid day.

---

J.K Incorporated, the J.K Incorporated logo, J.K Music, the J.K Music logo, EYN-DOS, the EYN-DOS logo and other J.K Incorporated affiliations are protected titles under the BSD-3 Clause "New" or "Revised" License.
