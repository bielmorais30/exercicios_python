try:
    n1 = int(input("N1:"))
    n2 = int(input("N2:"))
    n3 = int(input("n3:"))
    n4 = int(input("n4:"))
    n5 = int(input("n5:"))

    neg = 0

    if n1 < 0 :
        neg =+ 1
    if n2 < 0 :
        neg =+ 1
    if n3 < 0 :
        neg =+ 1
    if n4 < 0 :
        neg =+ 1
    if n5 < 0 :
        neg =+ 1

    print(f"Numero de negativos: {neg}")
except:
    print("Erro")