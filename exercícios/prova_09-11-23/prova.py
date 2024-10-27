from random import randint ###
premiado = False  ###
repet = 0  ##
sorteio = [randint(1, 60) for _ in range(6)]  ##
lista_acertos = []##
def gerar(lista): ##
    for i in range(10):##
        rnd = randint(1,60)##
        if rnd not in lista:##
            lista.append(rnd)##
    lista = lista.sort() ##
print("----------------------------------------")
while not(premiado):
    repet += 1
    jogo1 = []
    jogo1_acertos = 0
    jogo2 = []
    jogo2_acertos = 0
    jogo3 = []
    jogo3_acertos = 0

    rnd = 0
    
    #gerou os jogos
    gerar(jogo1)
    gerar(jogo2)
    gerar(jogo3)

    #verifica acertos
    for n in sorteio:
        if n in jogo1:
            jogo1_acertos += 1
        if n in jogo2:
            jogo2_acertos += 1
        if n in jogo3:
            jogo3_acertos += 1
        

   
    print(f"Jogo1: {jogo1}" )
    print(f"Jogo2: {jogo2}" )
    print(f"Jogo3: {jogo3}" )

    print(f"Sorteio: {sorted(sorteio)}")
    print(f"Acertos jogo 1: {jogo1_acertos}")
    print(f"Acertos jogo 2: {jogo2_acertos}")
    print(f"Acertos jogo 3: {jogo3_acertos}")


    
    if jogo1_acertos > jogo2_acertos and jogo1_acertos> jogo3_acertos and jogo1_acertos != jogo2_acertos and jogo1_acertos != jogo3_acertos:
        lista_acertos = [1]
    if jogo1_acertos == jogo2_acertos and jogo1_acertos != jogo3_acertos:
        lista_acertos = [1,2]
    if jogo1_acertos == jogo3_acertos and jogo1_acertos != jogo2_acertos:    
        lista_acertos=[1,3]
    if jogo1_acertos == jogo2_acertos == jogo3_acertos:
        lista_acertos=[1,2,3]
    if jogo2_acertos > jogo1_acertos and jogo2_acertos> jogo3_acertos and jogo2_acertos != jogo1_acertos and jogo2_acertos != jogo3_acertos:
        lista_acertos=[2]
    if jogo2_acertos == jogo3_acertos and jogo2_acertos != jogo2_acertos:    
        lista_acertos=[2,3]
    if jogo3_acertos > jogo1_acertos and jogo3_acertos> jogo2_acertos and jogo3_acertos != jogo1_acertos and jogo3_acertos != jogo2_acertos:
        lista_acertos = [3]
       
    print(f"Maiores acertos: {lista_acertos}")

    print("----------------------------------------")


    if jogo1_acertos > 4 or jogo2_acertos > 4 or jogo3_acertos > 4:
        premiado = True
        print(f"Repetições: {repet}")
        