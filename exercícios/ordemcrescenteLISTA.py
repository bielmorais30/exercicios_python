lista = []
lista.append(int(input("N1: "))) 
lista.append(int(input("N2: ")))
lista.append(int(input("N3: ")))

aux = 0
i=0
# 3 2 1 \ 2 3 1 \  
if lista[0] > lista[1]:
    lista[0], lista[1] = lista[1], lista[0]
if lista[1] > lista[2]:
    lista[1], lista[2] = lista[2], lista[1]
if lista[0] > lista[1]:
    lista[0], lista[1] = lista[1], lista[0]
    

while i < len(lista):
    print(lista[i])
    i = i+1
# print(lista[0])
# print(lista[1])
# print(lista[2])