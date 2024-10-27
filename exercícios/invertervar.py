n1 = float(input("Variavel 1:  "))
n2 = float(input("Variavel 2:  "))

if n1 > n2:
    aux = n2
    n2 = n1
    n1 = aux
    print(f"\nVariavel 1: {n1}")
    print(f"Variavel 2: {n2}")
else:
    print(f"\nVariavel 1: {n1}")
    print(f"Variavel 2: {n2}")