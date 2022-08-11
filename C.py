from commands import *

while True:
    command_line=input("C/} ")

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
        win()

    elif command_line==("count"):
        count()

    elif command_line==("troll"):
        troll()

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

    elif command_line==("errorlist"):
        errorlist()

    elif "A" in command_line:
        a()

    elif "B" in command_line:
        b()

    elif "C" in command_line:
        c()

    elif "D" in command_line:
        d()
    
    elif "E" in command_line:
        e()

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
        terry()

    else:
        print("")
        print("Invalid command.")
        print("")
