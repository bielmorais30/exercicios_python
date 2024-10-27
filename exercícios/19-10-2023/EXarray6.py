from random import randint

lis = [randint(10, 20) for _ in range(20)]
lis.sort()
print(f'Lista: {lis}\n')

print('Valores e quantidades:\n')
sel = [] # lista de valores já selecionados (mostrados)
for v in lis:
    if v not in sel:
        cont = 0
        for x in lis:
            if x == v:
                cont += 1
        print(f'{v}: {cont}x')
        sel.append(v)

print('\nValores e quantidades:\n')
sel = []  # lista de valores já selecionados (mostrados)
for v in lis:
    if v not in sel:
        print(f'{v}: {lis.count(v)}x')
        sel.append(v)

# Outra forma
print('\nValores e quantidades:\n')
for v in sorted(set(lis)):  # set (conjunto) elimina repetições em lis
    print(f'{v}: {lis.count(v)}x')