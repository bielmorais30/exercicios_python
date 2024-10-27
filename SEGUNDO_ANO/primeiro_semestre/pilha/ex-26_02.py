def push(p, v):
    p.append(v)

def pop(p):
    return p.pop()

def vazia(p):
    return False if p else True

p=[1,2,5,4,5]

def diferenca(l1):
    aux = []

    ultimo = pop(l1)

    while not(vazia(l1)):
        x = pop(l1)
        push(aux, x)

    primeiro = pop(aux)
    push(p, primeiro)

    while not(vazia(aux)):
        x = pop(aux)
        push(l1,x)

    return primeiro - ultimo



print(diferenca(p))


def diferenca2(l2):
    x = pop(l2)
    push(l2, x)
    menor = x
    maior = 0
    aux = []
    while not(vazia(l2)):
        x = pop(l2)

        if x > maior:
            maior = x
        elif x < menor:
            menor = x

        push(aux, x)

    while not(vazia(aux)):
        x = pop(aux)
        push(l2, x)

    return maior - menor

print(diferenca2(p))