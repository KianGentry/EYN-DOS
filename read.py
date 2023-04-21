from commands import r,wh

t=input(f"{r}What file do you want to read?: {wh}")
print()
with open(t, encoding="utf-8") as f:
    read_data = f.read()
print(read_data)
f.close