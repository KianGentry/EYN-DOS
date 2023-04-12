import os
import platform

ps=platform.system() # checks host os name

if ps==("Windows"): # if name is windows
    osrunner = "py" # use py in terminal
else: # if its smt else (bash)
    osrunner = "python3" # use python3 in terminal

os.system(osrunner + " writedir.py")

from commands import * # imports all definitions (commands) from commands.py

print(ps)

if ps==("Windows"): # if name is windows
    os.system("cls") # use windows clear command
else: # if its smt else (bash)
    os.system("clear") # use bash clear command

print("Copyright (c) 2023, J.K Incorporated, All Rights Reserved.") # copyright notice bc legality
print("Type 'help' for a list of commands.")
print()

while True: # basically just a loop of an input, and if the input matches the name of one of the commands, it executes it. the commands are all stored as functions in commands.py. pretty organised if you ask me.
    command_line=input(lbl+"/main/} "+wh)
    print(r+"")

    if command_line==("help"):
        help()

    elif command_line==("listdir"):
        listdir()

    elif command_line==("dir"):
        dir()

    elif command_line==("end"):
        end()

    elif command_line==("lgr"):
        lgr()
    
    elif command_line==("fdisk"):
        errfni()
    
    elif command_line==("win"):
        win() # no.

    elif command_line==("count"):
        count()

    elif command_line==("troll"):
        troll() # teehee

    elif command_line==("ver"):
        ver()

    elif command_line==("credits"):
        credits()

    elif command_line==("cdate"):
        cdate()

    elif command_line==("read"):
        read()
    
    elif command_line==("find"):
        find()

    elif command_line==("write"):
        write()

    elif command_line==("del"):
        del1()

    elif command_line==("size"):
        size()

    elif command_line==("clear"):
        clear()

    elif command_line==("run"):
        run()

    elif command_line==("cd"):
        cd()

    elif command_line==("cwd"):
        cwd()

    elif command_line==("ctime"):
        ctime()

    elif command_line==("md"):
        md()

    elif command_line==("copy"):
        copy()

    elif command_line==("echo"):
        echo()

    elif command_line==("colortest"):
        colortest()

    elif command_line==("terry"):
        terry() # rest in peace, legend

    elif command_line==("edit"):
        edit()

    elif command_line==("specs"):
        specs()

    elif command_line==("dirsize"):
        dirsize()

    elif command_line==("newver"):
        newver()

    elif command_line==("unzip"):
        unzip()

    elif command_line==("zip"):
        zip()

    elif command_line==("pyedit"):
        pyedit()

    elif command_line==("restart"):
        restart()

    elif command_line==("prevd"):
        prevdir()

    elif command_line==("prevf"):
        prevfiles()

    elif command_line==("noneyn"):
        noneyn()

    elif command_line==("rim"):
        rim()

    elif command_line==("ren"):
        ren()

    elif command_line==("eyndir"):
        eyndir()

    elif command_line==("pip"):
        pip()

    else: # if command-line input isnt one of the commands,
        print(Fore.LIGHTRED_EX+"Invalid command.") # print 'invalid command'
        print("")
