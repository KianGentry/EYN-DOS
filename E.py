import os
from os import listdir
from os.path import isfile, join

# File system

dir_path = os.path.dirname(os.path.realpath(__file__))

filesys = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]

def get_dir_size(path=dir_path):
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

while True:
    command_lineE=input("E:\> ")

    if command_lineE==("A:"):
        print("")
        os.system("python3 A.py")
        print("")

    if command_lineE==("B:"):
        print("")
        os.system("python3 B.py")
        print("")
    
    if command_lineE==("C:"):
        print("")
        os.system("python3 C.py")
        print("")
    
    if command_lineE==("D:"):
        print("")
        os.system("python3 D.py")
        print("")

    if command_lineE==("dir"):
        print("")
        print("ERROR EYN_E2")
        print("")

    if command_lineE==("listdir"):
        print("")
        print("ERROR EYN_E2")
        print("")

    if command_lineE==("end"):
        print("")
        exit()
