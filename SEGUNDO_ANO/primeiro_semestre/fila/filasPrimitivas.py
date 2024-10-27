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



# fila = []
# inserir(fila, 10)
# inserir(fila, 20)
# inserir(fila, 30)

# mostrar_fila(fila)
# print(f"\nQuantidade de elementos: {quantidade_fila(fila)}")

#print(f'Elemento retirado da fila: {retirar(fila)}')

