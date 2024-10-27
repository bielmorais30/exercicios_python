# a = menor elemento
# b = maior elemento
def ordenacao(a,b,vet):
    numero = [0]*(b-a+1)
    for i in range(len(vet)):
        numero[vet[i]-a] += 1
        
    listaOrdenada = [0]*(b-a+1)
    for i in range(len(numero)):
        cont = 0
        while cont <= numero[i]:
            listaOrdenada[cont] = numero[i]
            cont += 1
    return listaOrdenada

    
    

lista= [2,5,6,2,3,2,2,5,6,6,3,2,6,7,8]

print(ordenacao(2, 8, lista))
    