arr = [1,2,3,1,5,6,7]
x = int(input("Escolha um numero: "))
encontrou = False
# for indice, valor in enumerate(arr):    (0,1),(1,2),(indice, valor)
for i in range(len(arr)):
    # if x in list: ver se tem esse valor no array
    if arr[i] == x:
        print('Posição (índice) = ',i)
        encontrou = True
        #break para pegar somente o primeiro valor
if not(encontrou):
    print('Posição (índice) = -1')