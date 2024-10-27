from random import randint
arr = [randint(10,20) for _ in range(10)]
ocorrencias = []
qnt = 0
aux = 0
arr.sort()
for i in range(len(arr)):
    while (i+aux) < len(arr):
        if arr[i] == arr[(i+aux)]:
            qnt += 1
            
        if qnt > 0 and (i+aux) == len(arr):
            ocorrencias.append((arr[i], qnt))
            break
        if qnt == 0 and aux >= len(arr):
            break
        aux += 1   

    qnt = 0
    aux = 0
print(arr)
print(ocorrencias)
