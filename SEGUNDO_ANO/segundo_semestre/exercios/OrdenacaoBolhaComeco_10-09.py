# def bolha(lis):
#     for p in range(len(lis)-1):
#         pontero = len(lis)-p
#         for i in range(len(lis)-pontero):
#             pontero2 = len(lis)-i
#             if lis[pontero2] > lis[pontero2-1]:
#                 lis[pontero2], lis[pontero2-1] = lis[pontero2-1], lis[pontero2]
                 
            
        
# vet= [25,57,48,37,12,92,86,33]
# print(vet)
# bolha(vet)
# print(vet)    

def bolha(lis):
    for p in range(1, len(lis)):
        pontero2 = len(lis) - p
        for i in range(len(lis)-pontero2):
            pontero = len(lis)-1-i
            if lis[pontero] < lis[pontero - 1]:
                lis[pontero], lis[pontero - 1] = lis[pontero - 1], lis[pontero]
                 
            
        
vet= [25,57,48,37,12,92,86,33]
print(vet)
bolha(vet)
print(vet)    