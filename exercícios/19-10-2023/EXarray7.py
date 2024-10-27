from random import randint

arr1, arr2 = [], []
aux = 0
for i in range(10):
    while True:
        aux = randint(1, 100)
        if aux not in arr1:
            arr1.append(aux)
            break
aux = 0
for i2 in range(20):
    while True:
        aux = randint(1, 100)
        if aux not in arr2:
            arr2.append(aux)
            break
    
print(arr1,arr2)