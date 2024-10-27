from primitivas import *

def concatenaPilha (p1,p2,p3):

  aux1=[]

  aux2=[]

  while not vazia(p1):

    valor = pop(p1)

    push(aux1,valor)

  while not vazia(p2):

    valor = pop(p2)

    push(aux2,valor)



  while not vazia(aux1):

    valor = pop (aux1)

    push(p1,valor)

    push(p3,valor)



  while not vazia(aux2):

    valor = pop (aux2)

    push(p2,valor)

    push(p3,valor)





def intercalaPilha(p1,p2,p3):

  aux1=[]

  aux2=[]



  while not vazia(p1):

    valor = pop(p1)

    push(aux1,valor)

  while not vazia(p2):

    valor = pop(p2)

    push(aux2,valor)



  while not vazia(aux1) and not vazia(aux2):

    valor = pop(aux1)

    push(p1,valor)

    push(p3,valor)

    valor = pop(aux2)

    push(p2,valor)

    push(p3,valor)



  while not vazia(aux1):

    valor = pop (aux1)

    push(p1,valor)

    push(p3,valor)



  while not vazia(aux2):

    valor = pop (aux2)

    push(p2,valor)

    push(p3,valor)





p=[]

push(p,10)

push(p,20)

push(p,30)

push(p,40)

push(p,50)



p2=[]

push(p2,60)

push(p2,70)

push(p2,80)



p5=[]

p6=[]









concatenaPilha (p,p2,p5)

print('pilha 5')

mostrarPilha(p5)

intercalaPilha(p,p2,p6)

print('pilha 6')

mostrarPilha(p6)