V def difPrimeiroUltimo(p):
    aux=[]
    ultimo = pop(p)
    push(aux,ultimo)

    while not vazia(p):
        v = pop(p)
        push(aux,v)
    primeiro = pop(aux)
    push(p,primeiro)
    while not vazia(aux):
        v = pop(aux)
        push(p,v)
    diferenca = ultimo - primeiro
    return diferenca


def PilhaMaiorMenor(p):
    aux=[]
    menor = maior = pop(p)
    push(aux,maior)
    while not vazia(p):
        v = pop(p)
        if v > maior:
            maior = v
        if v < menor:
            menor = v
        push(aux,v)
    while not vazia(aux):
        v = pop(aux)
        push(p,v)

    diferenca = maior - menor
    return diferenca