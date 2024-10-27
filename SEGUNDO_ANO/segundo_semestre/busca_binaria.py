def busca_binaria(vet, n , chave):
    li=0
    lf=n-1
    while(li<=lf):
        meio = (li+lf)//2
        
        if chave == vet[meio]:
            return meio
        if chave < vet[meio]:
            lf = meio -1
        else:
            li = meio +1
    
    return -1

lista = [1,2,3,4,5,6,7,8,9]

print(busca_binaria(lista, 9, 8))