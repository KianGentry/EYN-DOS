import os
from os import listdir
from os.path import isfile, join

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
    command_lineB=input("B:\> ")

    if command_lineB==("A:"):
        print("")
        os.system("python3 A.py")
        print("")
    
    if command_lineB==("C:"):
        print("")
        os.system("python3 C.py")
        print("")

    if command_lineB==("D:"):
        print("")
        os.system("python3 D.py")
        print("")
    
    if command_lineB==("E:"):
        print("")
        os.system("python3 E.py")
        print("")

    if command_lineB==("dir"):
        print("")
        print("ERROR EYN_A1")
        print("")

    if command_lineB==("listdir"):
        print("")
        print("ERROR EYN_A1")
        print("")

    if command_lineB==("end"):
        print("")
        exit()
