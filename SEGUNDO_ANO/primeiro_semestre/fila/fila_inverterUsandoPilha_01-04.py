def push(p, v):
    p.append(v)

def pop(p):
    return p.pop()

def vazia(p):
    return False if p else True

def elementoTopo(p):
    valor = pop(p)
    push(p, valor)
    return valor

def inserir(f, v):
    f.append(v)  # insere um valor no final da lista


def retirar(f):
    return f.pop(0)  # retira e retorna um valor do início da lista


def vazia_fila(f):
    return False if f else True

def mostrar_fila(f):
    aux = []
    while not(vazia_fila(f)):
        x = retirar(f)
        print(x, end=' ')
        inserir(aux, x)

    while not(vazia_fila(aux)):
        x = retirar(aux)
        inserir(f, x)


def inverterFila(f1):
    p1 = []
    while not vazia_fila(f1):
        x = retirar(f1)
        push(p1, x)
    while not vazia(p1):
        x = pop(p1)
        inserir(f1, x)

    return f1

fila = [1,2,3,4]

print(inverterFila(fila))