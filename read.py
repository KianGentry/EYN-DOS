t=input("What file do you want to read?: ")
print("")
with open(t, encoding="utf-8") as f:
    read_data = f.read()
print(read_data)
f.close