def push(p, v):
    p.append(v)

def pop(p):
    return p.pop()

def vazia(p):
    return False if p else True

p=[]

push(p,1)
push(p,2)
push(p,3)

#x = pop(p)

def mostrarPilha(p):
    aux = []
    while not(vazia(p)):
        x = pop(p)
        print(x, end=' ')
        push(aux, x)

    while not(vazia(aux)):
        x = pop(aux)
        push(p,x)

mostrarPilha(p)

def elementos(p):
    aux = []
    contador = 0
    while not vazia(p):
        x = pop(p)
        push(aux, x)
    while not vazia(aux):
        x = pop(aux)
        contador = contador + 1
        push(p, x)
    return contador

print(f'\nQuantidade de elementos {elementos(p)}')

def primeiro(p):
    aux = []
    um = 0
    while not vazia(p):
        x = pop(p)
        push(aux, x)

    um = pop(aux)
    push(p, um)

    while not vazia(aux):
        x = pop(aux)
        push(p, x)

    return um

print(f'Primeiro elemento: {primeiro(p)}')

#while not(vazia(p)):
    #    x = pop(p)
    #print(f'valor desempilhado da pilha p: {x}')
#print(p)


