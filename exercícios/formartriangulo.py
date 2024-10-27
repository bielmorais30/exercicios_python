l1 = float(input("Lado 1: "))
l2 = float(input("Lado 2: "))
l3 = float(input("Lado 3: "))

if (l1 + l2) <= l3 or (l2 + l3) <= l1 or (l1 + l3) <= l2:
    print("Não é possivel formar um triandulo")
else:
    if l1 == l2 and l1 == l3:
        print("Triânulo equilatero")
    elif l1 == l2 or l1 == l3 or l3 == l2:
        print("Triângulo isóceles")
    else: 
        print("Trângulo escaleno")
