from math import floor
#print(floor(3.5))
def quantidade_digitos(n):
    qnt = 1
    if n <= 0:
        return 0
    else:
        
        qnt += quantidade_digitos(floor(n / 10))
        return qnt

print("A quantidade de digitor inteiros é: ",quantidade_digitos(7625.1))
