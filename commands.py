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

# All commands below

def help():
    print("")
    print("help = Prints commands currently usable, ")
    print("listdir = Prints a list of available directories, ")
    print("dir = Prints a list of all available files in the current directory, ")
    print("run = Executes the file entered, ")
    print("end = Closes and resets the EYN-DOS terminal, ")
    print("ver = Prints the EYN-DOS version that is running, ")
    print("credits = Prints a list of all the people who worked on EYN-DOS, ")
    print("cd = Takes you to the directory entered, ")
    print("cdate = Prints the current date and time, ")
    print("read = Prints the contents of the file entered, ")
    print("find = Prints the directory path of the file entered, ")
    print("write = Writes custom text to the file entered (creates new file), ")
    print("del = Deletes any file entered, ")
    print("size = Prints the size of the file entered, ")
    print("clear = Clears the screen of all previously printed lines, ")
    print("md = Makes a directory with the name entered, ")
    print("copy = Copy and pastes the file selected in the path entered, ")
    print("echo = Prints the text entered.")
    print("colortest = Tests if the 'colorma' module is functional, ")
    print("edit = Appends (edits) the file entered, ")
    print("specs = Prints accessible system specifications, ")
    print("dirsize = Prints the size of the directory entered, ")
    print("newver = Downloads the most recent version of EYN-DOS (Requires internet), ")
    print("unzip = Extracts the contents of a zip file to a specified path,")
    print("zip = Compresses all files entered into a zip file,")
    print("pyedit = Runs the default Python editor, ")
    print("restart = Closes and re-opens EYN-DOS,")
    print("")

def listdir():
    print("")
    test=next(os.walk('.'))[1]
    print(test)
    print("")

def dir():
    print("")
    filenames = next(os.walk(dir_path))[2]
    print(filenames)
    print("")
    print(get_dir_size(cwd)) 
    print(" | Kilobytes")
    print("")

def end():
    print("")
    confirm=input("Are you sure you want to end your EYN-DOS session? (y/n): ")

    if confirm==("y"):
        print("")
        exit()
    
    if confirm==("n"):
        print("")
        print("Command aborted.")
        print("")

def lgr():
    print("")
    print("Hey, that's a good YouTube channel!")
    print("")
    
def errfni():
    print("")
    print(Fore.BLUE + "████████████████")
    print("\033[37;44mERROR EYN_C3-FNI\033[m")
    print(Fore.BLUE + "████████████████")
    print(Fore.RESET)
    print("")
    
def win():
    print("")
    print("No.")
    print("")

def count():
    print("")
    count_1=input("WARNING: THIS WILL MAKE EYN-DOS UNUSABLE FOR THE REST OF THE SESSION. CONTINUE? (y/n) ")
    print("")
    
    if count_1==("y"):
        print("")
        os.system('py counter.py')
        print("")
    
    if count_1==("n"):
        print("")
        print("Command disbanded")
        print("")

def troll():
    print("")
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
    print("░░░░░░░░░░░░░░░░░░█▄▄▄▄▄▄▄▄▀")
    print("")

def ver():
    print("")
    print("█████████   ███     ███   ███      ███            ██████       ██████      ██████")
    print("███           ███ ███     ██████   ███            ███   ███  ███    ███  ███")
    print("█████████       ███       ███  ███ ███   ██████   ███   ███  ███    ███    ██████")
    print("███             ███       ███    █████            ███   ███  ███    ███        ███")
    print("█████████       ███       ███      ███            ██████       ██████     ██████")
    print("")
    print("")
    print("                         █████            ███       █████")
    print("                       ██  ███         ███   ███  ██  ███")
    print("                           ███            ███         ███")
    print("                           ███         ███   ███      ███")
    print("                        █████████  ██     ███      █████████")
    print("")
    print("EYN-DOS 1.81 (Nov 29 2022)")
    print("")

def credits():
    print("")
    print("The EYN-DOS Team:")
    print("")
    print("    Primary coder: Kian Gentry (Founder and CEO of J.K Incorporated)")
    print("    Secondary coder: Ian Greeves (Musician and Lead Artist of J.K Incorporated.")
    print("    Logo designer: Kamil Makuch")
    print("    Staff commander: Kian Gentry")
    print("    Everyone involved: Kian Gentry, Ian Greeves, Kamil Makuch and other J.K Incorporated employees.")
    print("")
    print("    Honorable mentions:")
    print("")
    print("         Robin Andrews: Coder of the 'Snake' game included with EYN-DOS.")
    print("         shomikj: Coder of the command line version of 'Solitaire' for EYN-DOS.")
    print("         Cayden Jackson: Supporter.")
    print("         Kamil M: Supporter and artist.")
    print("         Github, StackOverflow & GeeksForGeeks: Saver of countless hours of research.")
    print("         You: For using EYN-DOS.")
    print("         Linux: Just awesome")
    print("")
    print("         Thank you for using EYN-DOS!")
    print("")

def cdate():
    print("")
    now = datetime.now()
    dt_string = now.strftime("%B %d %Y, %H:%M")
    print(dt_string)
    print("")

def read():
    print("")
    txt_name=input("Enter the name of the file you want to read. (Including extension): ")
    print("")
    f=open(txt_name, 'r')
    contents = f.read()
    print(contents)
    f.close
    print("")

def find():
    print("")
    file_find=input("What file do you want to find? (Including extension): ")
    print("")
    print(os.path.abspath(file_find))
    print("")

def write():
    print("")
    os.system("py write.py")
    print("")

def del1():
    print("")
    print("(Type 'nul0' to abort the command.)")
    print("")
    del_file=input("What file do you want to delete? (Including extension): ")
    print("")

    if del_file==(["main.py",
    "write.py",
    "commands.py",
    "RUNMEFIRST.py",
    "append.py",
    "c-date.py",
    "c-time.py",
    "counter.py",
    "mouse_detection.py",
    "LICENSE", 
    "launch.json", 
    "README.md"]):
        print("")
        print("This is a critical system file. No action will be taken.")
        print("")

    elif del_file==("nul"):
        print("")
        print("Returning to the EYN-DOS main terminal...")
        print("")

    else:
        print("Deleting file...")
        os.remove(del_file)
        print("")
        print("File deleted.")
        print("")

def size():
    print("")
    size_cl=input("What file do you want the size to? (Including extension): ")
    print("")
    print(os.path.getsize(size_cl)/1024)
    print(" | Kilobytes")
    print("")

def clear():
    print("")
    os.system("cls")

def run():
    print("")
    run_name=input("What file do you want to run? (extension included): ")
    print("")
    if run_name==("main.py"):
        print("")
        print("This is already running!")
        print("")
    else:
        os.system('py ' + run_name)
        print("")

def cd():
    print("")
    print("(Type 'nul0' to return to the EYN-DOS main terminal)")
    print("")
    cd_line=input("What sub-directory do you want to go to?: ")
    print("")
    if cd_line==("nul0"):
        print("Returning to the EYN-DOS main terminal...")
        print("")
    else:
        chdir(cd_line)

def cwd():
    print("")
    cwd=os.getcwd()
    print(cwd)
    print("")

def ctime():
    print("")
    lt = time.localtime()
    ctime = time.strftime("%H:%M:%S", lt)
    print(ctime)
    print("")

def md():
    print("")
    print("(Type 'nul' to return the EYN-DOS main terminal)")
    print("")
    md_line=input("What do you want to call the directory?: ")
    print("")
    if md_line==("nul"):
        print("Returning to the EYN-DOS main terminal...")
        print("")
    else:
        print("Creating...")
        print("")
        mkdir(md_line)
        print("Directory created.")
        print("")

def copy():
    print("")
    print("Type 'nul0' to abort the command.")
    print("")
    cpy_line=input("Where is the file you want to copy?: ")
    print("")
    pst_line=input("Where do you want to paste the file?: ")
    print("")
    if cpy_line==("nul0"):
        print("Returning to the EYN-DOS main terminal...")
        print("")
    else:
        print("Pasting...")
        print("")
        shutil.copyfile(cpy_line, pst_line)
        print("Pasted.")
        print("")

def echo():
    print("")
    echo_line=input("What do you want to echo?: ")
    print("")
    print(echo_line)
    print("")

def colortest():
    print("")
    print(Fore.BLUE +            "████████████████████████████████")
    print(Fore.CYAN +            "████████████████████████████████")
    print(Fore.GREEN +           "████████████████████████████████")
    print(Fore.MAGENTA +         "████████████████████████████████")
    print(Fore.RED +             "████████████████████████████████")
    print(Fore.YELLOW +          "████████████████████████████████")
    print(Fore.WHITE +           "████████████████████████████████")
    print(Fore.LIGHTBLUE_EX +    "████████████████████████████████")
    print(Fore.LIGHTCYAN_EX +    "████████████████████████████████")
    print(Fore.LIGHTGREEN_EX +   "████████████████████████████████")
    print(Fore.LIGHTMAGENTA_EX + "████████████████████████████████")
    print(Fore.LIGHTRED_EX +     "████████████████████████████████")
    print(Fore.LIGHTYELLOW_EX +  "████████████████████████████████")
    print(Fore.LIGHTBLACK_EX +   "████████████████████████████████")
    print(Fore.RESET + "")

def terry():
    print("")
    print("^^^~~7!~!!!^^~^^~~!!!^:..... .....          .^!!!!!!!!!!!!!!!!!!!")
    print("^^^^^7J?7~^^^~~^^:........ .............      :!!!!!!!!!!!!!!!!!!")
    print(":::^^^!J7~~~^:...... ..:^!?YJ!!!77!~^^.......  .^!!!~~~~~~~~~!!!!")
    print("::::::^~77^.....  .^75GB####BBBBBBGPP5J7~^^^:.. .:!!~~~~~~~~~~!!!")
    print("::::::::~^.....:!5B&&&&&&&#####BBBBGGGPPP5?7??~.. .^~!!~~~~~!!!!!")
    print("^:::::::^^...^JB##&&&&&&&&&##B###BBBBBGGPPP5?7?~:::^!!~!!!!!!!!!!")
    print("^^^^:::.^^^~P####&&&&&&&##########BBGGGP5Y7!!~~!:^P555?7777777777")
    print("^^^^^^:.^~?B#&&&&&&#&&####&&&&&&BPYYG&G7^~?YYY?~::5PPP5J?????????")
    print("^^^^^^^:.^P##&&&&&&######&&&##PJ~:.^P&G?5BBBGP5J^.?5GGGPJ????????")
    print("^^^^^^^^:.?###&########&&#BG5?.     :^::~G##BGP5J!7?PBBG5????????")
    print("^^^^^^^^^..5B#######&&&&&##G^          .7B###BGP5YJ??BPP5J???????")
    print("^^^^^^^^^:.:PBB###########G?.        .~5######BGPYYJ?YGBP7!J?????")
    print("^^^^^^^^^:::^YBB#GJ7?J??7!JP5~.   .:7G&&&&&&&#BBGPP5J?5B5..7?7!~!")
    print("^^^^^^^^^^::::!J?^::.  ..!BBGGPYJ5G#&&&##&&&&##BBBGGPYJ?!...:..::")
    print("^^^^^^^^^^::::::7J^       JBBGGGBBBB###&########BBBGGP5J??!:....:")
    print("^^^^^^^^^^^:::^:.:.      .7B#BGGGGGGB##&&######BBBBBBBP5J7?!~:...")
    print("^^^^^^^^^^^^^^::.    ..:~YBG#BBBGGGBBG####&&##BBGBBBBBGG577777777")
    print("^^^^^^^^^^^^^^^^^^.::^JB####B#&&#BGGGGB########BGGGBBBBG57J?777JY")
    print("^^^^^^^^^^^^^~~^^^^^^^~YB###BBGGPPG##BBBB##BBB##BGGBGGGP??5YJJ??J")
    print("^^^^^^^^^^^^~~~~~~^^^^^^!5BBBBGPPB##########B####GGGGGPY7PP5YYYYY")
    print("^^^^^^^^^^^^~~~~~~^^^^^~^~YBBB##GBB####BBPPGB####BPGGP57YPPP5555P")
    print("^^^^^^^^^^^^~~~~~^^^^^^^~~~75GG#GGGGPGGGBB#####B##BGG57!YPGPP5555")
    print("^^^^^^^^^^^^~~~~~~~~~~~~~~~^.~5GBGGPGBBB##BBBBB###BG57~J5PGGPPPP7")
    print("^^^^^^^^^^^^~~~~~~~~~!!!!!~7:..!5GBGGGGGGGBB##&&&&BG?~?Y5PP55YY?~")
    print("^^^^^^^^^^^^~~~~~~~~~~!!!!!7~^^.:~7Y5PPGGB##&&&&&#P7~7YYYY55YY577")
    print("^^^^^^^^^^^^~~~~~~~~~~~~!~^!!^^^^^. .!PB######BGPJ^^7???JY55PPJ7J")
    print("^^^^^^^^^^^^~~~~~~~~~~!7!~:~~^~!!^~:.  ^YPPP5J7~:..:~?Y5PGGGGY~~7")
    print("^^^^^^^^^^^^^~~~~~~~~!7J?!:~!~^~!!!^:^.  .:. .::^^!~~JYB###BJ7^~!")
    print("^^^^^^^^^^^^^^^^^^~~~!!7JY!^7!!^^~!!!~^^:^:..^?JJ!~!7JPPBBBJ77^^~")
    print("::::::::::::::::^~7!!!!!!!?!~^~~^^^~?!!!!7!!^^777??J?J5PBBJ~~~??J")
    print("               .~?J7~~!^^~!?7~^!~^::~^~^~!7?^^~~!!!7!~755?~~~7J7J")
    print("")
    print("A tribute to one of the greatest programmers ever, Terry A. Davis (Inventor & Programmer for TempleOS.)")
    print("While he might have been quite controversial, there's no denying he was a very smart guy.")
    print("His (racist) rants were due to various mental problems. Later in his life, Terry suffered from homelessness.")
    print("Some hated him, some loved him. All together, he was still a great man.")
    print("R.I.P Terrence Andrew Davis (1969 - 2018)")
    print("")

def edit():
    print("")
    os.system("py append.py")
    print("")

def specs():
    syst=platform.uname()
    print("")
    print(f"System(s) - {syst.system}" + ", EYN-DOS")
    print("")
    print(f"Name - {syst.node}")
    print("")
    print(f"Release(s) - {syst.release}" + ", Full")
    print("")
    print(f"Version(s) - {syst.version}" + ", 1.8")
    print("")
    print(f"Machine - {syst.machine}")
    print("")
    print(f"Processor(s) - {syst.processor}")
    print("")

def dirsize():
    print("")
    folder=input("What folder do you want to know the size to?: ")
    print("")
    print(getFolderSize(folder))
    print(" | Kilobytes")
    print("")

def newver():
    print("")
    URL = "https://github.com/JK-Incorporated/EYN-DOS/archive/refs/heads/eyndos-experimental.zip"
    response = requests.get(URL)
    open("eyndos.zip", "wb").write(response.content)

def unzip():
    print("")
    zippath=input("What is the (absolute) path to the zip file you want to extract?: ")
    print("")
    zippath2=input("Where do you want to extract the contents to? (Path): ")
    with zipfile.ZipFile(zippath, 'r') as zip_ref:
        zip_ref.extractall(zippath2)
    print("")

def zip():
    print("")
    nmz=input("What do you want to call your .zip file? (Extension included): ")
    print("")
    print("What files do you want to zip? (One at a time) (Extensions included):")
    print("Type 'nul0' to exit and zip the entered files.")
    print("")
    while True:
        flz=input("> ")

        if flz.lower() == "nul0":
            break
    
        with zipfile.ZipFile(nmz, "a") as f:
            f.write(flz)
    print("")

def pyedit():	
    print("")	
    os.system("py")	
    print("")

def restart():
    print("")
    ryn=input("Are you sure you want to restart your EYN-DOS session? (y/n): ")
    if ryn==("y"):
        print("")
        os.system("py main.py")
        exit()
    if ryn==("n"):
        print("")
        print("Command aborted.")
        print("")
