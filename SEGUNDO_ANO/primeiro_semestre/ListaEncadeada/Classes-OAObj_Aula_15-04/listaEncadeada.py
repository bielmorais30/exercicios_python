class ListaNo:

    def __init__(self, info):
        self.info = info
        self.proximo = None


class ListaLigada:

    def __init__(self):
        self.inicio = None

    def insereInicio(self, info):
        no = ListaNo(info)
        no.proximo = self.inicio
        self.inicio = no

    def insereFinal(self, info):
        atual = self.inicio
       #while atual:
       #    if atual.proximo:
       #        atual = atual.proximo
       #    else:
       #        break
       #no = ListaNo(info)
       #atual.proximo = no
        if atual==None:
            self.insereInicio(info)
            return
        while atual.proximo:
            atual=atual.proximo
        no = ListaNo(info)
        atual.proximo=no

    def insereDepois(self, p, info):
        no = ListaNo(info)
        no.proximo = p.proximo
        p.proximo = no


    def mostraLista(self):
        atual = self.inicio
        while atual:
            print(f'Valor da informação nó: {atual.info}')
            atual = atual.proximo

    def insereOrdenado(self, x):
        atual = self.inicio
        if not atual or x < atual.info:
            self.insereInicio(x)
            return
        proxi = atual
        while proxi and proxi.info < x:
            inicio = proxi
            proxi = proxi.proximo

        if not proxi or proxi.info > x:
            self.insereDepois(atual, x)
        else:
            print("\n Elemento anteriormente cadastrado!")


a = ListaLigada()
a.insereInicio(10)
a.insereOrdenado(5)
a.insereOrdenado(3)
a.insereFinal(20)
a.mostraLista()
