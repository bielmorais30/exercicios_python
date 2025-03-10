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
            
    while not vazia_fila(aux):
        x = retirar(aux)
        inserir(fila, x)
    
    return fila
    
def menor(fila1, fila2):
    n1 = retirar(fila1)
    n2 = retirar(fila2)
    
    if n1 > n2:
        menor = n2
        inserir(fila1, n1)
    if n2 > n1:
        menor = n1
        inserir(fila2, n2)
    return menor
    
def intercalarOrdenado(f1, f2, f3):
    aux1 = []
    aux2 = []
    flag1 = True
    flag2 = True
    while not vazia_fila(f1) or not vazia_fila(f2):
        if flag1:
            x1 = retirar(f1)
            inserir(aux1, x1)
        if flag2:
            x2 = retirar(f2)
            inserir(aux2, x2)
            
        if x1 < x2:
            inserir(f3, x1)
            flag1 = True
            flag2 = False
            print(x1)
        if x2 < x1:
            inserir(f3, x2)
            flag1 = False
            flag2 = True
            print(x2)
            
        if vazia_fila(f1):
            while not vazia_fila(f2):
                x = retirar(f2)
                inserir(f3, x)
        if vazia_fila(f2):
            while not vazia_fila(f1):
                x = retirar(f1)
                inserir(f3, x)
        
    return f3
        
        
a = [10, 30, 40, 60]
b = [20, 50, 70, 80, 90]
c = []
print(intercalarOrdenado(a, b, c))
            
        