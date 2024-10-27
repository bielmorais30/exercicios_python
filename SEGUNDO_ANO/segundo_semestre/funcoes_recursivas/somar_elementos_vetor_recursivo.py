def somaVetor(vetor, tamanho):
    # if tamanho <= 1:
    #     return vetor[0]
    # else:
    #     return vetor[tamanho-1] + somaVetor(vetor, tamanho-1)
    
    if tamanho == 0:
        return 0
    else:
        return vetor[tamanho-1] + somaVetor(vetor, tamanho-1)
    

vet = [2,3,4,5]
print(somaVetor(vet, 4))


