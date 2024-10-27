def somaPares(vet, tamanho):
    if tamanho == 0:
        return 0
    else:
        if vet[tamanho - 1] % 2 == 0:
            return vet[tamanho - 1] + somaPares(vet, tamanho-1)
        else:
            return somaPares(vet, tamanho-1)
        
        
def somaPositivos(vet, tamanho):
    if tamanho == 0:
        return 0
    else:
        if vet[tamanho - 1] >= 0:
            return vet[tamanho - 1] + somaPares(vet, tamanho-1)
        else:
            return somaPares(vet, tamanho-1)

        
vet = [2,4,3,6,5]

print(somaPares(vet,5))