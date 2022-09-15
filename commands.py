# getting module stuff

from colorama import Fore
import shutil
import os
from os import chdir, listdir, mkdir
from os.path import isfile, join

# boring file system stuff

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

# the actual good part

def help():
    print("")
    print("help = Prints commands currently usable, ")
    print("dir = Prints a list of all available files in the current directory, ")
    print("run = Executes the file entered, ")
    print("end = Closes the EYN-DOS terminal, ")
    print("ver = Prints the EYN-DOS version that is running, ")
    print("credits = Prints a list of all the people who worked on EYN-DOS, ")
    print("cd = Takes you to the directory entered, ")
    print("read = Prints the contents of the file entered, ")
    print("find = Prints the directory path of the file entered, ")
    print("write = Writes custom text to the file entered (creates new file), ")
    print("del = Deletes any newly writtten file entered, ")
    print("size = Prints the size of the file entered, ")
    print("clear = Clears the screen of all previously printed lines, ")
    print("md = Makes a directory with the name entered.")
    print("copy = Copy and pastes the file selected in the path entered.")
    print("edit = Appends the file entered.")
    print("calculate = 'New command! Old code!' A simple command-line calculator.")
    print("")

def dir():
    print("")
    print(filesys)
    print("")
    print(get_dir_size(dir_path)) 
    print(" | Kilobytes")
    print("")

def end():
    exit()

def ver():
    print("")
    print("█████████   ███     ███   ███      ███            ██████       ██████      ██████")
    print("███           ███ ███     ██████   ███            ███   ███  ███    ███  ███")
    print("█████████       ███       ███  ███ ███   ██████   ███   ███  ███    ███    ██████")
    print("███             ███       ███    █████            ███   ███  ███    ███        ███")
    print("█████████       ███       ███      ███            ██████       ██████     ██████")
    print("")
    print("EYN-DOS Minimal (2022)")
    print("")

def credits():
    print("")
    print("The EYN-DOS Team:")
    print("")
    print("    Primary coder: Kian Gentry (Founder and CEO of J.K Incorporated.)")
    print("    Secondary coder: Ian Greeves (Musician and I.T Assistant of J.K Incorporated.)")
    print("    Logo designer: Kamil Makuch (Primary Artist of J.K Incorporated.)")
    print("    Staff commander: Kian Gentry (Founder and CEO of J.K Incorporated.)")
    print("    Everyone involved: Kian Gentry, Ian Greeves, Kamil Makuch and other J.K Incorporated employees.")
    print("")
    print("    Honorable mentions:")
    print("")
    print("         Robin Andrews: Coder of the 'Snake' game included with EYN-DOS. (Unincluded in EYN-DOS Minimal)")
    print("         shomikj: Coder of the command line version of 'Solitaire' for EYN-DOS. (Unincluded in EYN-DOS Minimal)")
    print("         Cayden Jackson: Supporter.")
    print("         Kamil Makuch: Supporter and artist.")
    print("         Github, StackOverflow & GeeksForGeeks: Saver of countless hours of research.")
    print("         You: For using EYN-DOS.")
    print("         Linux: Just awesome.")
    print("")
    print("         Thank you for using EYN-DOS!")
    print("")

def read():
    print("")
    txt_name=input("Enter the name of the file you want to read. (Including extension): ")
    print("")
    with open(txt_name) as f:
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
    fn=input("What do you want to call your new file? (Extension included): ")
    print("")
    print("Type what you want your file to contain! (Type nul0 to exit): ")
    print("")

    while True:
        text=input("> ")

        if text.lower() == "nul0":
            break
    
        with open(fn, 'a') as f:
          f.write(text + "\n")

def del1():
    print("")
    print("(Type 'nul0' to abort the command.)")
    print("")
    del_file=input("What file do you want to delete? (Including extension): ")
    print("")

    if del_file==("nul0"):
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
    print("(Type 'nul' to return to the EYN-DOS main terminal)")
    print("")
    cd_line=input("What sub-directory do you want to go to?: ")
    print("")
    if cd_line==("nul"):
        print("Returning to the EYN-DOS main terminal...")
        print("")
    else:
        chdir(cd_line)

def cwd():
    print("")
    cwd=os.getcwd()
    print(cwd)
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

def edit():
    ef=input("What file do you want to edit? (Including extension): ")
    print("")
    print("Type what you want to append to your file (Type nul0 to exit): ")
    print("")

    while True:
        efw=input("> ")
    
        if efw.lower() == "nul0":
            break
    
        with open(ef, "a") as f:
            f.write(efw)

def calculate():
    print("+ = Addition")
    print("- = Subtraction")
    print("x = Multiplication")
    print("/ = Division")
    print("^ = To the power of")

    Number1=input("Number1: ")
    Math_Symbol=input("Math Symbol: ")
    Number2=input("Number2: ")

    if Math_Symbol==("+"):
      sam=float(Number1) + float(Number2)
      print("Addition Answer: "+str(sam))

    if Math_Symbol==("-"):
       sum=float(Number1) - float(Number2)
       print("Subtraction Answer: "+str(sum))

    if Math_Symbol==("x"):
       som=float(Number1) * float(Number2)
       print("Multiplication Answer: "+str(som))

    if Math_Symbol==("/"):
       sim=float(Number1) / float(Number2)
       print("Division Answer: "+str(sim))

    if Math_Symbol==("^"):
       sem=float(Number1) ** float(Number2)
       print ("N1 to the power of N2 Answer: "+str(sem))
