n1 = int(input("1°: "))
n2 = int(input("2°: "))
n3 = int(input("3°: "))
n4 = int(input("4°: "))
n5 = int(input("5°: "))

soma = 0
repetidos = ""
# Numeros multiplos de 3
if (n1 % 3) == 0:
    soma += n1
if (n2 % 3) == 0:
    soma += n2
if (n3 % 3) == 0:
    soma += n3
if (n4 % 3) == 0:
    soma += n4
if (n5 % 3) == 0:
    soma += n5

# Numeros repetidos
if n1 == n2 or n1 == n3 or n1 == n4 or n1 == n5:

    repetidos += str(n1)

if n2 == n3 or n2 == n4 or n2 == n5 and (n2 != n1):
    if n2 != n1:
        repetidos += " " + str(n2)

if n3 == n4 or n3 == n5 and (n3 != n2 and n3 != n1):
    if n3 != n2 and n3 != n1:
        repetidos += " " + str(n3)

if n4 == n5 and (n4 != n3 and n4 != n2 and n4 != n1):
    if n4 != n3 and n4 != n2 and n4 != n1:
        repetidos += " " + str(n4)

print(f"Soma: {soma}")
print(f"Repetidos: {repetidos}")

