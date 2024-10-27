import math
vinicial = float(input("Entre com V° (velocidade inicial): "))
aceleracao = float(input("Entre com a aceleração: "))
tempo = float(input("Entre com t (tempo): "))
espacoinicial = float(input("Entre com S (espaço inical): "))


print(f"V: {vinicial+(aceleracao*tempo)}")

espacofinal = espacoinicial + vinicial*tempo + 0.5*(aceleracao*(tempo**2))

print(f"S: {espacofinal}")

torricelli = ((vinicial**2) + (2*aceleracao)*(espacofinal-espacoinicial))**0.5

print(f"V²: {torricelli}")

