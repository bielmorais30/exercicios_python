from primitivas import *
#ex = [3,5,"+",4,2,"-","*"]
ex = ["*","-",2,4,"+",5,3]
p1 = []
operador = ""
op1 = 0
op2 = 0
aux = 0
r = 0
# ex = input("Entre com a operação pósfixa: ")

# for i in ex:
#     if isinstance(i, int):
#         push(p1, i)

# print(p1)

for i in range(len(ex)):
    aux = pop(ex)
    print(aux)
    if isinstance(aux, int):
        push(p1, aux)
    else:
        aux = pop(ex)
        operador = aux
        op2 = pop(p1)
        op1 = pop(p1)
        if(operador == "+"):
            r = op1+op2
        elif(operador == "-"):
            r = op1-op2
        elif(operador == "*"):
            r = op1*op2
        elif(operador == "/"):
            r = op1/op2
        push(p1, r)

print(p1)
print(ex)