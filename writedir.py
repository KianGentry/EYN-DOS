import os

cwd=os.getcwd()

chf = os.stat("dir.py").st_size

if(chf == 0):
    print("Saving EYN-DOS location...")
    print("")
    with open("dir.py", 'a') as f: # opens the 'dir.save' file in 'append' mode
        f.writelines("drnm="+'(r"' + cwd + '")')
    print("Done! Continuing to EYN-DOS...")
else:
    print("Continuing...")

exit()