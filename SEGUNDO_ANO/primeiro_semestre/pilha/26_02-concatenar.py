from primitivas import *

p1 = [1,2,3,4,5]
p2 = [6,7,8,9,10]

def concatenar(l1, l2):
    aux = []
    l3 = []
    while not(vazia(l1)):
        x = pop(l1)
        push(aux, x)
    while not(vazia(aux)):
        x = pop(aux)
        push(l1, x)
        push(l3, x)

    while not (vazia(l2)):
        x = pop(l2)
        push(aux, x)
    while not (vazia(aux)):
        x = pop(aux)
        push(l2, x)
        push(l3, x)

    return l3

print(concatenar(p1, p2))

def intercalar(l1, l2):
    aux = []
    l3 = []
    listaum = False
    while not (vazia(l1)) or not (vazia(l2)):
        x = pop(l2)
        push(aux, x)
        x = pop(l1)
        push(aux, x)

    while not (vazia(aux)):
        x = pop(aux)
        push(l3, x)
        if listaum:
            push(l1, x)
            listaum = False
        else:
            push(l2, x)
            listaum = True


    return l3

print(intercalar(p1, p2))