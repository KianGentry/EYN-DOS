from commands import * # imports all definitions (commands) from commands.py

os.system("cls") # clears previous terminal text

print("Copyright (c) 2022, J.K Incorporated") # copyright notice bc legality
print("All rights reserved.") # what does this mean again, someone tell me
print("")

while True: # basically just a loop of an input, and if the input matches the name of one of the commands, it executes it. the commands are all stored as functions in commands.py. pretty organised if you ask me.
    command_line=input("/main/} ")

    if command_line==("help"):
        help()

    elif command_line==("listdir"):
        listdir()

    elif command_line==("dir"):
        dir()

    elif command_line==("end"):
        end()

    elif command_line==("ver"):
        ver()

    elif command_line==("credits"):
        credits()

    elif command_line==("cdat"):
        cdat()

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

    elif command_line==("md"):
        md()

    elif command_line==("copy"):
        copy()

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

    else: # if command-line input isnt one of the commands,
        print("")
        print("Invalid command.") # print 'invalid command'
        print("")
