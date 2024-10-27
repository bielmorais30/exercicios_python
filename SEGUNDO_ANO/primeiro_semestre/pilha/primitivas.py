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

def  precedencia(operador):
    if operador == "+" or operador == "-":
        return 1
    if operador == "*" or operador == "/":
        return 2
    if operador == "$":
        return 3
    else:
        return 0