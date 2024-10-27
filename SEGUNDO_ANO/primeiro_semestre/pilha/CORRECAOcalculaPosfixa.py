# funcoes primitivas para manipulacao de pilha

def push(p, v):  # p representa a pilha (utilizamos uma lista
                 # para representar)  e v o valor a ser inserido
    p.append(v)


def pop(p):
    return p.pop()


def vazia(p):
    return False if p else True


def calcularPosfixa(epos):
    pilha = []
    for crt in epos:
        if crt.isdigit():
            push(pilha, float(crt))
        else:
            b = pop(pilha)  # segundo termo
            a = pop(pilha)  # primeiro termo
            if crt == '+':
                r = a + b
            elif crt == '-':
                r = a - b
            elif crt == '*':
                r = a * b
            elif crt=='/':
                r = a / b
            else:
                r = a ** b
            push(pilha, r)

    return pop(pilha)


posfixa='35+42-*'
valor = calcularPosfixa(posfixa)
print(f'Valor da expressao {posfixa}: {valor}')

posfixa='623+-382/+*2$3+'
valor = calcularPosfixa(posfixa)
print(f'Valor da expressao {posfixa}: {valor}')

