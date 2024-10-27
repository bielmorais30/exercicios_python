import math
vinicial = float(input("Entre com V° (velocidade inicial): "))
aceleracao = float(input("Entre com a aceleração: "))
tempo = float(input("Entre com t (tempo): "))
espacoinicial = float(input("Entre com S (espaço inical): "))
op = float(input("Escolha a equação: 1-Velo Final 2-Espaço Final 3-Torricelli "))

if op == 1 :

    print(f"V: {vinicial+(aceleracao*tempo)}") #não precisa de parenteses: vinicial+aceleracao*tempo
if op == 2 :
    espacofinal = espacoinicial + vinicial*tempo + 0.5*(aceleracao*(tempo**2))

    print(f"S: {espacofinal}")
if op == 3 :
    delta = float(input("Entre com o Delta S: "))
    torricelli = ((vinicial**2) + (2*aceleracao)*(delta))**0.5

    print(f"V²: {torricelli}")

