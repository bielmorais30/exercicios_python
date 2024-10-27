def inverter_inteiro(num, n):
    if n == 0:
        return 0
    else:
        return ((num%10)*(10**(n-1)) + inverter_inteiro(num//10, n-1))
    
print(inverter_inteiro(12, 2))