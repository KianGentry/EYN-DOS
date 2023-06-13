import os

cwd=os.getcwd()

chf=os.stat("dir.py").st_size
chf2=os.stat("eyn.sh").st_size

if(chf == 0):
    print("Writing EYN-DOS location...")
    print()
    with open("dir.py", 'a') as f: # opens the 'dir.save' file in 'append' mode
        f.writelines(f'drnm=(r"{cwd}")')
    print("Done! Continuing to EYN-DOS...")
else:
    print("Continuing...")

if(chf2 == 0):
    print("Writing shell script(s)...")
    print()
    with open("eyn.sh", 'a') as f:
        f.write("#!/bin/bash" + "\n")
        f.write(f"cd {cwd} && python3 main.py")
    with open("eyn.bat", 'a') as f:
        f.write(f"cd {cwd}" + "\n")
        f.write("py main.py")
    print("Done! Continuing to EYN-DOS...")
else:
    print("Continuing...")