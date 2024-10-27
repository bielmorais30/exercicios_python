n2e4 = 0
neg_maior = float("-inf")
repet = 0
anterior = 0
flag_neg = False

for i in range(5):
    n = int(input(f"{i+1}° Valor: "))
    if i != 0 and n == anterior:
        repet +=1
    if n < 0 and n > neg_maior:
        neg_maior = n
        flag_neg = True
    if i == 1:
        n2e4 += n
    if i == 3:
        n2e4 += n
    anterior = n
print(f"Média 2° e 4°: {n2e4/2}")
if flag_neg:
    print(f"Maior valor negativo: {neg_maior}")
else:
    print("Não existe valores negativos!")
print(f"Repetições : {repet}")