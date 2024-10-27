from random import randint
arr = []
par = []
impar = []
for i in range(10):
    # poderia fazer a verificação de par ou impar aqui
    arr.append(randint(1, 100))
    if arr[i] % 2 == 0:
        par.append(arr[i])
    else:
        impar.append(arr[i])
print(f"Lista completa: \n{arr}\n\nPares: \n {par}\n\nImpares: \n {impar}")

# from random import randint

# lista = [randint(1, 100) for _ in range(10)]

# par, impar = [], []
# for v in lista:
#     par.append(v) if v % 2 == 0 else impar.append(v)


# par = [v for v in lista if v % 2 == 0]
# impar = [v for v in lista if v % 2 != 0]


# print(f'Lista: {lista}')
# print(f'\nPares: {par}')
# print(f'\nÍmpares: {impar}')