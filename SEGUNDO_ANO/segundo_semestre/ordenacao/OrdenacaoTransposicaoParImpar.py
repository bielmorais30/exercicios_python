def transposicaoParImpar(lis):
    continua=True
    while continua:
        continua=False
        for i in range(0, len(lis)-1, 2):
            if lis[i] > lis[i+1]:
                lis[i], lis[i+1] = lis[i+1], lis[i]
                continua=True
        for i in range(1, len(lis)-1, 2):
            if lis[i] > lis[i+1]:
                lis[i], lis[i+1] = lis[i+1], lis[i]

lista = [4,5,6,1,56,1,5]
print(lista)
transposicaoParImpar(lista)
print(lista)