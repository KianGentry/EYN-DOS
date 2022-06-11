print("Type 'exit(note)' to return to the main terminal.")
print("")

while True:
    notebook_line=input("")

    notebook_l2=notebook_line

    if notebook_line==("exit(note)"):
        print("")
        print("Returning to the EYN-DOS main terminal...")
        exit()

    if notebook_line==("save(note)"):
        print("")
        note_filename=input("What do you want to call your file? (including extension): ")
        print("")
        with open((note_filename), 'w') as f:
            f.write(notebook_line)
            