ef=input("What file do you want to edit? (Including extension): ") # variable of the name of the file to edit
print("")
print("Type what you want to append to your file (Type nul0 to exit): ")
print("")

while True: # basically like write.py but its writing to an already existing file, essentially just adding onto the file
    efw=input("> ")
    
    if efw.lower() == "nul0":
        break
    
    with open(ef, "a") as f:
        f.write(efw)
