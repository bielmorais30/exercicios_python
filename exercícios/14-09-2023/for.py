maior = 0
menor = 0
for i in range(5):
    entrada = input(f"Digite a {i+1}° nota: ")
    if menor == 0:
        menor = entrada
    if maior != 0 and entrada > menor:
        maior = entrada
    else:
        maior = menor
        menor = entrada