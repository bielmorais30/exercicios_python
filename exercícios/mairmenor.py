n1 = int(input("Entre com o primeiro numero: "))
n2 = int(input("\nEntre com o primeiro numero: "))
n3 = int(input("\nEntre com o primeiro numero: "))
    # Descobrir o maior
if n1 > n2 and n1 > n3 :
    print(f"\nMaior: {n1}   ", end="")
if n2 > n1 and n2 > n3 :
    print(f"\nMaior: {n2}   ", end="")
if n3 > n1 and n3 > n2 :
    print(f"\nMaior: {n3}   ", end="")
    # Descobrir o menor
if n1 < n2 and n1 < n3 :
    print(f"Menor: {n1}")
if n2 < n1 and n2 < n3 :
    print(f"Menor: {n2}")
if n3 < n1 and n3 < n2 :
    print(f"Menor: {n3}")