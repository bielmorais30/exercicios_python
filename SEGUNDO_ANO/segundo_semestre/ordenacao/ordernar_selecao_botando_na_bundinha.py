def selecao(lis):
    #for p in range(len(lis) - 1):
    p = len(lis) - 1
    while p >= 0:
        maior = p #armazena o indice do maior elemento
        for i in range (len(lis)):
            if lis[i] > lis[maior]:
                maior = i
                i -= 1
        lis[p], lis[maior] = lis[maior], lis[p]
        print('\n',lis,end='')
        
vet=[25,57,48,37,12,92,86,33]
print(f'{vet} - vetor não ordenado')
print('Passos para a ordenacao')
selecao(vet)
print(f'\n\n{vet} - vetor ordenado')