fn=input("What do you want to call your new file? (Extension included): ") # variable for filename
print("")
print("Type what you want your file to contain! (Type nul0 to exit): ")
print("")

while True:
    text=input("> ") # variable for stuff to write to the file, loops until nul0 is typed
    
    if text.lower() == "nul0": # basically 'text' and the code below interact in a loop until nul0 is typed, then this code is executed
        break # breaks loop
    
    with open(fn, 'a') as f: # opens file in 'append' mode
       f.write(text + "\n") # writes the text entered, then if enter is struck, it makes it a new line. all done in real time
