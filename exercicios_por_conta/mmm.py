import random

numeros = []
i = 0
qnt = int(input("Quantidade: "))
while len(numeros) < qnt:
    n = random.randint(1,50)
    numeros.append(n)
    i += 1

def media(pArray):
    loop = 0
    total = 0
    while loop < len(pArray):
        total += pArray[loop]
        loop += 1
    media_value = total/len(pArray)
    return media_value

def mediana(pArray):
    pArray.sort()
    if len(pArray) % 2 == 0:
        indice_mediana1 = len(pArray) // 2
        indice_mediana2 = len(pArray) // 2 - 1
        mediana_value = (pArray[indice_mediana1] + pArray[indice_mediana2]) / 2
    else:
        indice_mediana = len(pArray) // 2
        mediana_value = pArray[indice_mediana]
    return mediana_value
    

def printar(pArray):
    loop2 = 0
    while len(pArray) < loop2:
        print(pArray[loop2])
        loop2 += 1

print("Média: " , media(numeros)," Mediana: ", mediana(numeros)," Print: ", print(numeros), len(numeros))
