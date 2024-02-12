from commands import r,wh,inp2

t=input(f"{r}What file do you want to read?{inp2} {wh}")
print()
with open(t, encoding="utf-8") as f:
    read_data = f.read()
print(read_data)
f.close