from commands import *

while True:
    command_line=input("/mini/} ")

    if command_line==("help"):
        help()

    elif command_line==("dir"):
        dir()

    elif command_line==("end"):
        end()

    elif command_line==("ver"):
        ver()

    elif command_line==("credits"):
        credits()

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

    else:
        print("")
        print("Invalid command.")
        print("")
