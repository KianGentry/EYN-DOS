import os
import tkinter as tk
from tkinter.ttk import *

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
print("In order for EYN-DOS to work as intended, please type 'install' and install 'eyndos_1_1.zpd' and 'eyn_os_0_1.py'.")
print("")

command_list="122333444455555code1"

if command_list!="122333444455555code1":
    print("Bad command")

while True:
    command_line=input("A:\DIR1\eyndos.py> ")

    if command_line=="help":
        print("")
        print("help = Displays commands currently usable, dir = Shows available directories, files = Shows available files, run = Runs an executable file, end = Ends code, settings = Shows settings for EYN-DOS, install = Searches for installables. Attempting to execute an unkown command results in a blank response. For further support, contact EYN-DOS Support#9295 via Discord or eyndos@gmail.com via electronic mail.")
        print("")
        command_list=="122333444455555code1"
    
    if command_line==("install"):
        print("")
        print("Type 'install (file)' to install that file.")
        print("Type 'n' to return to the EYN-DOS Main Terminal.")
        print("")
        print("")
        print("Searching...")
        print("")
        print("2 INSTALL FILES FOUND:")
        print("     eyndos_1_1.zpd")
        print("     eyn_os_0_1.py")
        print("")
        ins_ans=input("A:\DIR1\eyndos.py\install> ")

        if ins_ans==("install eyn_os_0_1.py"):
            print("")
            os_exp=input("WARNING: EYN-OS 0.1 IS IN A HIGHLY EXPERIMENTAL STATE AND SHOULD NOT BE EXPECTED TO BE BUG-FREE OR FINISHED. CONTINUE? (y/n) ")
            print("")

            if os_exp==("y"):
                print("")
                print("Installing...")
                print("")
                print("        (1kb/1kb)")
                print("[||||||||||||||||||||||||]")
                print("")
                print("Installation complete.")
                print("")
            
            if os_exp==("n"):
                print("")
                print("Install Terminal Disbanded.")
                print("")

        if ins_ans==("eyndos_1_1.zpd info"):
            print("")
            print("eyndos_1_1 is the 1st package installation file for EYN-DOS 1.0")
            print("")

        if ins_ans=="install eyndos_1_1.zpd":
            print("")
            print("Installing...")
            print("")
            ins_ans2=input("eyndos_1_1.zpd already exists. Replace? (y/n) ")

            if ins_ans2=="y":
                print("")
                print("     (34kb/43kb)")
                print("[|||||||||||||||||-------]")
                print("")
                ins_corr1=input("minesweeper.py is corrupted. Install anyway? (y/n) ")
                if ins_corr1==("y"):
                    print("")
                    print("     (43kb/43kb)")
                    print("[||||||||||||||||||||||||]")
                    print("")
                    print("Installation complete.")
                    print("")
                
                if ins_corr1==("n"):
                    print("")
                    print("minesweeper.py will not be included.")
                    print("")
                    print("     (34kb/34kb)")
                    print("[||||||||||||||||||||]")
                    print("")
                    print("Installation complete.")
                    print("")
        
            if ins_ans2=="n":
                print("")
                print("     (34kb/43kb)")
                print("[|||||||||||||||||-------]")
                print("")
                ins_corr2=input("minesweeper.py is corrupted. Install anyway? (y/n)")
                if ins_corr2==("y"):
                    print("")
                    print("     (43kb/43kb)")
                    print("[||||||||||||||||||||||||]")
                    print("")
                    print("Installation complete.")
                    print("")
                
                if ins_corr2==("n"):
                    print("")
                    print("minesweeper.py will not be included.")
                    print("")
                    print("     (34kb/34kb)")
                    print("[||||||||||||||||||||]")
                    print("")
                    print("Installation complete.")
                    print("")
                
        if ins_ans=="n":
            print("")
            print("Install Terminal Disbaned.")
            print("")

    if command_line=="dir":
        print("")
        print("DIR1 (Max Storage: 1mb)")
        print("")
        command_list=="122333444455555code1"
    
    if command_line=="files":
        if ins_ans2=="y":
            if ins_corr1==("y"): 
                if os_exp==("y"):
                    print("")
                    print("DIR1 - eyndos_1_1.zpd - 10 FILES: ")
                    print("")
                    print("     eyndos.py - 13kb")
                    print("     calculator.py - 1kb")
                    print("     minesweeper.py - 9kb")
                    print("     notebook.py - 1kb")
                    print("     solitaire.py - 12kb")
                    print("     test1.py - 1kb")
                    print("     kg_lbs_weight_converter.py - 1kb")
                    print("     gui_calculator.py - 4kb")
                    print("     clock.py - 1kb")
                    print("     eyn_os_0_1.py - 1kb")
                    print("")
                    print(" Total: 44kb")
                    print("")
                
                if os_exp==("n"):
                    print("")
                    print("DIR1 - eyndos_1_1.zpd - 9 FILES: ")
                    print("")
                    print("     eyndos.py - 13kb")
                    print("     calculator.py - 1kb")
                    print("     minesweeper.py - 9kb")
                    print("     notebook.py - 1kb")
                    print("     solitaire.py - 12kb")
                    print("     test1.py - 1kb")
                    print("     kg_lbs_weight_converter.py - 1kb")
                    print("     gui_calculator.py - 4kb")
                    print("     clock.py - 1kb")
                    print("")
                    print(" Total: 43kb")
                    print("")
            
            if ins_corr1==("n"):
                if os_exp==("y"):
                    print("")
                    print("DIR1 - eyndos_1_1.zpd - 9 FILES: ")
                    print("")
                    print("     eyndos.py - 13kb")
                    print("     calculator.py - 1kb")
                    print("     notebook.py - 1kb")
                    print("     solitaire.py - 12kb")
                    print("     test1.py - 1kb")
                    print("     kg_lbs_weight_converter.py - 1kb")
                    print("     gui_calculator.py - 4kb")
                    print("     clock.py - 1kb")
                    print("     eyn_os_0_1.py - 1kb")
                    print("")
                    print(" Total: 35kb")
                    print("")

                if os_exp==("n"):
                    print("")
                    print("DIR1 - eyndos_1_1.zpd - 8 FILES: ")
                    print("")
                    print("     eyndos.py - 13kb")
                    print("     calculator.py - 1kb")
                    print("     notebook.py - 1kb")
                    print("     solitaire.py - 12kb")
                    print("     test1.py - 1kb")
                    print("     kg_lbs_weight_converter.py - 1kb")
                    print("     gui_calculator.py - 4kb")
                    print("     clock.py - 1kb")
                    print("")
                    print(" Total: 34kb")
                    print("")

        if ins_ans2=="n":
            if ins_corr2==("y"):
                if os_exp==("y"):
                    print("")
                    print("DIR1 - eyndos_1_1 - 11 FILES: ")
                    print("")
                    print("     eyndos.py -13kb")
                    print("     calculator.py - 1kb")
                    print("     minesweeper.py - 9kb")
                    print("     notebook.py - 1kb")
                    print("     solitaire.py - 12kb")
                    print("     test1.py - 1kb")
                    print("     kg_lbs_weight_converter.py - 1kb")
                    print("     eyndos.py - 13kb")
                    print("     gui_calculator.py - 4kb")
                    print("     clock.py - 1kb")
                    print("     eyn_os_0_1.py - 1kb")
                    print("")
                    print(" Total: 57kb")
                    print("")

                if os_exp==("n"):
                    print("")
                    print("DIR1 - eyndos_1_1 - 10 FILES: ")
                    print("")
                    print("     eyndos.py -13kb")
                    print("     calculator.py - 1kb")
                    print("     minesweeper.py - 9kb")
                    print("     notebook.py - 1kb")
                    print("     solitaire.py - 12kb")
                    print("     test1.py - 1kb")
                    print("     kg_lbs_weight_converter.py - 1kb")
                    print("     eyndos.py - 13kb")
                    print("     gui_calculator.py - 4kb")
                    print("     clock.py - 1kb")
                    print("")
                    print(" Total: 56kb")
                    print("")

            if ins_corr2==("n"):
                if os_exp==("y"):
                    print("")
                    print("DIR1 - eyndos_1_1 - 10 FILES: ")
                    print("")
                    print("     eyndos.py -13kb")
                    print("     calculator.py - 1kb")
                    print("     notebook.py - 1kb")
                    print("     solitaire.py - 12kb")
                    print("     test1.py - 1kb")
                    print("     kg_lbs_weight_converter.py - 1kb")
                    print("     eyndos.py - 13kb")
                    print("     gui_calculator.py - 4kb")
                    print("     clock.py - 1kb")
                    print("     eyn_os_0_1 - 1kb")
                    print("")
                    print(" Total: 47kb")
                    print("")
                
                if os_exp==("n"):
                    print("")
                    print("DIR1 - eyndos_1_1 - 9 FILES: ")
                    print("")
                    print("     eyndos.py -13kb")
                    print("     calculator.py - 1kb")
                    print("     notebook.py - 1kb")
                    print("     solitaire.py - 12kb")
                    print("     test1.py - 1kb")
                    print("     kg_lbs_weight_converter.py - 1kb")
                    print("     eyndos.py - 13kb")
                    print("     gui_calculator.py - 4kb")
                    print("     clock.py - 1kb")
                    print("")
                    print(" Total: 46kb")
                    print("")
        command_list=="122333444455555code1"
        
    if command_line=="run eyndos.py":
        print("")
        print("This is already running!")
        print("")
        command_list=="122333444455555code1"
        
    if command_line=="end":
        exit()
        
    if command_line=="run calculator.py":
        print("")
        os.system('py calculator.py')
        print("")
        command_list="122333444455555code1"

    if command_line==("run minesweeper.py"):
        print("")
        print("minesweeper.py is corrupted. This will hopefully be fixed in future EYN-DOS updates.")
        print("")

    if command_line==("settings"):
        print(" █████  ██████  ██████  ██████  ██████  ██    ██   █████   █████")
        print("█       █         ██      ██      ██    ███   ██  █       █")
        print(" ████   ██████    ██      ██      ██    ██ ██ ██  █  ███   ████")
        print("     █  █         ██      ██      ██    ██   ███  █   ██       █")
        print(" ████   ██████    ██      ██    ██████  ██    ██   ████    ████")
        print("")
        print("Type the setting name to edit that setting's configuration. Type enter to disband settings.")
        print("")
        print("█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
        print("██mono█-█True███test2█-█True███test3█-█True██████████████████████████████████████████████████████████████████████████████████████████")
        print("█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
        setting_line=input("")
        if setting_line==("mono"):
            print("")
            setting_yn_1=input("test1 is set to True. Change? (Y/N)")
            if setting_yn_1==("y"):
                print("")
                print("Error has occured. Contact EYN-DOS Support#9295 via Discord or eyndos@gmail.com via electronic mail for further support.")
                print("")
            
            if setting_yn_1==("n"):
                print("")
                print("test1 is now True.")
                print("")
        
        if setting_line==("test2"):
            print("")
            setting_yn_2=input("test2 is set to True. Change? (Y/N)")
            if setting_yn_2==("y"):
                print("")
                print("Error has occured. Contact EYN-DOS Support#9295 via Discord or eyndos@gmail.com via electronic mail for further support.")
                print("")
            
            if setting_yn_2==("n"):
                print("")
                print("test2 is now True.")
                print("")
            command_list=="122333444455555code1"
    
        if setting_line==("test3"):
            print("")
            setting_yn_3=input("test3 is set to True. Change? (Y/N)")
            if setting_yn_3==("y"):
                print("")
                print("Error has occured. Contact EYN-DOS Support#9295 via Discord or eyndos@gmail.com via electronic mail for further support.")
                print("")
            
            if setting_yn_3==("n"):
                print("")
                print("test3 is now True.")
                print("")

    if command_line==("run notebook.py"):
        print("")
        print("█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
        print("██Notebook█-█Input████████████████████████████████████████████████████████████ Hold the 'Enter' key to end the notebook session██████")
        print("█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")
        words=input("")

        next_page=words*37
        word2=input("To create a new page, type 'np'.")
        if word2==("np"):
            print("Error has occured. Contact EYN-DOS Support#9295 via Discord or eyndos@gmail.com via electronic mail for further support.")
        command_list=="122333444455555code1"
    
    if command_line==("lgr"):
        print("")
        print("Hey, that's a good YouTube channel!")
        print("")
        command_list=="122333444455555code1"
    
    if command_line==("fdisk"):
        print("")
        print("Sorry, but no.")
        print("")
        command_list=="122333444455555code1"
    
    if command_line==("win"):
        print("")
        print("No.")
        print("")
        command_list=="122333444455555code1"
    
    if command_line==("bin"):
        print("")
        print("No, I'm good.")
        print("")
        command_list=="122333444455555code1"
    
    if command_line==("run solitaire.py"):
        "Credit to 'shomikj' on GitHub for this code!"
        print("")
        os.system('py solitaire.py')
        print("")
        command_list=="122333444455555code1"

    if command_line==("run test1.py"):
        root= tk.Tk()

        canvas1 = tk.Canvas(root, width = 300, height = 300)
        canvas1.pack()

        def hello ():  
            label1 = tk.Label(root, text= "test", fg='black', font=('Ariel', 12, 'bold'))
            canvas1.create_window(150, 200, window=label1)
    
        button1 = tk.Button(text='test',command=hello, bg='brown',fg='grey')
        canvas1.create_window(150, 150, window=button1)

        root.mainloop()

    if command_line==("run kg_lbs_weight_converter.py"):
        print("")
        os.system("py weight_converter.py")
        print("")
        command_list=="122333444455555code1"

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

    if command_line==("run eyn_os_0_1.py"):
        print("")
        os.system('py eyn_os_0_1.py')
        print("")
    
    if command_line==("setup"):
        print("")
        print("Get out of my terminal.")
        print("")

    if command_line==("create dir"):
        print("")
        print("Coming soon...")
        print("")