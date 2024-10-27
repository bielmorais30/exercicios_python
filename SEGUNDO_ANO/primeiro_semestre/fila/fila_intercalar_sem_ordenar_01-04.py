def inserir(f, v):
    f.append(v)  # insere um valor no final da lista


def retirar(f):
    return f.pop(0)  # retira e retorna um valor do início da lista


def vazia_fila(f):
    return False if f else True

def intercalarSemOrdenar(f1, f2, f3):
    aux1 = []
    aux2 = []
    vezf2 = False

    while not vazia_fila(f1) or not vazia_fila(f2):
        if vezf2:
            x = retirar(f2)
            inserir(f3, x)
            inserir(aux2, x)
            if not vazia_fila(f1):
                vezf2 = False
        else: 
            x = retirar(f1)
            inserir(f3, x)
            inserir(aux1, x)
            if not vazia_fila(f2):
                vezf2 = True
                
    while not vazia_fila(aux1):
        x = retirar(aux1)
        inserir(f1, x)
    while not vazia_fila(aux2):
        x = retirar(aux2)
        inserir(f2, x)
            
    return f3
        
l1 = [1,3,5]
l2 = [2,4,6,7,8]
l3 = []
print(f"{intercalarSemOrdenar(l1,l2,l3)}\n{l1}\n{l2}")