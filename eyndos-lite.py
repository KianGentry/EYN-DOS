while True:
    c=input(">")
    if c==("w"):
        q=input("?>")
        w=input("1>")
        with open((q),'w') as f:
            f.writelines([w])
    if c==("r"):
        r=input("?>")
        with open(r) as f:
            d=f.read()
            print(d)
            f.close
    if c==("e"):
        exit()