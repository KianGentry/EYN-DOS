fn=input("What do you want to call your new file? (Extension included): ")
print("")
print("Type what you want your file to contain! (Type nul0 to exit): ")
print("")

while True:
    text=input("> ")
    
    if text.lower() == "nul0":
        break
    
    with open(fn, 'a') as f:
       f.write(text + "\n")
