# Importing Modules

import time
from datetime import datetime
import zipfile
import platform
from colorama import *
import shutil
import os
from os import *
from os.path import *
import requests
from PIL import Image
from dir import *
import psutil
from termcolor import colored
import logging

# format for logging errors n that

lvl1=logging.DEBUG # uhhhhhh
fmt="[%(levelname)s] %(asctime)s - %(message)s" # uhhhhhhhhhhhhhhhhh
logging.basicConfig(level=lvl1, format=fmt) # uhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh

# Color/Colour variables (so i dont have to write them every single time)

wh=Fore.WHITE
b=Fore.BLACK
bl=Fore.BLUE
cy=Fore.CYAN
gr=Fore.GREEN
ma=Fore.MAGENTA
re=Fore.RED
ye=Fore.YELLOW
lbl=Fore.LIGHTBLUE_EX
lc=Fore.LIGHTCYAN_EX
lg=Fore.LIGHTGREEN_EX
lm=Fore.LIGHTMAGENTA_EX
lr=Fore.LIGHTRED_EX
ly=Fore.LIGHTYELLOW_EX
lb=Fore.LIGHTBLACK_EX
lw=Fore.LIGHTWHITE_EX
r=Fore.RESET

# finding system (os) name and making variables for the py command
# (Cross compatability (between windows and linux) reasons)

syst=platform.uname()
ps=platform.system() # checks host os name

if ps==("Windows"): # if name is windows
    osr = "py" # use py in terminal
else: # if its smt else (bash)
    osr = "python3" # use python3 in terminal

# that little yellow, blinking '!' thats used everywhere

inp=colored(f"{ly}!",attrs=["blink"])
inp2=colored(f"{lc}!",attrs=["blink"])

# Calculating directory size

cwd=os.getcwd()

dir_path=os.path.dirname(os.path.realpath(__file__))

filesys=[f for f in listdir(dir_path) if isfile(join(dir_path, f))]

# Getting directory size

def getFolderSize(folder):
    total = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total += getFolderSize(itempath)
    return total

def get_dir_size(dir_path):
    total = 0
    with os.scandir() as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
    return total

size=0
for path, dirs, files in os.walk(dir_path):
    for f in files:
        fp = os.path.join(path, f)
        size += os.path.getsize(fp)

# kian did all comments above (and wrote most of the code), idk what that all does, all i know is that it works so im not gonna touch it

# all the commands are under here (commented by ian greeves)

def help(): # just prints all the commands. not automated, has to be entered manually.
    print("help = Prints commands currently usable, ") # inception
    print("listdir = Prints a list of available directories, ") # cool command name, not very common
    print("dir = Prints a list of all available files in the current directory, ") # idk why its called dir and not files but im not complaining
    print("run = Executes the Python file entered, ") # cool but could be merged with noneyn
    print("end = Closes and resets the EYN-DOS terminal, ") # yup, it does that
    print("ver = Prints the EYN-DOS version that is running, ") # i hate having to update the version number here
    print("credits = Prints a list of all the people who worked on EYN-DOS, ") # i mean, yeah, pretty self-explanatory
    print("cd = Takes you to the directory entered, ") # im getting lazy with these comments, i did them from bottom to top (commands) but top to bottom (inside the commands) so you may see me drastically lose enthusiasm in real time
    print("cdate = Prints the current date and time, ") # idk why they dont merge cdate and ctime, actually, thats a good idea, ill note it down
    print("ctime = Prints the current time, including seconds,")
    print("read = Prints the contents of the file entered, ") # fixed!
    print("find = Prints the directory path of the file entered, ") # underrated
    print("write = Writes custom text to the file entered (creates new file), ") # i loved working on this command
    print("del = Deletes any file entered, ") # can delete main.py (dont actually do that)
    print("size = Prints the size of the file entered, ") # pretty good command, 8/10
    print("clear = Clears the screen of all previously printed lines, ") # cool for hiding what mischevious activities youve been doing, 7/10
    print("md = Makes a directory with the name entered, ") # essential
    print("copy = Copy and pastes the file selected in the path entered, ") # great command, 9/10
    print("echo = Prints the text entered.") # im pretty bored writing these comments, its like midnight and i wanna go to bed, but im determined to do this
    print("colortest = Tests if the 'colorma' module is functional, ") # works 89% of the time
    print("terry = Tribute to a legend. Rest in peace.")
    print("edit = Appends (edits) the file entered, ") # i wouldnt call it 'editing' personally, just sorta like adding onto it
    print("usage = Prints the current CPU and RAM usage, ") # eh, not the best, 4/10
    print("dirsize = Prints the size of the directory entered, ") # cool, 6/10
    print("newver = Downloads the most recent version of EYN-DOS (Requires internet), ") # pairs nicely with the zip and unzip commands, and can be used for alot more, 8/10
    print("unzip = Extracts the contents of a zip file to a specified path,") # great command, 8/10
    print("zip = Compresses all files entered into a zip file,") # very cool, 9/10
    print("pyedit = Runs the default Python editor, ") # reminds me of the pcs with basic installed on them, and pretty useful, 7/10
    print("restart = Closes and re-opens EYN-DOS,") # really useful for development and debugging, 9/10
    print("prevd = Shows all directories in the previous directory, ") # sorta useful i guess, 7/10
    print("prevf = Shows all files in the previous directory, ") # same as above, 7/10
    print("noneyn = Executes any command entered in your host terminal,") # useful for defeating the purpose of eyndos, 8/10
    print("rim = Shows the contents of the image entered,") # cool novelty, not really useful, 6/10
    print("eyndir = Changes the directory to the EYN-DOS root directory,") # i cant be bothered commenting this
    print("pip = Provides an EYN-ified version of pip (Python's package manager),")
    print("home = Takes you to the root directory of your system ('C:' for Windows, '/' for Linux),")
    print("root = Takes you to your user folder ('This PC' for Windows, '~' for Linux),")
    print()

def listdir():
    dirs=next(os.walk('.'))[1] # finds all sub-directories (1) in the current directory (.)
    print(dirs) # prints sub-directory names
    print()

def dir():
    fn=next(os.walk("."))[2] # finds list of all files (2) in the current directory (.)
    print(fn) # prints filenames
    print()
    print(get_dir_size(cwd)) # prints size of current directory
    print(" | Bytes")
    print()

def end():
    cnfrm=input(f"{r}Are you sure you want to end your EYN-DOS session? (y/n){inp2} {wh}") # variable for confirming exit
    print(f"{r}")
    if cnfrm==("y"): # if response is y
        exit() # exit eyndos
    if cnfrm==("n"): # if response is n
        print("Command aborted.") # abort command
        print()

def lgr():
    print("Hey, that's a good YouTube channel!") # lgr is pretty good tbh
    print()
    
def errfni():
    print(f"{lr}"), logging.error("FNI")
    print()

def win():
    print("No.") # dont even think about it
    print()

def count(): # this command is so pointless but i love it
    c1=input(f"{lr}WARNING: THIS WILL MAKE EYN-DOS UNUSABLE FOR THE REST OF THE SESSION. CONTINUE? (y/n){inp2} {wh}") # variable for confirming counting
    print(f"{r}")
    if c1==("y"): # if response is y
        chdir(drnm)
        os.system(f"{osrunner} counter.py") # opens counter.py
        print()
    if c1==("n"): # if response is n
        print("Command disbanded") # return to terminal
        print()

def troll():
    print("░░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄▄")
    print("░░░░░█░░░░░░░░░░░░░░░░░░▀▀▄")
    print("░░░░█░░░░░░░░░░░░░░░░░░░░░░█")
    print("░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█")
    print("░▄▀░▄▄▄░░█▀▀▀▀▄▄█░░░██▄▄█░░░░█")
    print("█░░█░▄░▀▄▄▄▀░░░░░░░░█░░░░░░░░░█")
    print("█░░█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄░█")
    print("░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█")
    print("░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█")
    print("░░░█░░░░██░░▀█▄▄▄█▄▄█▄▄██▄░░█")
    print("░░░░█░░░░▀▀▄░█░░░█░█▀█▀█▀██░█")
    print("░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█")
    print("░░░░░░░▀▄▄░░░░░░░░░░░░░░░░░░░█")
    print("░░░░░░░░░░▀▀▄▄░░░░░░░░░░░░░░░█")
    print("░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█")
    print("░░░░░░░░░░░░░░░░░░█▄▄▄▄▄▄▄▄▀") # trolly
    print()

def ver():
    print(f"{lm}█████████   ███     ███   ███      ███            ██████       ██████      ██████")
    print("███           ███ ███     ██████   ███            ███   ███  ███    ███  ███")
    print("█████████       ███       ███  ███ ███   ██████   ███   ███  ███    ███    ██████")
    print("███             ███       ███    █████            ███   ███  ███    ███        ███")
    print("█████████       ███       ███      ███            ██████       ██████     ██████")
    print()
    print("                          █████         ████████    ████")
    print("                        ██     ███      ██        ██ ███")
    print("                            ███         ███████      ███")
    print("                         ███                  ██     ███")
    print("                         █████████  ██  ███████    ███████")
    print()
    print(f"{wh}EYN-DOS 2.51 (May 21 2023)")
    print()

def credits():
    print("The EYN-DOS Team:")
    print()
    print("    Primary coder: Kian Gentry (Founder and CEO of J.K Incorporated)") # boss man
    print("    Secondary coder: Ian Greeves (Junior Programmer of J.K Incorporated.") # look, its me!
    print("    Logo designer: Kamil Makuch") # great guy
    print("    Staff commander: Kian Gentry") # boss man again
    print("    Everyone involved: Kian Gentry, Ian Greeves, Kamil Makuch and other J.K Incorporated employees.") # 'other' being the janitors
    print()
    print("    Honorable mentions:")
    print()
    print("         Robin Andrews: Coder of the 'Snake' game included with EYN-DOS.") 
    print("         shomikj: Coder of the command line version of 'Solitaire' for EYN-DOS.")
    print("         Cayden Jackson: Supporter.") # short guy
    print("         Kamil Makuch: Supporter and artist.") # the man again
    print("         Github, StackOverflow & GeeksForGeeks: Saver of countless hours of research.") # i use these too often for my own good
    print("         You: For using EYN-DOS.") # aww thats cute
    print("         Linux: Just awesome.") # mhm
    print("         Terrance Davis: Inspiration.")
    print()
    print("         Thank you for using EYN-DOS!") # really, thank you!
    print()

def cdate():
    now = datetime.now() # finds todays date
    dt=now.strftime("%B %d %Y, %H:%M") # variable for formatting date into month:day:year, hour:minutes
    print(dt) # prints date
    print()

def read():
    os.system(f"{osr} read.py") # opens read.py
    print()

def find():
    ff=input(f"{r}What file do you want to find? (Including extension){inp2} {wh}") # variable for file to look for
    print(f"{r}")
    print(os.path.abspath(ff)) # prints absolute path of file entered
    print()

def write():
    os.system(f"{osr} write.py") # opens write.py
    print()

def del1():
    print("(Type 'nul0' to abort the command)")
    print()
    df=input(f"{r}What file do you want to delete? (Including extension){inp2} {wh}") # variable for name of file to delete
    print(f"{r}")
    if df==("nul0"): # if response is nul0
        print("Returning to the EYN-DOS main terminal...") # return to command-line
        print()
    else:
        print("Deleting file...")
        os.remove(df) # removes file completely
        print()
        print("File deleted.")
        print()

def size():
    size_cl=input(f"{r}What file do you want the size to? (Including extension){inp} {wh}") # variable for name of file to find size of
    print()
    print(os.path.getsize(size_cl)) # gets size of file in bytes
    print(" | Bytes")
    print()

def clear():
    if ps==("Windows"): # if name is windows
        os.system("cls") # use windows clear command
    else:
        os.system("clear")

def run():
    print("(Type 'e' to return to the EYN-DOS main terminal)")
    print()
    run_name=input(f"What file do you want to run? (extension included){inp2} {wh}") # variable for python file to run
    print(f"{r}")
    if run_name==("e"): # if response is e
        print("Command Aborted.") # abort command
        print()
    else:
        os.system(f"{osr} {run_name}") # runs the python file entered
        print()

def cd():
    print("(Type 'e' to return to the EYN-DOS main terminal)")
    print()
    cdd=input(f"What sub-directory do you want to go to?{inp2} {wh}") # variable for name of sub-directory
    print(f"{r}")
    if cdd==("e"): # if response is nul0
        print("Returning to the EYN-DOS main terminal...") # return to command-line
        print()
    else:
        chdir(cdd) # change directory to entered sub-directory name

def cwd():
    cwd=os.getcwd() # variable for finding current working directory
    print(cwd) # prints current working directory
    print()

def ctime():
    lt=time.localtime() # variable for finding time
    ct=time.strftime("%H:%M:%S", lt) # variable for formatting the time in an hour:minute:second format
    print(ct) # prints time
    print()

def md():
    print("(Type 'e' to return the EYN-DOS main terminal)")
    print()
    mdn=input(f"What do you want to call the directory?{inp2} {wh}") # variable for directory name
    print(f"{r}")
    if mdn==("e"): # if response is e
        print("Returning to the EYN-DOS main terminal...") # return to command-line
        print()
    else:
        print("Creating...")
        print()
        mkdir(mdn) # make directory with entered name
        print("Directory created.")
        print()

def copy():
    print("Type 'e' to abort the command.")
    print()
    cpy=input(f"Where is the file you want to copy?{inp2} {wh}") # variable for absolute path of file to copy
    print(f"{r}")
    pst=input(f"Where do you want to paste the file?{inp2} {wh}") # variable for path to paste file to
    print(f"{r}")
    if cpy==("e"): # if e is entered
        print("Returning to the EYN-DOS main terminal...") # go back to command-line
        print()
    else:
        print("Pasting...")
        print()
        shutil.copyfile(cpy, pst) # copies entered file to path entered
        print("Pasted.")
        print()

def colortest():
    print(f"{bl}████████████████████████████████") # prints all text in colour after 'f"'
    print(f"{cy}████████████████████████████████")
    print(f"{gr}████████████████████████████████")
    print(f"{ma}████████████████████████████████")
    print(f"{re}████████████████████████████████")
    print(f"{ye}████████████████████████████████")
    print(f"{wh}████████████████████████████████")
    print(f"{lbl}████████████████████████████████")
    print(f"{lc}████████████████████████████████")
    print(f"{lg}████████████████████████████████")
    print(f"{lm}████████████████████████████████")
    print(f"{lr}████████████████████████████████")
    print(f"{ly}████████████████████████████████")
    print(f"{lb}████████████████████████████████")
    print(f"{r}")

def terry():
    print()
    print(f"{wh}~~~~^^^^^::^^^^^^^..::7PPY!~^^~~~?YYYYPJ????????J?")
    print("YYYYJJ?^....~JYPP7::..^Y7:       .?PP55555YYYJJJ??")
    print("~!~!!!!^~~^..^:?#?.               :PPP55555YYYJJJ?")
    print("J???J?JJJJYJ?7?J~:.               ^GPPPP5555YYYJJJ")
    print("^~^^^^^^^^^!7?YYY?~  ....         ^5PPPP5555YYYJJJ")
    print("::::::.....:^~!?PGJ.!7?PG?~^        .:!55555YYYJJ?")
    print(":..^^^::::::::::^~^75GGGPP5?^.:..      .7555YYYJJJ")
    print("^::^^^::::::~~~^^^^~Y#GG5GB!:^^::..      77!!~!~~!")
    print("::::.      .^~~~~~~~!PGBGPY~~^^^^:::    ^~~^^.:.::")
    print(".....   .. :^~~~~~^~~!GBGY!~^^^^^^^:.   ..::::....")
    print("         ::^^^^:::^^^^~JJ!^^^^:^^^::        ...   ")
    print(" J.      :!~~^:   ..:^^^^^::::::^:::..        .  .")
    print(" ?: .....^PB5^      :::^::::^^^^:::~!~:...    ....")
    print(" ::~JYYYJ5BP?:.... ........:7Y57:..^!!~:     ~&&#B")
    print("  .....^JG&&&&&&&####BBBGGPPPP^^....:^^:     ?@@@@")
    print(" .::...75B@BYY555555555555PG##:.....::^.  .:.5@@@&")
    print(" ::::.:7Y#@PJYYYYYYYJJJ??7!J#B:  ...::.  .:..B@@&&")
    print(".^^^^:^?J#&P5PPPPPPP55YJ?77J#B:  ...::  .::..B@@@&")
    print(":^^^^^~JJ&&GGGBBBBBGGP5YJ?7Y#G~. ..::.  ....:P###&")
    print("::^^^:^JG@&BB##&@&#BBGG5YJ?5#G~  .:... .:::.:~!777")
    print(".::^^.~P5@&&##&@@&#BBGG5YJJG#G?. ....  ::::::^~~~~")
    print(":^:^^~?5P@@@@@@@@@@@@&&&&###&GY::?!!!~:^^^::?#BP5Y")
    print("^^~^~~!75#&##&&&&&&&&&@&&&@@&5Y^:JBBGP?^^^^:P@&BBP")
    print("^~~~~!!!!!!~~~~~~~~~~~~!!!7?!^:::^YGGG5~^^^^B@&&&&")
    print("^^!!~~~!!!!!!~^^^^::::.:..:::.....^!??7^:::^&&&&&&")
    print("::^~~~~~!!!!!~~^^^^::::::::::::::^::^^^^:..!&&&&##")
    print()
    print("A tribute to one of the greatest programmers ever, Terry A. Davis (Inventor & Programmer for TempleOS.)")
    print("While he might have been quite controversial, there's no denying he was a very smart guy.")
    print("His rants were due to various mental problems, such as schizophrenia. Later in his life, Terry suffered from homelessness.")
    print("Some hated him, some loved him. All together, he was still a great man.")
    print("R.I.P Terrence Andrew Davis (1969 - 2018)") # rest in peace, legend
    print()

def edit():
    os.system(f"{osr} append.py")
    print()

def specs():
    load1, load5, load15=psutil.getloadavg() # gets cpu average from 15 minutes
    cpuu=(load15/os.cpu_count()) * 100 # divides average across all cores
    print(f"{syst.node} Usage:") # pc name
    print()
    print("CPU Usage: ", cpuu,"%") # prints usage
    print()
    print("RAM Usage: ", psutil.virtual_memory()[2],"%") # uhhh just gets the memory usage in percentage
    print("RAM Usage (Bytes): ", psutil.virtual_memory()[3]) # gets memory usage in bytes
    print()

def dirsize():
    folder=input(f"What folder do you want to know the size to?{inp} {wh}") # variable for folder name in current directory
    print()
    print(getFolderSize(folder)) # prints size of the folder entered
    print(" | Bytes")
    print()

def newver():
    URL="https://github.com/JK-Incorporated/EYN-DOS/archive/refs/heads/Main.zip" # eyndos download url
    response=requests.get(URL) # variable for requesting the content from the url
    open("eyndos.zip", "wb").write(response.content) # writes content from url (download page) to 'eyndos.zip'
    print(f"Newest EYN-DOS version successfully saved as 'eyndos.zip' in {os.getcwd()}.")
    print()

def unzip():
    zippath=input(f"What is the (absolute) path to the zip file you want to extract?{inp2} {wh}") # variable for absolute path for zip file
    print()
    zippath2=input(f"Where do you want to extract the contents to? (Path){inp2} {wh}") # variable for regular path of where to extract files
    with zipfile.ZipFile(zippath, 'r') as zip_ref: # opens zip file in 'read' mode
        zip_ref.extractall(zippath2) # extracts all contents into the path entered
    print(f"{r}")

def zip():
    nmz=input(f"What do you want to call your .zip file? (Extension included){inp2} {wh}") # variable for file name
    print(f"{r}")
    print(f"What files do you want to zip? (One at a time) (Extensions included):")
    print("Type 'nul0' to exit and zip the entered files.")
    print()
    while True:
        flz=input(f"> {wh}") # whatever filename is typed is saved in the zip file
        if flz.lower() == "nul0": # if filename is nul0, create the zip file with all entered filenames before
            break
        with zipfile.ZipFile(nmz, "a") as f: # opens created zipfile in 'append' mode
            f.write(flz) # adds all files entered into the zip file
    print(f"{r}")

def pyedit():
    os.system(osr)
    print()

def restart():
    ryn=input(f"Are you sure you want to restart your EYN-DOS session? (y/n){inp2} {wh}") # variable for user response
    print()
    if ryn==("y"): # if response is y
        chdir(drnm)
        os.system(f"{osr} main.py")
        exit() # exits the first opened main file (current)
    if ryn==("n"): # if response is n 
        print("Command aborted.") # continue with command line
        print()

def prevdir():
    pdirs=next(os.walk('..'))[1] # finds all directories (1) in the previous directory (..)
    print(pdirs)
    print()

def prevfiles():
    pfn=next(os.walk(".."))[2] # find all filenames (2) in the previous directory (..)
    print(pfn) # prints the filenames
    print()
    print(get_dir_size(cwd)) # finds the size of all the files in the current directory
    print(" | Bytes")
    print()

def noneyn():
    nec=input(f"What non-EYN command do you want to execute?{inp2} {wh}") # variable of what host-system command to execute
    print(f"{r}")
    os.system(nec) # executes the variable in the host-terminal
    print()

def rim():
    img=input(f"What image do you want to read? (Including extension){inp2} {wh}") # variable for image name
    print(f"{r}")
    im=Image.open(img, mode='r') # opens image name in current directory in 'read' mode
    im.show() # shows the image

def ren():
    renx=input(f"What file do you want to rename?{inp2} {wh}") # variable for original file/folder to rename
    print(f"{r}")
    reny=input(f"What do you want to rename the file?{inp2} {wh}") # variable for what to rename it to
    print(f"{r}")
    os.rename(renx, reny) # renames the file entered to the new name entered
    print("File renamed.")
    print()

def eyndir():
    print("Returning to EYN-DOS main directory...")
    chdir(drnm)
    print()

def pip():
    print("What Python package do you want to install?")
    print("(Type 'nul0' to return)")
    print()
    pkgn=input(f"?> {wh}")
    print(f"{r}")
    if pkgn==("nul0"):
        print("Returning to the EYN-DOS terminal...")
        print()
    else:
        os.system(f"pip install {pkgn}")

def tr():
    if ps==("Windows"): # if name is windows
        os.chdir("C:")
        print("Taking you to the 'C:' directory...")
        print()
    else: # if its smt else (bash)
        os.chdir("/")
        print("Taking you to the '/' directory...")
        print()

def rr():
    usrd=os.path.expanduser('~')
    os.chdir(usrd)
    if ps==("Windows"): # if name is windows
        print("Taking you to 'This PC'...")
        print()
    else: # if its smt else (prob bash)
        print("Taking you to '~'...")
        print()

def dbg():
    print("Welcome to the 'dbg' command!")
    print("This command is used in EYN-DOS development to test new commands and features before being fully integrated.")
    print("This command may be of no use to the average user, but to the development team, it's really handy!")
    print("We hope you enjoy EYN-DOS!")
    print()

# EYN-DOS: March 15 2022 - Present (May 21 2023)