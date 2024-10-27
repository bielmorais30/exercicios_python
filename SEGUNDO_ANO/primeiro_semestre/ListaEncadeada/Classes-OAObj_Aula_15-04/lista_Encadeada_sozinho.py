class No:
    def __init__ (self, valor):
        self.valor = valor
        self.proximo = None
    

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def insereInicio(self, valor):
        no = No(valor)
        no.proximo = self.inicio
        self.inicio = no