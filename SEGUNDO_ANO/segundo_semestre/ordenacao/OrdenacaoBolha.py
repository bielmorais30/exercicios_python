def bolha(lis):
    for p in range(1, len(lis)):
        for i in range(len(lis)-p):
            if lis[i] > lis[i+1]:
                lis[i], lis[i+1] = lis[i+1], lis[i]
                 
            
        
vet= [25,57,48,37,12,92,86,33]
print(vet)
bolha(vet)
print(vet)    