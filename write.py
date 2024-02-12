from commands import inp2,wh,r,inp3

fn=input(f"{r}What do you want to call your new file? (Extension included){inp2} {wh}") # variable for filename
print(f"{r}")
print(f"Type what you want your file to contain! (Type nul0 to exit)")
print(f"{r}")

while True:
    text=input(f"{r}{inp3} {wh}") # variable for stuff to write to the file, loops until nul0 is typed
    
    if text.lower()=="nul0": # basically 'text' and the code below interact in a loop until nul0 is typed, then this code is executed
        break # breaks loop
    
    with open(fn,'a') as f: # opens file in 'append' mode
       f.write(text+"\n") # writes the text entered, then if enter is struck, it makes it a new line. all done in real time
