while True:
    c=input("C> ")
    if c==("w"):
        w0=input("?> ")
        w1=input("1> ")
        with open((w0), 'w') as f:
            f.writelines([w1])
    if c==("r"):
        r1=input("?> ")
        with open(r1) as f:
            cont = f.read()
            print(cont)
            f.close
    if c==("e"):
        print("Goodbye!")
        exit()