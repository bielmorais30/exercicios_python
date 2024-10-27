from filasPrimitivas import *

def concatenarFila(f1, f2, f3):
    aux1 = []
    aux2 = []
    flag1 = True
    flag2 = True

    while not vazia_fila(f1) and not vazia_fila(f2):

        if flag1:
            x1 = retirar(f1)
        if flag2:
            x2 = retirar(f2)

        if x1 < x2:
            flag2 = False
            inserir(f3, x1)
            inserir(aux1, x1)
        if x2 < x1:
            flag1 = False
            inserir(f3, x2)
            inserir(aux2, x2)

    if not vazia_fila(f1):
        inserir(f3, x1)
        inserir(aux1, x1)
        
        while not vazia_fila(f1):
            inserir(f3, x1)
            inserir(aux1, x1)


    if not vazia_fila(f2):
        inserir(f3, x2)
        inserir(aux2, x2)

        while not vazia_fila(f2):
            inserir(f3, x2)
            inserir(aux2, x2)

    return f3

a = [10, 30, 40, 60]
b = [20, 50, 70]
c = []

print(concatenarFila(a, b, c)+"\n"+ a + b)