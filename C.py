# Importing modules required (Download all for proper function) #

from colorama import Fore
import shutil
import os
from os import chdir, listdir, mkdir
from os.path import isfile, join

# Start of calculating directory size #

dir_path = os.path.dirname(os.path.realpath(__file__))

filesys = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]

def get_dir_size(dir_path):
    total = 0
    with os.scandir(dir_path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total/1024

size=0
for path, dirs, files in os.walk(dir_path):
    for f in files:
        fp = os.path.join(path, f)
        size += os.path.getsize(fp)

# End of calculating directory size #

while True:
    command_line=input("C/} ")

# All commands below #

    if command_line==("help"):
        print("")
        print("help = Prints commands currently usable, ")
        print("listdir = Prints a list of available directories, ")
        print("dir = Prints a list of all available files in the current directory, ")
        print("run = Executes the file entered, ")
        print("end = Closes and resets the EYN-DOS terminal, ")
        print("ver = Prints the EYN-DOS version that is running, ")
        print("credits = Prints a list of all the people who worked on EYN-DOS, ")
        print("cd (File/Folder location) = Takes you to the directory entered, ")
        print("cdate = Prints the current date and time, ")
        print("read = Prints the contents of the file entered, ")
        print("find = Prints the directory path of the file entered, ")
        print("write = Writes 25 lines of custom text to the file entered (creates new file), ")
        print("del = Deletes any newly writtten file entered, ")
        print("size = Prints the size of the file entered, ")
        print("clear = Clears the screen of all previously printed lines, ")
        print("errorlist = Prints all error codes and their meanings.")
        print("A = Takes you to the A drive (Floppy disk drive 1)")
        print("B = Takes you to the B drive (Floppy disk drive 2)")
        print("C = Takes you to the C drive (Hard drive)")
        print("D = Takes you to the D drive (Recovery drive)")
        print("E = Takes you to the E drive (Compact Disc drive)")
        print("md = Makes a directory with the name entered.")
        print("copy = Copy and pastes the file selected in the path entered.")
        print("echo = Prints the text entered.")
        print("")

    if command_line==("listdir"):
        print("")
        print("temp", " - ", float(size)/1024, " Kilobytes")
        print("")

    if command_line==("dir"):
        print("")
        print(filesys)
        print("")
        print(get_dir_size(dir_path)) 
        print(" | Kilobytes")
        print("")

    if command_line==("end"):
        print("")
        exit()

    if command_line==("lgr"):
        print("")
        print("Hey, that's a good YouTube channel!")
        print("")
    
    if command_line==("fdisk"):
        print(Fore.BLUE + "████████████████")
        print("\033[37;44mERROR EYN_C3-FNI\033[m")
        print(Fore.BLUE + "████████████████")
    
    if command_line==("win"):
        print("")
        print("No.")
        print("")

    if command_line==("count"):
        print("")
        count_1=input("WARNING: THIS WILL MAKE EYN-DOS UNUSABLE FOR THE REST OF THE SESSION. CONTINUE? (y/n) ")
        print("")
        
        if count_1==("y"):
            print("")
            os.system('python3 counter.py')
            print("")
        
        if count_1==("n"):
            print("")
            print("Command disbanded")
            print("")

    if command_line==("troll"):
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

    if command_line==("ver"):
        print("")
        print("█████████   ███     ███   ███      ███            ██████       ██████      ██████")
        print("███           ███ ███     ██████   ███            ███   ███  ███    ███  ███")
        print("█████████       ███       ███  ███ ███   ██████   ███   ███  ███    ███    ██████")
        print("███             ███       ███    █████            ███   ███  ███    ███        ███")
        print("█████████       ███       ███      ███            ██████       ██████     ██████")
        print("")
        print("")
        print("                          █████████   ███     ███   ██████")
        print("                          ███           ███ ███     ███  ███")
        print("                          █████████       ███       ██████")
        print("                          ███           ███ ███     ███")
        print("                          █████████   ███     ███   ███")
        print("")
        print("EYN-DOS Experimental (2022)")
        print("")

    if command_line==("credits"):
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

    if command_line==("cdate"):
        print("")
        os.system("python3 c-date.py")
        print("")

    if command_line==("read"):
        print("")
        txt_name=input("Enter the name of the file you want to read. (Including extension): ")
        print("")
        with open(txt_name) as f:
            contents = f.read()
            print(contents)
            f.close
        print("")
    
    if command_line==("find"):
        print("")
        file_find=input("What file do you want to find? (Including extension): ")
        print("")
        print(os.path.abspath(file_find))
        print("")

    if command_line==("write"):
        print("")
        os.system("python3 write.py")
        print("")

    if command_line==("del"):
        print("")
        del_file=input("What file do you want to delete? (Including extension): ")
        print("")
        if del_file==("C.py", 
        "A.py", 
        "B.py", 
        "D.py", 
        "E.py", 
        "LICENSE", 
        "launch.json", 
        "info.md"):
            print("")
            print("This is a critical system file. No action will be taken.")
            print("")
            break
        else:
            print("Deleting file...")
            os.remove(del_file)
            print("")
            print("File deleted.")
            print("")

    if command_line==("size"):
        print("")
        size_cl=input("What file do you want the size to? (Including extension): ")
        print("")
        print(os.path.getsize(size_cl)/1024)
        print(" | Kilobytes")
        print("")

    if command_line==("clear"):
        print("")
        os.system("cls")

    if command_line==("errorlist"):
        print("")
        print(" --A ERRORS--")
        print("")
        print("EYN_A1 = No floppy drive detected.")
        print(" | EYN_A1-NDI = No floppy diskette inserted.")
        print("EYN_A2 = Corrupted/unreadable floppy diskette.")
        print("EYN_A3 = Invalid diskette format/invalid diskette type.")
        print(' | Additional info = Only 3.5" floppy diskettes are supported.')
        print("")
        print(" --B ERRORS--")
        print("")
        print("All A Errors apply to the B drive.")
        print("")
        print(" --C ERRORS--")
        print("")
        print("EYN_C1 = Unable to boot EYN-DOS due to a C drive error.")
        print(" | EYN_C1-1 = Unable to read a critical system file (Possible cause of EYN_C1).")
        print("EYN_C2 = Unable to boot EYN-DOS due to a permission issue.")
        print("EYN_C3 = Feature not supported in EYN-DOS.")
        print("EYN_C3_FNI = Feature not (yet) included in EYN-DOS.")
        print("EYN_C4 = Invalid command or file name.")
        print("")
        print(" --D ERRORS--")
        print("")
        print("EYN_D1 = Recovery not created.")
        print(" | EYN_D2 = Recovery unable to be created.")
        print("  | EYN_D2-LNS = Recovery unable to be created due to low/nul storage.")
        print("")
        print("All C Errors apply to the D drive.")
        print("")
        print(" --E ERRORS--")
        print("")
        print("EYN_E1 = Unable to read the E drive due to an E drive error.")
        print(" | EYN_E1-NDI = No disc inserted.")
        print("EYN_E2 = Corrupted/unreadable disc.")
        print("EYN_E3 = Unable to read the E drive due to a permission issue.")
        print("EYN_E4 = No disc drive detected.")
        print("")
        print(" --ADDITIONAL ERRORS--")
        print("")
        print("EYN_AD1 = Unable to read the current date/time.")
        print(" | EYN_AD1-CM = Unable to read the current date/time due to CMOS battery error.")
        print("EYN_AD2 = Unable to read/run software.")
        print(" | EYN_AD2-NMD = Unable to read/run software due to no essential module detected.")
        print("")

    if command_line==("A"):
        print("")
        os.system("python3 A.py")
        print("")

    if command_line==("B"):
        print("")
        os.system("python3 B.py")
        print("")

    if command_line==("C"):
        print("")
        os.system("python3 C.py")
        print("")

    if command_line==("D"):
        print("")
        os.system("python3 D.py")
        print("")
    
    if command_line==("E"):
        print("")
        os.system("python3 E.py")
        print("")

    if command_line==("run"):
        print("")
        run_name=input("What file do you want to run? (extension included): ")
        print("")
        if run_name==("C.py"):
            print("")
            print("This is already running!")
            print("")
        else:
            os.system('py ' + run_name)
            print("")

    if command_line==("cd"):
        print("")
        print("(Type 'nul' to return to the EYN-DOS main terminal)")
        print("")
        cd_line=input("What directory do you want to go to?: ")
        print("")
        if cd_line==("nul"):
            print("Returning to the EYN-DOS main terminal...")
            print("")
        else:
            chdir(cd_line)

    if command_line==("cwd"):
        print("")
        cwd=os.getcwd()
        print(cwd)
        print("")

    if command_line==("ctime"):
        print("")
        os.system("python3 c-time.py")
        print("")

    if command_line==("md"):
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

    if command_line==("copy"):
        print("")
        cpy_line=input("Where is the file you want to copy?: ")
        print("")
        pst_line=input("Where do you want to paste the file?: ")
        print("")
        if cpy_line==("nul"):
            print("Returning to the EYN-DOS main terminal...")
            print("")
        else:
            print("Pasting...")
            print("")
            shutil.copyfile(cpy_line, pst_line)
            print("Pasted.")
            print("")

    if command_line==("echo"):
        print("")
        echo_line=input("What do you want to echo?: ")
        print("")
        print(echo_line)
        print("")

    if command_line==("colortest"):
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

    if command_line==("terry"):
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

    if command_line==("placeholder"):
        print("placeholder");

    # Feel free to add extra commands for yourself! Modding is encouraged. #

    # "Enjoy EYN-DOS!" - J.K Incorporated #
    