try:
    n1 = int(input("Entre com o primeiro numero: "))
    n2 = int(input("\nEntre com o primeiro numero: "))
    n3 = int(input("\nEntre com o primeiro numero: "))

    maior = n1
    menor = n1

        # Descobrir o maior
    if n2 > maior:
        maior = n2
    if n3 > maior :
        maior = n3

    print(f"\nMaior: {maior}   ", end="")

        # Descobrir o menor
    if n2 < menor :
        menor = n2
    if n3 < menor :
        menor = n3

    print(f"Menor: {menor}")

except:
    print("Erro!!! Digite um numero inteiro!!!")