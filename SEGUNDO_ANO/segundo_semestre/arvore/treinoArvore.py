class NoArvore:
    def __init__(self, info):
        self.info = info
        self.esq = None
        self.dir = None

class Arvore:
    def __init__(self):
        self.raiz = None

    def montaArvore(self, x):
        if self.raiz == None:
            no = NoArvore(x)
            self.raiz = no
            return
        q=None
        p=self.raiz

        while p and p.info != x:
            q=p
            if x < p.info:
                p = p.esq
            else:
                p = p.dir
        if p:  ## se p for diferente de None é pq parou em um Nó que existe e não um vazio
            print(f'Informação já cadastrada')
            return
        p=NoArvore(x)
        if x < q.info:
            q.esq = p
        else:
            q.dir = p

        
    def preOrdem(self, p):
        if p:
            print(f'no visitado em preOrdem {p.info}')
            self.preOrdem(p.esq)
            self.preOrdem(p.dir)

    def emOrdem(self, p):
        if p:
            self.emOrdem(p.esq)
            print(f'no visitado em ordem {p.info}')
            self.emOrdem(p.dir)







arv=Arvore()

arv.montaArvore(50)
arv.montaArvore(30)
arv.montaArvore(82)


arv.preOrdem(arv.raiz)
print('\n')
arv.emOrdem(arv.raiz)