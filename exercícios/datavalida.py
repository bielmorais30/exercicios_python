d, m, a, = input("Digite a data: ").split("/")
d, m, a, = int(d), int(m), int(a)


if d > 0 and d <= 31 and m > 0 and m <= 12 and a > 0 and a <= 9999:
    if a % 4 != 0 and m == 2 and d > 28:
        # print("Data inválida!")
        valid = False
    elif a % 4 == 0 and m == 2 and d > 29:
        # print("Data inválida!")
        valid = False
    elif m % 2 == 0 and m <= 7 and d > 30:
        # print("Data não válida")
        valid = False
    elif m % 2 != 0 and m >= 8 and d > 30:
        # print("Data não válida!") 
        valid = False
    else:
        # print("Data válida!")
        valid = True 
else:
    # print("Data inválida!")
    valid = False

if valid == True:
    print(f"A data {d}/{m}/{a} é válida!")
else:
    print(f"A data {d}/{m}/{a} NÂO é válida!")