def verificarOrdenadoRecursivo(list, final=10):
    
    if final <= 1: #Assim deu certo, o porque só Deus sabe
        return True
    if list[final-1] < list[final-2]:
        return False
    else:
        return verificarOrdenadoRecursivo(list, final-1)
        
    
lista = [1,2,3,4,5,6,7,8,9,10]
print(verificarOrdenadoRecursivo(lista,10))


#lixo de codigos:
# if list[len(list)-1] < list[len(list)-2]:
    #     return False
    # else:
    #     list2= [0]*(len(list)-1)
    #     for i in range(len(list)-1):
    #         list2[i] = list[i]
    #     return verificarOrdenadoRecursivo(list2)