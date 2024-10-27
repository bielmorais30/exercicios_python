# lista = [1,2,3,4,5,6,7,8,9,10]
# i = len(lista)
# while i > 0:
#     i = i-1
#     print(lista[i])
    
lista = [1,2,3,4,5,6,7,8,9,10]
 
for i in range(len(lista)):
    print(lista[i])
    i = i-1
    
lista.reverse()
print(lista)