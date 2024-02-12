import os

cwd=os.getcwd()

chf=os.stat("dir.py").st_size # the size of 'dir.py

if(chf==0): # if 'dir.py' has a size equal to zero
    print("Saving EYN-DOS location...")
    print()
    with open("dir.py",'a') as f: # open the 'dir.py' file in 'append' mode
        f.writelines(f'drnm=(r"{cwd}")') # writes that to the file
    print("Done! Continuing to EYN-DOS...")
else:
    print("Continuing...")

exit() # closes this file