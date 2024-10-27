from random import randint
arr = [randint(10,20) for _ in range(10)]
ocorrencias = []
qnt = 0
aux = 0
flag = False
arr.sort()
for i in range(len(arr)):
    while True:
        if arr[i] == arr[(i+aux)]:
            qnt += 1
            flag = True
        if (i+aux) <= 10:
            break
    if flag:
        ocorrencias.append((arr[i], qnt))
        flag = False        
    qnt = 0
    aux = 0
print(arr)
print(ocorrencias)
