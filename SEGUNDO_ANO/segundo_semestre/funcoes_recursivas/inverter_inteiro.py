def inverter_inteiro(n):
    strnumber = str(n)
    if len(strnumber) <= 1:
        return strnumber
    else: 
        return strnumber[-1]+inverter_inteiro(strnumber[:-1])
    
print(inverter_inteiro(-12))