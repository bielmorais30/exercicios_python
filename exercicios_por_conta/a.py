numeros = []
numero = int(input("Entre com o 1º número: "))
numeros.append(numero)

for i in range(9):
    numero = int(input("Entre com o %dº número: " % (i + 2)))
    numeros.append(numero)

maior = max(numeros)
print("O maior valor é", maior)
menor = min(numeros)
print("O menor valor é", menor)
l1=[]
for i in numeros:
    if i not in l1:
        l1.append(i)
    else:
        print("existem numeros iguais: ", i,end=' ')
        print()