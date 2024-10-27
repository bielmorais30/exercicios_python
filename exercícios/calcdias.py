# jeito mais dificil:
s = int(input("Digite a quantidade de segundos: "))
d = s //(60*60*24)
h = (s % (60*60*24))//(60*60)
m = (s % (60*60*24))%(60*60)//60
s = (s % (60*60*24))%(60*60)%60

# jeito mais facil:
# s = 1000000000
# m = s // 60
# s %= 60
# h = m // 60
# m %= 60
# d = h // 24
# h %= 24
# me = 
# print(d, h, m, s)

print(f"Dias: {d} \nHoras: {h} \nMinutos: {m} \nSegundos: {s}")