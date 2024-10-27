# qnt = int(input("Quantidade: "))

# # variaveis
# anterior = 0
# atual = 0
# aux = 0

# # repetição
# for i in range(qnt):
#     if atual != 0:
#         aux = anterior + atual
#         print(f"{aux}",end=" ")
#         anterior = atual
#         atual = aux
#     else:
#         print(f"{anterior}",end=" ")
#         atual = atual + 1
#         print(f"{atual}",end=" ")
qnt = int(input("Quantidade: "))

# variaveis
anterior = 0
atual = 1
aux = 0

# repetição
for i in range(qnt):
    
    print(f"",anterior,end=" ")
    aux = anterior+atual
    anterior = atual
    atual = aux