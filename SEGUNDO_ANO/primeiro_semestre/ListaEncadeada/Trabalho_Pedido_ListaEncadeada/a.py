class No:
    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        
    
lista = ListaEncadeada()

a = No(1)
b = No(2)
c = No(3)

lista.inicio = a

lista.inicio.proximo = b

lista.inicio.proximo.proximo = c


print(lista.inicio.proximo.proximo.conteudo)

del a
del lista.inicio.proximo

print(lista.inicio.conteudo)
print(lista.inicio.proximo.conteudo)

