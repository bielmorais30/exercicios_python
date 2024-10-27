from random import randint
premiado = False
repet = 0
macertos = [float('-inf'), float('-inf'), float('-inf')]
sorteio = [randint(1, 60) for _ in range(6)]
def gerar(lista):
    for i in range(10):
        rnd = randint(1,60)
        if rnd not in lista:
            lista.append(rnd)
    lista = lista.sort()

# def maiores(acertos1, acertos2, acertos3, lista): 
#     lista
#     if acertos1 > lis


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

    

    if jogo1_acertos > 4 or jogo2_acertos > 4 or jogo3_acertos > 4:
        premiado = True
        print(f"Repetições: {repet}")
        