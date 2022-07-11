Weight=input("Weight Amount: ")
Unit=input("(K)g's or (L)bs: ")

if Unit==("K"):
    l1=(float(Weight)*float(2.205))
    print(str(l1)+"lbs")

if Unit==("k"):
    l2=(float(Weight)*float(2.205))
    print(str(l2)+"lbs")

if Unit==("Kg"):
    l3=(float(Weight)*float(2.205))
    print(str(l3)+"lbs")

if Unit==("kg"):
    l4=(float(Weight)*float(2.205))
    print(str(l4)+"lbs")

if Unit==("L"):
    k1=(float(Weight)/float(2.205))
    print(str(k1)+"kg")

if Unit==("l"):
    k2=(float(Weight)/float(2.205))
    print(str(k2)+"kg")

if Unit==("Lbs"):
    k3=(float(Weight)/float(2.205))
    print(str(k3)+"kg")

if Unit==("lbs"):
    k4=(float(Weight)/float(2.205))
    print(str(k4)+"kg")
