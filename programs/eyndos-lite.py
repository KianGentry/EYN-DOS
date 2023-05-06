while True:
    c=input()
    if c==('/'):
        q=input('n')
        w=input('>')
        with open(q,'w') as f:
            f.write(w)
    if c==('-'):
        r=input('>')
        with open(r) as f:
            print(f.read())
            f.close
    if c==('.'):
        exit()