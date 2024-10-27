from primitivas import *

def toPosfix(exp):
    pilha = []
    opr = []
    for crt in exp:
        if crt.isdigit():
            push(pilha, crt)
        else:
            if len(opr) == 0 or precedencia(crt) < precedencia(elementoTopo(opr)):   
                push(opr, crt)
            else: 
                push(pilha, crt)

    return pilha                

print(toPosfix("2+4*3-5"))