def inserir(f, v):
    f.append(v)  # insere um valor no final da lista


def retirar(f):
    return f.pop(0)  # retira e retorna um valor do início da lista


def vazia_fila(f):
    return False if f else True
    
def furarFila(fila, valor, posi):
    aux = []
    cont = 0
    while not vazia_fila(fila):
        if posi == cont:
            inserir(aux, valor)
            cont += 1
        else:
            x = retirar(fila)
            inserir(aux, x)
            cont += 1
            
    if posi > cont:
        inserir(aux, valor)


    while not vazia_fila(aux):
        x = retirar(aux)
        inserir(fila, x)
    
    return fila
    
a = [1,2,3,4,5]
print(furarFila(a, 10, 10))
            
        