def OrdenacaoPorContagem(x):
    count = [0]*len(x)
    saida = [0]*len(x)
   
    for i in range(0, len(x)):
        menores = 0
        for i2 in range(len(x)):
            if x[i] > x[i2]:
                menores += 1
        count[i] = menores
    
    for i in range(len(count)):
        saida[count[i]] = x[i]
        
    return saida
lista = [25,57,48,37,12,92,86,33]

print(lista)

print(OrdenacaoPorContagem(lista))
        