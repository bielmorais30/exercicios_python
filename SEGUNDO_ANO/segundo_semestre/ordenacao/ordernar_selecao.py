def selecao(lis):
    for p in range(len(lis) - 1):
        ime = p #armazena o indice do menor elemento
        for i in range (p+1, len(lis)):
            if lis[i] < lis[ime]:
                ime = i
        lis[p], lis[ime] = lis[ime], lis[p]
        print('\n',lis,end='')
        
vet=[25,57,48,37,12,92,86,33]
print(f'{vet} - vetor não ordenado')
print('Passos para a ordenacao')
selecao(vet)
print(f'\n\n{vet} - vetor ordenado')