def representacaoBin(n):
    if n > 1:
        
        return  str(representacaoBin(n//2))+str(n%2)
    elif 1:
        return "1"
    else:
        return "0"
    
    
    
print(representacaoBin(25))