# Importing Modules

import time
from datetime import datetime
import zipfile
import platform
import shutil
import os
from os import *
from os.path import *
import requests
from PIL import Image

# Calculating directory size

cwd = os.getcwd()

dir_path = os.path.dirname(os.path.realpath(__file__))

filesys = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]

# Getting directory size

def getFolderSize(folder):
    total = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total += getFolderSize(itempath)
    return total/1024

def get_dir_size(dir_path):
    total = 0
    with os.scandir() as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
    return total/1024

size=0
for path, dirs, files in os.walk(dir_path):
    for f in files:
        fp = os.path.join(path, f)
        size += os.path.getsize(fp)

# kian did all comments above (and wrote most of the code), idk what that all does, all i know is that it works so im not gonna touch it

# all the commands are under here (commented by ian greeves)

def help(): # just prints all the commands. not automated, has to be entered manually.
    print("")
    print("help = Prints commands currently usable, ") # inception
    print("listdir = Prints a list of available directories, ") # cool command name, not very common
    print("dir = Prints a list of all available files in the current directory, ") # idk why its called dir and not files but im not complaining
    print("run = Executes the Python file entered, ") # i corrected it
    print("end = Closes and resets the EYN-DOS terminal, ") # yup, it does that
    print("ver = Prints the EYN-DOS version that is running, ") # i hate having to update the version number here
    print("credits = Prints a list of all the people who worked on EYN-DOS, ") # me
    print("cd = Takes you to the directory entered, ") # im getting lazy with these comments, i did them from bottom to top (commands) but top to bottom (inside the commands) so you may see me drastically lose enthusiasm in real time
    print("cdat = Prints the current date and time, ") # idk why they dont merge cdate and ctime, actually, thats a good idea, ill note it down
    print("read = Prints the contents of the file entered, ") # fixed!
    print("find = Prints the directory path of the file entered, ") # underrated
    print("write = Writes custom text to the file entered (creates new file), ") # i loved working on this command
    print("del = Deletes any file entered, ") # can delete main.py (dont actually do that)
    print("size = Prints the size of the file entered, ") # pretty good command, 8/10
    print("clear = Clears the screen of all previously printed lines, ") # cool for hiding what mischevious activities youve been doing, 7/10
    print("md = Makes a directory with the name entered, ") # essential
    print("copy = Copy and pastes the file selected in the path entered, ") # great command, 9/10
    print("edit = Appends (edits) the file entered, ") # i wouldnt call it 'editing' personally, just sorta like adding onto it
    print("specs = Prints accessible system specifications, ") # eh, not the best, 4/10
    print("dirsize = Prints the size of the directory entered, ") # cool, 6/10
    print("newver = Downloads the most recent version of EYN-DOS Minimal (Requires internet), ") # pairs nicely with the zip and unzip commands, and can be used for alot more, 8/10
    print("unzip = Extracts the contents of a zip file to a specified path,") # great command, 8/10
    print("zip = Compresses all files entered into a zip file,") # very cool, 9/10
    print("pyedit = Runs the default Python editor, ") # reminds me of the pcs with basic installed on them, and pretty useful, 7/10
    print("restart = Closes and re-opens EYN-DOS,") # really useful for development and debugging, 9/10
    print("prevd = Shows all directories in the previous directory, ") # sorta useful i guess, 7/10
    print("prevf = Shows all files in the previous directory, ") # same as above, 7/10
    print("noneyn = Executes any command entered in your host terminal,") # useful for defeating the purpose of eyndos, 8/10
    print("rim = Shows the contents of the image entered,") # cool novelty, not really useful, 6/10
    print("")

def listdir():
    print("")
    dirs=next(os.walk('.'))[1] # finds all sub-directories (1) in the current directory (.)
    print(dirs) # prints sub-directory names
    print("")

def dir():
    print("")
    filenames = next(os.walk("."))[2] # finds list of all files (2) in the current directory (.)
    print(filenames) # prints filenames
    print("")
    print(get_dir_size(cwd)) # prints size of current directory
    print(" | Kilobytes")
    print("")

def end():
    print("")
    exit()

def ver():
    print("")
    print("█████████   ███     ███   ███      ███            ██████       ██████      ██████")
    print("███           ███ ███     ██████   ███            ███   ███  ███    ███  ███")
    print("█████████       ███       ███  ███ ███   ██████   ███   ███  ███    ███    ██████")
    print("███             ███       ███    █████            ███   ███  ███    ███        ███")
    print("█████████       ███       ███      ███            ██████       ██████     ██████")
    print("")
    print("")
    print("                                █████            ███")
    print("                              ██     ███      ███   ███")
    print("                                  ███         ███   ███")
    print("                               ███            ███   ███")
    print("                               █████████  ██     ███")
    print("")
    print("EYN-DOS Minimal 2.0 (Dec 23 2022)")
    print("")

def credits():
    print("")
    print("Ian Greeves... Yeah, I made the entirety of EYN-DOS Minimal.")
    print("I'm normally the guy who just comments the code, not writing it!")
    print("Oh well, I hope you enjoy EYN-DOS Minimal!")

def cdat():
    print("")
    now = datetime.now() # finds todays date
    dt_string = now.strftime("%B %d %Y") # variable for formatting date into month:day:year, hour:minutes
    print(dt_string) # prints date
    lt = time.localtime() # variable for finding time
    ctime = time.strftime("%H:%M:%S", lt) # variable for formatting the time in an hour:minute:second format
    print("")
    print(ctime) # prints time
    print("")

def read():
    print("")
    os.system("py read.py")
    print("")

def find():
    print("")
    file_find=input("What file do you want to find? (Including extension): ") # variable for file to look for
    print("")
    print(os.path.abspath(file_find)) # prints absolute path of file entered
    print("")

def write():
    print("")
    os.system("py write.py") # opens write.py
    print("")

def del1():
    print("")
    print("(Type 'nul0' to abort the command.)")
    print("")
    del_file=input("What file do you want to delete? (Including extension): ") # variable for name of file to delete
    print("")
    if del_file==("nul0"): # if response is nul0
        print("")
        print("Returning to the EYN-DOS main terminal...") # return to command-line
        print("")
    else:
        print("Deleting file...")
        os.remove(del_file) # removes file completely
        print("")
        print("File deleted.")
        print("")

def size():
    print("")
    size_cl=input("What file do you want the size to? (Including extension): ") # variable for name of file to find size of
    print("")
    print(os.path.getsize(size_cl)/1024) # gets size of file in bytes, then divides by 1024 to get kibibytes (kilobytes for compatibility)
    print(" | Kilobytes")
    print("")

def clear():
    print("")
    os.system("cls")

def run():
    print("")
    print("(Type 'nul0' to return to the EYN-DOS main terminal)")
    print("")
    run_name=input("What file do you want to run? (extension included): ") # variable for python file to run
    print("")
    if run_name==("nul0"): # if response is nul0
        print("Command Aborted.") # abort command
        print("")
    else:
        os.system('py ' + run_name) # run python file entered
        print("")

def cd():
    print("")
    print("(Type 'nul0' to return to the EYN-DOS main terminal)")
    print("")
    cd_line=input("What sub-directory do you want to go to?: ") # variable for name of sub-directory
    print("")
    if cd_line==("nul0"): # if response is nul0
        print("Returning to the EYN-DOS main terminal...") # return to command-line
        print("")
    else:
        chdir(cd_line) # change directory to entered sub-directory name

def cwd():
    print("")
    cwd=os.getcwd() # variable for finding current working directory
    print(cwd) # prints current working directory
    print("")

def md():
    print("")
    print("(Type 'nul0' to return the EYN-DOS main terminal)")
    print("")
    md_line=input("What do you want to call the directory?: ") # variable for directory name
    print("")
    if md_line==("nul0"): # if response is nul0
        print("Returning to the EYN-DOS main terminal...") # return to command-line
        print("")
    else:
        print("Creating...")
        print("")
        mkdir(md_line) # make directory with entered name
        print("Directory created.")
        print("")

def copy():
    print("")
    print("Type 'nul0' to abort the command.")
    print("")
    cpy_line=input("Where is the file you want to copy?: ") # variable for absolute path of file to copy
    print("")
    pst_line=input("Where do you want to paste the file?: ") # variable for path to paste file to
    print("")
    if cpy_line==("nul0"): # if nul0 is entered
        print("Returning to the EYN-DOS main terminal...") # go back to command-line
        print("")
    else:
        print("Pasting...")
        print("")
        shutil.copyfile(cpy_line, pst_line) # copies entered file to path entered
        print("Pasted.")
        print("")

def edit():
    print("")
    os.system("py append.py")
    print("")

def specs():
    syst=platform.uname()
    print("")
    print(f"System(s) - {syst.system}" + ", EYN-DOS") # os name
    print("")
    print(f"Name - {syst.node}") # pc name
    print("")
    print(f"Release(s) - {syst.release}" + ", Minimal") # release of os
    print("")
    print(f"Version(s) - {syst.version}" + ", 2.0") # version of os
    print("")
    print(f"Machine - {syst.machine}") # processor distributor/pc manufacturer
    print("")
    print(f"Processor(s) - {syst.processor}") # processor model
    print("")

def dirsize():
    print("")
    folder=input("What folder do you want to know the size to?: ") # variable for folder name in current directory
    print("")
    print(getFolderSize(folder)) # prints size of the folder entered
    print(" | Kilobytes")
    print("")

def newver():
    print("")
    URL = "https://github.com/JK-Incorporated/EYN-DOS/archive/refs/heads/EYN-DOS-Minimal.zip" # eyndos download url
    response = requests.get(URL) # variable for requesting the content from the url
    open("eyndos.zip", "wb").write(response.content) # writes content from url (download page) to 'eyndos.zip'

def unzip():
    print("")
    zippath=input("What is the (absolute) path to the zip file you want to extract?: ") # variable for absolute path for zip file
    print("")
    zippath2=input("Where do you want to extract the contents to? (Path): ") # variable for regular path of where to extract files
    with zipfile.ZipFile(zippath, 'r') as zip_ref: # opens zip file in 'read' mode
        zip_ref.extractall(zippath2) # extracts all contents into the path entered
    print("")

def zip():
    print("")
    nmz=input("What do you want to call your .zip file? (Extension included): ") # variable for file name
    print("")
    print("What files do you want to zip? (One at a time) (Extensions included):")
    print("Type 'nul0' to exit and zip the entered files.")
    print("")
    while True:
        flz=input("> ") # whatever filename is typed is saved in the zip file
        if flz.lower() == "nul0": # if filename is nul0, create the zip file with all entered filenames before
            break
        with zipfile.ZipFile(nmz, "a") as f: # opens created zipfile in 'append' mode
            f.write(flz) # adds all files entered into the zip file
    print("")

def pyedit():	
    print("")	
    os.system("py")	
    print("")

def restart():
    print("")
    ryn=input("Are you sure you want to restart your EYN-DOS session? (y/n): ") # variable for user response
    if ryn==("y"): # if response is y
        print("")
        os.system("py main.py") # open main file
        exit() # exits the first opened main file (current)
    if ryn==("n"): # if response is n 
        print("")
        print("Command aborted.") # continue with command line
        print("")

def prevdir():
    print("")
    pdirs=next(os.walk('..'))[1] # finds all directories (1) in the previous directory (..)
    print(pdirs)
    print("")

def prevfiles():
    print("")
    filenames = next(os.walk(".."))[2] # find all filenames (2) in the previous directory (..)
    print(filenames) # prints the filenames
    print("")
    print(get_dir_size(cwd)) # finds the size of all the files in the current directory
    print(" | Kilobytes")
    print("")

def noneyn():
    print("")
    nonec=input("What non-EYN command do you want to execute?: ") # variable of what host-system command to execute
    os.system(nonec) # executes the variable in the host-terminal
    print("")

def rim():
    print("")
    img=input("What image do you want to read? (Including extension): ") # variable for image name
    print("")
    im=Image.open(img, mode='r') # opens image name in current directory in 'read' mode
    im.show() # shows the image

# thanks for reading my silly little comments. have a good day (or night if youre like me and are making code comments at midnight)