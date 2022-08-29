ef=input("What file do you want to edit? (Including extension): ")
print("")
print("Type what you want to append to your file (Type nul0 to exit): ")
print("")

while True:
    efw=input("> ")
    
    if efw.lower() == "nul0":
        break
    
    with open(ef, "a") as f:
        f.write(efw)
