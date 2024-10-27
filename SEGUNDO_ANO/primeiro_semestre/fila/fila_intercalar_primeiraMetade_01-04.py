def inserir(f, v):
    f.append(v)  # insere um valor no final da lista


def retirar(f):
    return f.pop(0)  # retira e retorna um valor do início da lista


def vazia_fila(f):
    return False if f else True


def quantidade_fila(f):
    aux = []
    contador = 0
    while not vazia_fila(f):
        x = retirar(f)
        contador += 1
        inserir(aux, x)

    while not vazia_fila(aux):
        x = retirar(aux)
        inserir(f, x)

    return contador

    

def intercalarMetade(f1, f2, f3):
    aux1 = []
    aux2 = []
    contador = 0

    while contador <= (quantidade_fila(f1)/2):
        x = retirar(f1)
        inserir(f3, x)
        inserir(aux1, x)
        contador += 1
    while not vazia_fila(f1):
        x = retirar(f1)
        inserir(aux1, x)

    while contador >= (quantidade_fila(f2)/2):
        x = retirar(f2)
        inserir(f3, x)
        inserir(aux2, x)
        contador += 1
    while not vazia_fila(f2):
        x = retirar(f2)
        inserir(aux2, x)
    
    return f3

fila1 = [1,2,3,4,5,6,7,8,9,10]
fila2 = [1,2,3,4,5,6,7,8,9,10]
fila3 = []
print(intercalarMetade(fila1, fila2, fila3))