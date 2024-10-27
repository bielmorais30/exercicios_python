lista = [1,2,3,4,5,6,7,8,9,10]
i = len(lista)
pares = []
impar = []
while i < len(lista):
    i = i+1
    if lista[i] % 2 == 0:
        pares[i] = lista[i]
    else:
        impar[i] = lista[i]

# i=0
# while i < len(pares):
#     print(f"pares: ",pares[i])
#     i = i+1

# i=0
# while i < len(impar):
#     print(f"impar: ",impar[i])
#     i = i+1