def multiplicacao_russa(n,x):
    if n == 0:
        return 0
    if n%2 != 0:
        return x + multiplicacao_russa(n//2, x*2)
    else:
        return 0 + multiplicacao_russa(n//2, x*2)
    
print(multiplicacao_russa(2,8))

