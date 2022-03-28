import webbrowser

print("")
print("Welcome to the EYN-DOS browser terminal! This terminal requires a web browser installed on your host system. Without this, the browser terminal cannot function.")
print("")

while True:
    browser_line=input("B:\DIR2\eyndos_1_41\eyndos.py> browser.py> ")

    if browser_line==("https://www.google.com"):
        print("")
        webbrowser.open("https://www.google.com")
    
    if browser_line==("https://github.com"):
        print("")
        webbrowser.open("https://github.com")
    
    if browser_line==("https://stackoverflow.com"):
        print("")
        webbrowser.open("https://stackoverflow.com")

    if browser_line==("https://www.geeksforgeeks.org"):
        print("")
        webbrowser.open("https://www.geeksforgeeks.org")

    if browser_line==("https://www.youtube.com"):
        print("")
        webbrowser.open("https://www.youtube.com")
    
    if browser_line==("https://discord.com"):
        print("")
        webbrowser.open("https://discord.com")

        if browser_line==("return"):
            print("")
            print("Returning to the main EYN-DOS terminal...")
            print("")
            exit()
