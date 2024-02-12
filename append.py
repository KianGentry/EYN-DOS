from commands import inp2,wh,r,inp3

ef=input(f"What file do you want to edit? (Including extension){inp2} {wh}") # variable of the name of the file to edit
print(f"{r}")
print(f"Type what you want to append to your file (Type nul0 to exit):")
print(f"{r}")

while True: # basically like write.py but its writing to an already existing file, essentially just adding onto the file
    efw=input(f"{r}{inp3} {wh}")
    
    if efw.lower() == "nul0":
        break
    
    with open(ef, "a") as f:
        f.write(efw)
