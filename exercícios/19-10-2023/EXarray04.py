arr = []
aux = 0
repetido = False
for i in range(5):
    while True:
        aux = input(f"{i+1}° numero: ")
        for i2 in range(len(arr)):
            if aux == arr[i2]:
                repetido = True
            else:
                repetido = False
        if repetido:
            print("Valor já inserido. Digite novamente...")
        else: 
            arr.append(aux)
            break
print(arr)

# lis = []
# i = 0
# while i < 5:
#     val = int(input(f'{i + 1}º valor: '))
#     if val not in lis:
#         lis.append(val)
#         i += 1
#     else:
#         print('Valor já digitado. Digite novamente...')

# print(f'\nLista = {lis}')