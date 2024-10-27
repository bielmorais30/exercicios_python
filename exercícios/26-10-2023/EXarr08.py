# Criar e mostrar uma lista com 20 valores aleatórios entre 0 e 9. Pode ter valores repetidos.
# Mostrar os 3 menores valores distintos contidos na lista.
# Mostrar uma msg (Sim ou Não) se o número 1 aparece na lista antes de um 0 (seguidos). Apenas uma msg deve ser mostrada.
# Calcular e mostrar qual ou quais valores mais aparecem na lista.
from random import randint
lista = [randint(0,9) for _ in range(20)]
menores = [0,0,0]
print(lista)
for i in range(len(lista)):
    if lista[i] < menores[2]:
        if lista[i] < menores[1]:
            if lista[i] < menores[0]:
                menores[2] = menores[1]
                menores[1] = menores[0]
                menores[0] = lista[i]
            else:
                menores[2] = menores[1]
                menores[1] = lista[i]
        else:
            menores[2] = lista[i]

print(menores)