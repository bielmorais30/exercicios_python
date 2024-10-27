lista = [int(input(f'{ i+ 1}° Valor: '))for i in range(5)]
print(lista[0], end='')
for i in range(1, len(lista)):
    print(f', {lista[i]}',end='')
    