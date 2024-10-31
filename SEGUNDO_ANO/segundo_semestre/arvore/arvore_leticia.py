class No:
    def __init__(self, valor):
        self.valor = valor
        self.filhos = []

    def adicionar_filho(self, filho):
        self.filhos.append(filho)

    def __str__(self, nivel=0):
        ret = " " * nivel + repr(self.valor) + "\n"
        for filho in self.filhos:
            ret += filho.__str__(nivel + 2)
        return ret


class ArvoreLeticia:
    def __init__(self, raiz):
        self.raiz = No(raiz)

    def __str__(self):
        return str(self.raiz)



arvore = ArvoreLeticia("Letícia")
no_filho1 = No("Filho 1")
no_filho2 = No("Filho 2")

arvore.raiz.adicionar_filho(no_filho1)
arvore.raiz.adicionar_filho(no_filho2)

no_filho1.adicionar_filho(No("Neto 1"))
no_filho1.adicionar_filho(No("Neto 2"))

print(arvore)
