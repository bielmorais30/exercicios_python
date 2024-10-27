class NoArvore:

    def __init__(self,info):
        self.info=info
        self.esq=None
        self.dir=None


class Arvore:

    def __init__(self):
        self.raiz=None

    def montaArvore(self,x):

        if self.raiz == None:
            no=NoArvore(x)
            self.raiz=no
            return
        q=None
        p=self.raiz
        while p and p.info!=x:
            q=p
            if x<p.info:
                p=p.esq
            else:
                p=p.dir
        if p:
            print(f'informacao ja cadastrada')
            return
        p=NoArvore(x)
        if x < q.info:
            q.esq = p
        else:
            q.dir = p

    def preOrdem(self,p):
        if p:
            print(f'no visitado em preOrdem {p.info}')
            self.preOrdem(p.esq)
            self.preOrdem(p.dir)


    def emOrdem(self,p):
        if p:
            self.emOrdem(p.esq)
            print(f'no visitado em emOrdem {p.info}')
            self.emOrdem(p.dir)


    def posOrdem(self,p):
        if p:
            self.posOrdem(p.esq)
            self.posOrdem(p.dir)
            print(f'no visitado em posOrdem {p.info}')

    def obterValorMinino(self,p):
        if p==None:
            return p
        if p.esq==None:
            return p
        else:
            return(self.obterValorMinino(p.esq))

    def obterValorMaximo(self,p):
        if p==None:
            return p
        if p.dir==None:
            return p
        else:
            return(self.obterValorMaximo(p.dir))



    def contaNos(self,p):
        if not p:
            return 0
        else:
            return (1+self.contaNos(p.esq) + self.contaNos(p.dir))




    def contaNosPares(self,p):
        if not p:
            return 0
        elif p.info % 2 == 0:
            return (1 + self.contaNosPares(p.esq) + self.contaNosPares(p.dir))
        else:
            return (0 +self.contaNosPares(p.esq) + self.contaNosPares(p.dir))


    def contaNosFolhas(self,p):
        if not p:
            return 0

        if not p.esq and not p.dir:
            return 1
        else:
            return (0 + self.contaNosFolhas(p.esq) + self.contaNosFolhas(p.dir))


    def mostraNosFolhas(self,p):
        if not p:
            return

        if not p.esq and not p.dir:
            print(f'no folha: {p.info}, esq: {p.esq}, dir: {p.dir}')
            return

        self.mostraNosFolhas(p.esq)
        self.mostraNosFolhas(p.dir)



arv=Arvore()

arv.montaArvore(50)
arv.montaArvore(30)
arv.montaArvore(82)
arv.montaArvore(45)
arv.montaArvore(20)
arv.montaArvore(80)
arv.montaArvore(84)

arv.preOrdem(arv.raiz)
print('\n')
arv.emOrdem(arv.raiz)
print('\n')
arv.posOrdem(arv.raiz)

print('\n')
print(f'quantidade de nos: {arv.contaNos(arv.raiz)}')
print('\n')
print(f'quantidade de pos pares: {arv.contaNosPares(arv.raiz)}')
print('\n')
print(f'\nQuantidade de nos folhas: {arv.contaNosFolhas(arv.raiz)}')

print('\n')
print(f'\nnos folhas')
arv.mostraNosFolhas(arv.raiz)

print(f'\nMenor Valor: {(arv.obterValorMinino(arv.raiz)).info}')
print(f'\nMaior Valor: {(arv.obterValorMaximo(arv.raiz)).info}')

