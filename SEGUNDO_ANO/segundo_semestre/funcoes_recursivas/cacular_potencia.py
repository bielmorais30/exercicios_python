def calcular_potencia(x, n):
    if n == 0:
        return 1
    if n > 0:
        return x * calcular_potencia(x, n-1)
    else:
        return x/calcular_potencia(x, n+1)
    
print(calcular_potencia(3,2))