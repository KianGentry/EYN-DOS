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
    command_line=input("C:\> ")

    if command_line=="help":
        print("")
        print("help = Prints commands currently usable, ")
        print("listdir = Prints a list of available directories, ")
        print("dir = Prints a list of all available files in the current directory, ")
        print("run (file) = Executes the file entered, ")
        print("end = Closes and resets the EYN-DOS terminal, ")
        print("browser = Takes you to the EYN-DOS browser terminal, ")
        print("ver = Prints the EYN-DOS version that is running, ")
        print("credits = Prints a list of all the people who worked on EYN-DOS, ")
        print("cd (File/Folder location) = Takes you to the directory entered, ")
        print("cdate = Prints the current date and time, ")
        print("read = Prints the contents of the file entered, ")
        print("find = Prints the directory path of the file entered, ")
        print("write = Writes 1 line of custom text to the file entered (creates new file), ")
        print("del = Deletes any newly writtten file entered, ")
        print("size = Prints the size of the file entered, ")
        print("clear = Clears the screen of all previously printed lines, ")
        print("errorlist = Prints all error codes and their meanings.")
        print("A: = Takes you to the A drive (Floppy disk drive 1)")
        print("B: = Takes you to the B drive (Floppy disk drive 2)")
        print("C: = Takes you to the C drive (Hard drive)")
        print("D: = Takes you to the D drive (Recovery drive)")
        print("E: = Takes you to the E drive (Compact Disc drive)")
        print("")
        print("Misc:")
        print("")
        print(" insert(1-9).py = You can add a custom Python file into the EYN-DOS folder and execute it by typing 'run insert(Number in the filename (1-9)).py, ")
        print("")

    if command_line=="listdir":
        print("")
        print("DIR1 - ", float(size)/1024, " Kilobytes")
        print("")
        print("DIR2 - ", "0.0", " Kilobytes")
        print("")
        print("DIR3 - ", "0.0", " Kilobytes")
        print("")

    if command_line=="dir":
        print("")
        print(filesys)
        print("")
        print(get_dir_size('data/src')) 
        print(" | Kilobytes")
        print("")
        
    if command_line=="run eyndos.py":
        print("")
        print("This is already running!")
        print("")
        
    if command_line=="end":
        print("")
        exit()
        
    if command_line=="run calculator.py":
        print("")
        os.system('python3 calculator.py')
        print("")

    if command_line==("run minesweeper.py"):
        print("")
        os.system('python3 minesweeper.py')
        print("")

    if command_line==("run notebook.py"):
        print("")
        os.system("python3 notebook.py")
        print("")
    
    if command_line==("lgr"):
        print("")
        print("Hey, that's a good YouTube channel!")
        print("")
    
    if command_line==("fdisk"):
        print("")
        print("ERROR EYN_C3-FNI")
        print("")
    
    if command_line==("win"):
        print("")
        print("No.")
        print("")
    
    if command_line==("run solitaire.py"):
        "Credit to 'shomikj' on GitHub for this code!"
        print("")
        os.system('python3 solitaire.py')
        print("")

    if command_line==("run weight_converter.py"):
        print("")
        os.system("python3 weight_converter.py")
        print("")

    if command_line==("run gui_calculator.py"):
        print("")
        os.system('python3 gui_calculator.py')
        print("")
    
    if command_line==("run clock.py"):
        print("")
        os.system('python3 clock.py')
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

    if command_line==("run insert1.py"):
        print("")
        os.system('python3 insert1.py')
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

    if command_line==("run oregon_trail.py"):
        print("")
        os.system('python3 oregon_trail.py')
        print("")

    if command_line==("run snake.py"):
        print("")
        os.system('python3 snake.py')
        print("")

    if command_line==("run pong.py"):
        print("")
        os.system('python3 pong.py')
        print("")

    if command_line==("run tetris.py"):
        print("")
        print("Use A to go left, D to go right and spacebar to rotate.")
        os.system('python3 tetris.py')
        print("")

    if command_line==('run invaders.py'):
        print("")
        print("Use the left arrow to go left, the right arrow to go right, and spacebar to shoot.")
        os.system('python3 invaders.py')
        print("")

    if command_line==("run paintbrush.py"):
        print("")
        os.system('python3 paintbrush.py')
        print("")

    if command_line==("!devdebug1!"):
        print("")
        dev_ver=input("THIS OPTION IS FOR DEVELOPERS AND TESTERS ONLY. IF YOU ARE NOT A DEVELOPER OR TESTER, YOU WILL BE REPORTED TO A HR. CONTINUE? (y/n) ")
        print("")

        if dev_ver==("n"):
            print("")
            print("Command disbanded")
            print("")
        
        if dev_ver==("y"):
            print("")
            dev_ver1=input("Enter your provided username: ")

            if dev_ver1==("kg2"):
                print("")
                print("Welcome back, Kian.")
                print("")

                dev_ver2=input("Enter your provided password: ")

                if dev_ver2==("celerysticksfiddlebottom20"):
                    print("")
                    print("Welcome to the EYN-DOS development terminal, Kian!")
                    print("")
                
                if dev_ver2!=("celerysticksfiddlebottom20"):
                    exit()
            
            if dev_ver1==("cj9"):
                print("")
                print("Welcome back, Cayden.")
                print("")

                dev_ver3=input("Enter your provided password: ")

                if dev_ver3==("carrotfarmmule90"):
                    print("")
                    print("Welcome to the EYN=DOS development terminal, Cayden!")
                    print("")
                
                if dev_ver3!=("carrotfarmmule90"):
                    exit()
            
            if dev_ver1==("ig1"):
                print("")
                print("Welcome back, Ian.")
                print("")

                dev_ver4=input("Enter your provided password: ")

                if dev_ver4==("isaacboatorange30"):
                    print("")
                    print("Welcome to the EYN-DOS development terminal, Ian!")
                    print("")

                if dev_ver4!=("isaacboatorange30"):
                    exit()

            if dev_ver1==(""):
                exit()

            while True:
                command_line1=input("C:\DEVDEBUG1\> ")

                if command_line1==("debug"):
                    print("")
                    print("Coming soon...")
                    print("")
                
                if command_line1==("end"):
                    exit()
                
                if command_line1==("eyn_os"):
                    print("")
                    print("Welcome to...")
                    print("                        (Built on EYN-DOS)")
                    print("                    ██████████████████████████")
                    print("                    ███░█████░██░░░██░██░░░█░██")
                    print("██       ██      ██ ██░░█░░░░░░░███░░░██░░░█░░██")
                    print("     ██      ██     ██░░█████░░░░█░░░░█░█░░█░░██")
                    print("██       ██      ██ ██░░█░░░░░░░░█░░░░█░░█░█░░██")
                    print("     ██      ██     ███░█████░░░░█░░░░█░░░██░░██")
                    print("██       ██      ██ ████████████████████████████")
                    print("     ██      ██     ███░░░█████░░░░░░█████░░░░██")
                    print("         ██      ██ ██░░░█░░░░░█░░░░█░░░░░░░░░██")
                    print("     ██      ██     ██░░░█░░░░░█░░░░░█████░░░░██")
                    print("                 ██ ██░░░█░░░░░█░░░░░░░░░░█░░░██")
                    print("             ██     ███░░░█████░░░░░░█████░░░██")
                    print("                    ██████████████████████████")
                    print("                     A nostalgic, yet modern")
                    print("                      O.S...")
                    print("")
                    os.system('python3 eyn_os_0_1.py')
                    print("")
    
                if command_line1==("calculate"):
                    print("")
                    gc1=input("GUI based or CLI based? (g/c) ")

                    if gc1==("g"):
                        print("")
                        os.system('python3 gui_calculator.py')
                        print("")
                    
                    if gc1==("c"):
                        print("")
                        os.system('python3 calculator.py')
                        print("")
                
                if command_line1==("time"):
                    print("")
                    os.system('python3 clock.py')
                    print("")
                
                if command_line1==("coder"):
                    print("")
                    print("Coming soon...")
                    print("")

                if command_line1==("count"):
                    print("")
                    countperm=input("WARNING: counter.py WILL LOCK YOUR PC UNTIL RESTARTED PHYSICALLY. CONTINUE? (y/n) ")

                    if countperm==("n"):
                        print("")
                        print("Command disbanded")
                        print("")

                    if countperm==("y"):
                        print("")
                        os.system('python3 counter.py')
                        print("")

                if command_line1==("eynos01 files"):
                    print("")
                    print(" - - - - EYNOS1 - - - - ")
                    print("")
                    print("   eyn_os_0_1.py - 3kb")
                    print("   user.folder - 0kb")
                    print("")
                    print(" TOTAL: 3kb")
                    print("")
                
                if command_line1==("dir1 files"):
                    print("")
                    print(" - - - - DIR1 - - - - ")
                    print("")
                    print("   eyndos.py - 29kb")
                    print("   calculator.py - 1kb")
                    print("   minesweeper.py - 9kb")
                    print("   notebook.py - 1kb")
                    print("   solitaire.py - 12kb")
                    print("   test1.py - 1kb")
                    print("   weight_converter.py - 1kb")
                    print("   gui_calculator.py - 4kb")
                    print("   clock.py - 1kb")
                    print("   oregon_trail.py - 8kb")
                    print("   snake.py - 4kb")
                    print("   pong.py - 3kb")
                    print("   tetris.py - 7kb")
                    print("   paintbrush.py - 3kb")
                    print("   test3.py - 15kb")
                    print("   mouse_detection.py - 1kb")
                    print("")
                    print(" TOTAL: 100kb - LEFT: 900kb - 16 Files")
                    print("")

                if command_line1==("return"):
                    print("")
                    print("Returning to main terminal...")
                    print("")
                    break

                if command_line1==("help"):
                    print("")
                    print("help = Prints a list of available commands, end = Ends the current EYN-DOS session, eyn_os = Runs the latest version of EYN-OS, calculate = Runs a calculator program, time = Runs a clock program, count = Counts infinitely (locks current EYN-DOS session), (directory) files = Prints files and information about the entered directory, return = Returns you to the main EYN-DOS terminal. Attempting to type an unknown command results in a blank response.")
                    print("")

                if command_line1==("run mouse_detection.py"):
                    print("")
                    os.system('python3 mouse_detection.py')
                    print("")

    if command_line==("ver"):
        print("")
        print("█████████   ███     ███   ███      ███            ██████       ██████      ██████")
        print("███           ███ ███     ██████   ███            ███   ███  ███    ███  ███")
        print("█████████       ███       ███  ███ ███   ██████   ███   ███  ███    ███    ██████")
        print("███             ███       ███    █████            ███   ███  ███    ███        ███")
        print("█████████       ███       ███      ███            ██████       ██████     ██████")
        print("")
        print("                             ████         ████████")
        print("                          ███ ███              ███")
        print("                              ███             ███")
        print("                              ███           ███")
        print("                              ███          ███")
        print("                           █████████  ██   ███")
        print("")
        print("EYN-DOS 1.7 (2022)")
        print("")

    if command_line==("credits"):
        print("")
        print("The EYN-DOS Team:")
        print("")
        print("    Primary coder: Kian Gentry (Founder and CEO of J.K Incorporated)")
        print("    Secondary coder: Ian Greeves (Musician and Lead Artist of J.K Incorporated.")
        print("    Logo designer: Kamil M.")
        print("    Staff commander: Kian Gentry")
        print("    Everyone involved: Kian Gentry, Ian Greeves, Kamil M. and other J.K Incorporated employees.")
        print("")
        print("-----------------------------------------------------------------------------------------")
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

    if command_line==("run insert2.py"):
        print("")
        os.system("python3 insert2.py")
        print("")

    if command_line==("run insert3.py"):
        print("")
        os.system("python3 insert3.py")
        print("")

    if command_line==("run insert4.py"):
        print("")
        os.system("python3 insert4.py")
        print("")
    
    if command_line==("run insert5.py"):
        print("")
        os.system("python3 insert5.py")
        print("")
    
    if command_line==("run insert6.py"):
        print("")
        os.system("python3 insert6.py")
        print("")
    
    if command_line==("run insert7.py"):
        print("")
        os.system("python3 insert7.py")
        print("")
    
    if command_line==("run insert8.py"):
        print("")
        os.system("python3 insert8.py")
        print("")
    
    if command_line==("run insert9.py"):
        print("")
        os.system("python3 insert9.py")
        print("")

    if command_line==("browser"):
        print("")
        os.system("python3 browser.py")
        print("")

    if command_line==("run cli_notebook.py"):
        print("")
        print("Loading the EYN-DOS notebook terminal...")
        print("")
        os.system('python3 cli_notebook.py')
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
        wri_name=input("What do you want to call your new file? (Extension included): ")
        print("")
        print("Type what you want your file to contain! (1 line): ")
        print("")
        wri_con=input("> ")
        print("")
        print("Saving...")
        print("")
        with open((wri_name), 'w') as f:
            f.write("")
            f.write(wri_con)
            f.write("")
        print("Saved.")
        print("")

    if command_line==("del"):
        print("")
        del_file=input("What file do you want to delete? (Including extension): ")
        print("")
        if del_file==(wri_name):
            print("")
            print("Deleting file...")
            os.remove(wri_name)
            print("")
            print("File deleted.")
            print("")
        else:
            print("")
            print("The file entered is invalid.")
            print("")
            print("No action will be taken.")
            print("")

    if command_line==("size"):
        print("")
        size_cl=input("What file do you want the size to? (Including extension): ")
        print("")
        print(os.path.getsize(size_cl)/1024)
        print(" | Kilobytes")
        print("")

    if command_line==("cd DIR2"):
        print("")
        while True: 
            dir2_line=input("C:\DIR2\> ")

            if dir2_line==("cd"):
                print("")
                print("Returning to the EYN-DOS main terminal...")
                print("")
                break
            
            if dir2_line==("dir"):
                print("")
                print("No files found!")
                print("")
            
            if dir2_line=="listdir":
                print("")
                print("DIR1 - ", float(size)/1024, " Kilobytes")
                print("")
                print("DIR2 - ", "0.0", " Kilobytes")
                print("")
                print("DIR3 - ", "0.0", " Kilobytes")
                print("")
            
            if dir2_line==("write"):
                print("")
                print("Unsupported command for DIR2 in EYN-DOS 1.62.")
                print("")
            
            if dir2_line==("del"):
                print("")
                print("No files to delete.")
                print("")
            
            if dir2_line==("read"):
                print("")
                print("No files to read.")
                print("")

    if command_line==("cd DIR3"):
        print("")
        while True: 
            dir3_line=input("C:\DIR3\>")

            if dir3_line==("cd"):
                print("")
                print("Returning to the EYN-DOS main terminal...")
                print("")
                break
            
            if dir3_line==("dir"):
                print("")
                print("No files found!")
                print("")
            
            if dir3_line=="listdir":
                print("")
                print("DIR1 - ", float(size)/1024, " Kilobytes")
                print("")
                print("DIR2 - ", "0.0", " Kilobytes")
                print("")
                print("DIR3 - ", "0.0", " Kilobytes")
                print("")
            
            if dir3_line==("write"):
                print("")
                print("Unsupported command for DIR3 in EYN-DOS 1.62.")
                print("")
            
            if dir3_line==("del"):
                print("")
                print("No files to delete.")
                print("")
            
            if dir3_line==("read"):
                print("")
                print("No files to read.")
                print("")

    if command_line==("clear"):
        print("")
        os.system("clear")

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

    if command_line==("A:"):
        print("")
        os.system("python3 A.py")
        print("")

    if command_line==("B:"):
        print("")
        os.system("python3 B.py")
        print("")

    if command_line==("D:"):
        print("")
        os.system("python3 D.py")
        print("")
    
    if command_line==("E:"):
        print("")
        os.system("python3 E.py")
        print("")
