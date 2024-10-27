# Criar e mostrar uma lista com 20 valores aleatórios entre 0 e 9. Pode ter valores repetidos.
# Mostrar os 3 menores valores distintos contidos na lista.
# Mostrar uma msg (Sim ou Não) se o número 1 aparece na lista antes de um 0 (seguidos). Apenas uma msg deve ser mostrada.
# Calcular e mostrar qual ou quais valores mais aparecem na lista.
from random import randint
lista = [randint(0,9) for _ in range(20)]
menores = sorted(set(lista))
qnt = [0 for a in range(20)]
moda = []
flag = False
print(f"Lista:   {lista}")


for i in range(len(lista)):
    if lista[i] == 1 and lista[i+1] == 0:
        flag = True
    for i2 in range(len(lista)):
        if lista[i2] == lista[i]:
            qnt[i] += 1

print(f'Espelho: {qnt}')            
print(f'Menores: {menores[0]} , {menores[1]} , {menores[2]}')            

if flag:
    print("Sim")
else:
    print("Não")


for indice, valor in enumerate(qnt):
    if valor == max(qnt):
        if lista[indice] not in moda:
            moda.append(lista[indice])

print(f'Mais aparece: {moda}')