def arvrinha(qnt):
    for i in range(qnt+1):
        print("*"*i)
        
def arvrinhaContrario(qnt):
    a=1
    for i in range(qnt, 1 , -1):
        print(" "* i +"*"*a)
        a = a +1


arvrinha(10)
arvrinhaContrario(10)