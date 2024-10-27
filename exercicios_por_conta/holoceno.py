d, m, a, = input("Digite a data: ").split("/")
d, m, a, = int(d), int(m), int(a)

ano = 10000 + a 
mes = ""

if m == 1:
    mes = "janeiro"
elif m == 2:
    mes = "fevereiro"
elif m == 3:
    mes = "março"
elif m == 4:
    mes = "abril"
elif m == 5:
    mes = "maio"
elif m == 6:
    mes = "junho"
elif m == 7:
    mes = "julho"
elif m == 8:
    mes = "agosto"
elif m == 9:
    mes = "setembro"
elif m == 10:
    mes = "outubro"
elif m == 11:
    mes = "novembro"
elif m == 12:
    mes = "dezembro"

if a < 0:
    print(f"{d} de {mes} de {ano} a.C.")
else:
    print(f"{d} de {mes} de {ano} d.C.")
