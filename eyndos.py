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
    return total

print("Starting EYN-DOS...")
print("")

print("                  ████████████████ ")
print("               ███░░░░░░░░░░░░░░░░███")
print("            ████░░░░░░░░░░░░░░░░░░░░████      ")
print("         ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░███")
print("        ██░░░██████████████████████████░░░██")
print("       █░░░░░░░░░░░░░█████░░░░░░░░░████░░░░░█")
print("      █░░░░░░░░░░░░░░░███░░░░░░░░█████░░░░░░░█")
print("     █░░░░░░░░░░░░░░░░███░░░░░░░█████░░░░░░░░░█")
print("     █░░░░░░░░░░░░░░░░████░░░███████░░░░░░░░░░█")
print("     █░░░░░░░░░░░░░░░░████████████░░░░░░░░░░░░█")
print("     █░░░░░░░░░░░░░░░░░████████░░░░░░░░░░░░░░░█")
print("     █░░░░░░███░░░░░░░░████████░░░░░░░░░░░░░░░█")
print("     █░░░░░███████████████████████░░░░░░░░░░░░█")
print("     █░░░░░░██████████████░░░███████░░░░░░░░░░█")
print("     █░░░░░░████████████░░░░░░░░█████░░░░░░░░░█")
print("      █░░░░░░██████████░░░░░░░░░█████░░░░░░░░█")
print("       █░░░░░░████████░░░░░░░░░░░█████░░░░░░█")
print("        ██░░░░░██████░░░░░░░░░░░░░████░░░░██")
print("         ███░░░I N C O R P O R A T E D░░███")
print("            ████░░░░░░░░░░░░░░░░░░░░████")
print("               ███░░░░░░░░░░░░░░░░███")
print("                  ████████████████")
print("")
print("             J.K Incorporated (1983 - 2022)")
print("")
input("Press the 'Enter' key to continue.")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")

print("")
print("1. Q W E R T Y U I O P   2.  A B C D E F G H I J")
print("    A S D F G H J K L         K L M N O P Q R S")
print("      Z X C V B N M             T U V W X Y Z")
print("")

keyboard_select=input("Select your keyboard layout. (1/2) ")

if keyboard_select==("1"):
    print("")
    print("Keyboard layout 1 applied.")
    print("")

if keyboard_select==("2"):
    print("")
    print("Keyboard layout 2 applied.")
    print("")

if keyboard_select==(""):
    print("")
    print("Host system default applied.")
    print("")

print("Loading...")
print("")
command_line=input("Press the 'Enter' key to enter EYN-DOS.")

print("")
print("█████████   ███     ███   ███      ███            ██████       ██████      ██████")
print("███           ███ ███     ██████   ███            ███   ███  ███    ███  ███")
print("█████████       ███       ███  ███ ███   ██████   ███   ███  ███    ███    ██████")
print("███             ███       ███    █████            ███   ███  ███    ███        ███")
print("█████████       ███       ███      ███            ██████       ██████     ██████")
print("")
print("Type 'help' for a list of commands.")
print("")

while True:
    command_line=input("C:\DIR1\eyndos_1_51\eyndos.py> ")

    if command_line=="help":
        print("")
        print("help = Prints commands currently usable, ")
        print("dir = Prints a list of available directories, ")
        print("files = Prints a list of all available files, ")
        print("run (file) = Executes the file entered, ")
        print("end = Closes and resets the EYN-DOS terminal, ")
        print("install = Takes you to the EYN-DOS install terminal, ")
        print("browser = Takes you to the EYN-DOS browser terminal, ")
        print("B: = Takes you to the B partition, ")
        print("C: = Takes you to the C partition, ")
        print("ver = Prints the EYN-DOS version that is running.")
        print("credits = Prints a list of all the people who worked on EYN-DOS, ")
        print("cd (File/Folder location) = Takes you to the directory entered, ")
        print("")
        print("Misc:")
        print("")
        print(" insert(1-9).py = You can add a custom Python file into the EYN-DOS folder and execute it by typing 'run insert(Number in the filename (1-9)).py, ")
        print("")

    if command_line=="dir":
        print("")
        print("DIR1 (Max Storage: 10mb)")
        print("- - - - - - - - - - - - - - - - - -")
        print("EYNOS01 (Max Storage: 10mb)")
        print("")
    
    if command_line=="files":
        print("")
        print(filesys)
        print("")
        print(get_dir_size('data/src')) 
        print(" | Bytes")
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
        os.system('py calculator.py')
        print("")

    if command_line==("run minesweeper.py"):
        print("")
        os.system('py minesweeper.py')
        print("")

    if command_line==("run notebook.py"):
        print("")
        os.system("py notebook.py")
        print("")
    
    if command_line==("lgr"):
        print("")
        print("Hey, that's a good YouTube channel!")
        print("")
    
    if command_line==("fdisk"):
        print("")
        print("The disk is already formatted. Command disbanded.")
        print("")
    
    if command_line==("win"):
        print("")
        print("No.")
        print("")
    
    if command_line==("run solitaire.py"):
        "Credit to 'shomikj' on GitHub for this code!"
        print("")
        os.system('py solitaire.py')
        print("")

    if command_line==("run weight_converter.py"):
        print("")
        os.system("py weight_converter.py")
        print("")

    if command_line==("run gui_calculator.py"):
        print("")
        os.system('py gui_calculator.py')
        print("")
    
    if command_line==("run clock.py"):
        print("")
        os.system('py clock.py')
        print("")
    
    if command_line==("count"):
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
    
    if command_line==("setup"):
        print("")
        print("Coming soon... In the meantime, try playing some games bundled with EYN-DOS.")
        print("")

    if command_line==("create dir"):
        print("")
        print("Coming soon...")
        print("")

    if command_line==("run insert.py"):
        print("")
        os.system('py insert.py')
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
        os.system('py oregon_trail.py')
        print("")

    if command_line==("run snake.py"):
        print("")
        os.system('py snake.py')
        print("")

    if command_line==("run pong.py"):
        print("")
        os.system('py pong.py')
        print("")

    if command_line==("run tetris.py"):
        print("")
        print("Use A to go left, D to go right and spacebar to rotate.")
        os.system('py tetris.py')
        print("")

    if command_line==('run invaders.py'):
        print("")
        print("Use the left arrow to go left, the right arrow to go right, and spacebar to shoot.")
        os.system('py invaders.py')
        print("")

    if command_line==("run paintbrush.py"):
        print("")
        os.system('py paintbrush.py')
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
                command_line1=input("A:\DIR1\eyndos_1_5\eyndos.py\devdebug_1>  ")

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
                    os.system('py eyn_os_0_1.py')
                    print("")
    
                if command_line1==("calculate"):
                    print("")
                    gc1=input("GUI based or CLI based? (g/c) ")

                    if gc1==("g"):
                        print("")
                        os.system('py gui_calculator.py')
                        print("")
                    
                    if gc1==("c"):
                        print("")
                        os.system('py calculator.py')
                        print("")
                
                if command_line1==("time"):
                    print("")
                    os.system('py clock.py')
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
                        os.system('py counter.py')
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
                    os.system('py mouse_detection.py')
                    print("")

    if command_line==("B:", "b:"):
        print("")
        while True:
            command_line2=input("B:\> ")

            if command_line2==("C:" or "c:"):
                print("")
                while True:
                    command_line5=("C:\>")

                    if command_line5==("return"):
                        print("")
                        print("Returning to the main EYN-DOS terminal...")
                        print("")
            
            if command_line2==("return"):
                print("")
                print("Returning to the main EYN-DOS terminal...")
                print("")

    if command_line==("A:", "a:"):
        print("")
        while True:
            command_line3=input("A:\> ")

            if command_line3==("C:" or "c:"):
                print("")
                while True:
                    command_line4=("C:\>")

                    if command_line4==("return"):
                        print("")
                        print("Returning to the main EYN-DOS terminal...")
                        print("")
            
            if command_line3==("return"):
                print("")
                print("Returning to the main EYN-DOS terminal...")
                print("")

    if command_line==("ver"):
        print("")
        print("█████████   ███     ███   ███      ███            ██████       ██████      ██████")
        print("███           ███ ███     ██████   ███            ███   ███  ███    ███  ███")
        print("█████████       ███       ███  ███ ███   ██████   ███   ███  ███    ███    ██████")
        print("███             ███       ███    █████            ███   ███  ███    ███        ███")
        print("█████████       ███       ███      ███            ██████       ██████     ██████")
        print("")
        print("                                  ████         ██████")
        print("                               ███ ███        ███     ")
        print("                                   ███        ███████  ")
        print("                                   ███        ███  ███")
        print("                                   ███        ███  ███")
        print("                                ████████  ██   ██████ ")
        print("")
        print("EYN-DOS 1.6 (Windows) (2022)")
        print("")

    if command_line==("credits"):
        print("")
        print("  ████████   ████████    ████████    ████████    ██████████  ██████████    ██████")
        print("██           ██      ██  ██          ██      ██      ██          ██      ██")
        print("██           ██      ██  ██          ██      ██      ██          ██        ███")
        print("██           ████████    ████████    ██      ██      ██          ██           ███")
        print("██           ██ ███      ██          ██      ██      ██          ██       █████")
        print("██           ██   ███    ██          ██      ██      ██          ██      ")
        print("  ████████   ██     ██   ████████    ████████    ██████████      ██      ")
        print("")
        print("The Team:")
        print("")
        print("    Primary coder: Kian Gentry (Founder and CEO of J.K Incorporated)")
        print("")
        print("    Secondary coder: Ian Greeves (Musician and Lead Artist of J.K Incorporated.")
        print("")
        print("    EYN-OS Lead Coder: Kian Gentry")
        print("")
        print("    Box art & Logo design: Kamil M.")
        print("")
        print("    Staff commander: Kian Gentry")
        print("")
        print("    Everyone involved: Kian Gentry, Ian Greeves and other J.K Incorporated employees.")
        print("")
        print("-----------------------------------------------------------------------------------------")
        print("")
        print("    Honerable mentions:")
        print("")
        print("         Robin Andrews: Coder of the 'Snake' game included with EYN-DOS.")
        print("")
        print("         shomikj: Coder of the command line version of 'Solitaire' for EYN-DOS.")
        print("")
        print("         Cayden Jackson: Supporter.")
        print("")
        print("         Kamil M: Supporter & artist.")
        print("")
        print("         Github & StackOverflow: Saver of countless hours of research.")
        print("")
        print("         Microsoft: Without them, this project wouldn't be possible.")
        print("")
        print("         You: For using EYN-DOS.")
        print("")
        print("         You: For being the very best you can be.")
        print("")
        print("         You: For being one of the best people the EYN-DOS team knowns.")
        print("")
        print("")
        print("         Thank you for using EYN-DOS!")
        print("")

    if command_line==("run insert2.py"):
        print("")
        os.system("py insert2.py")
        print("")

    if command_line==("run insert3.py"):
        print("")
        os.system("py insert3.py")
        print("")

    if command_line==("run insert4.py"):
        print("")
        os.system("py insert4.py")
        print("")
    
    if command_line==("run insert5.py"):
        print("")
        os.system("py insert5.py")
        print("")
    
    if command_line==("run insert6.py"):
        print("")
        os.system("py insert6.py")
        print("")
    
    if command_line==("run insert7.py"):
        print("")
        os.system("py insert7.py")
        print("")
    
    if command_line==("run insert8.py"):
        print("")
        os.system("py insert8.py")
        print("")
    
    if command_line==("run insert9.py"):
        print("")
        os.system("py insert9.py")
        print("")

    if command_line==("cd EYNOS01"):
        print("")
        print("This directory is used exclusively for the unreleased operating system, EYN-OS 0.1")
        print("")
        while True:
            eynos_cdcl=input("C:\EYNOS01> ")

            if eynos_cdcl==("dir"):
                print("")
                print(" EYNOS01 - 3kb/10mb")
                print("--------------------")
                print(" DIR1 - 219kb/10mb")
                print("")
            
            if eynos_cdcl==("files"):
                print("")
                print(" EYNOS01 - 1 FILE, 1 FOLDER: ")
                print("")
                print(" eyn_os_0_1.py - 3kb")
                print(" user.fld - 0kb")
                print("")
                print("TOTALS: 3kb/10mb - 2 DISPLAY FILES")
            
            if eynos_cdcl==("return"):
                print("")
                print("Returning to the main EYN-DOS terminal...")
                print("")
                break

    if command_line==("browser"):
        print("")
        os.system("py browser.py")
        print("")

    if command_line==("run cli_notebook.py"):
        print("")
        print("Loading the EYN-DOS notebook terminal...")
        print("")
        os.system('py cli_notebook.py')
        print("")

    if command_line==("cdate"):
        print("")
        os.system("py c-date.py")
        print("")

    if command_line==("read"):
        print("")
        txt_name=input("Enter the name of the file you want to read. (Including extension): ")
        print("")
        with open(txt_name) as f:
            contents = f.read()
            print(contents)
            f.close
    
    if command_line==("find"):
        print("")
        file_find=input("What file do you want to find? (Including extension): ")
        print("")
        print(os.path.abspath(file_find))
        print("")

    if command_line==("keytest"):
        if keyboard_select==("1"):
            print("")
            os.system("py keytest-q.py")
            print("")

        if keyboard_select==("2"):
            print("")
            os.system("py keytest-a.py")
            print("")
        
        if keyboard_select==(""):
            print("")
            os.system("py keytest-q.py")
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
            f.write(wri_con)
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
            print("This is a file bundled with EYN-DOS (Critical system file or included software).")
            print("")
            print("No action will be taken.")
            print("")
