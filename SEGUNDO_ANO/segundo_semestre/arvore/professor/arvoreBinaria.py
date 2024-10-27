
# rotinas para pilhas

def push(p, v):  # p representa o repositorio-lista e v o valor a ser inserido
    p.append(v)


def pop(p):
    return p.pop()


def vazia(p):
    return False if p else True



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

    def removeNo(self,x):
        # p - contem a referencia para o nó a ser retirado
        # q - pai do nó p
        # v - nó que vai substituir p
        # t - pai do nó v
        # s - filho esquerdo de v
        p = self.raiz
        q = None
        while p and p.info != x:
            q = p
            if x < p.info:
                p = p.esq
            else:
                p = p.dir

        if not p:
            print(f'nao cadastrado')
            return

        # posionar o ponteiro v no nó que irá substitui p

        if not p.esq:
            v = p.dir
        elif not p.dir:
            v = p.esq
        else:
            # p possui 2 subarvores. Posicionar v nosucessor emOrdem
            # de p ( nó mais a esquerda da subarvore direita) e
            # t no pai de v
            t = p
            v = p.dir
            s = v.esq
            while s:
                t = v
                v = s
                s = v.esq

            # nesse ponto v esta no sucessor emOrdem de p
            if t!=p:
                # p não é o pai de e v esta a esquerda de t
                t.esq=v.dir
                # remove o nó v de sua posição atual e
                # coloca no lugar do nó p
                v.dir=p.dir
            v.esq=p.esq

            if not q:
                # p é a raiz da arvore
                self.raiz = v
            else :
                if p == q.esq:
                    q.esq=v
                else:
                    q.dir=v

            p = None



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


    def mostraInfoNivel(self, p, nivel):
      if p!=None:
        print(f'valor: {p.info}  nivel: {nivel}')
        self.mostraInfoNivel(p.esq,nivel+1)
        self.mostraInfoNivel(p.dir,nivel+1)






    def mostraNosMesmoNivel(self, p, nivel):
      if p!=None:
          if nivel==0:
            print(f'valor: {p.info}')
          else:
            self.mostraNosMesmoNivel(p.esq,nivel-1)
            self.mostraNosMesmoNivel(p.dir,nivel-1)

    def percurso1NaoRecursivo(self,p):
        aux=[]
        push(aux,p)
        while not vazia(aux):
            no=pop(aux)
            print(f'Valor: {no.info}')
            if no.dir!=None:
                push(aux,no.dir)
            if no.esq!=None:
                push(aux, no.esq)



    def percurso2NaoRecursivo(self,p):
        aux=[]
        no=p
        while not vazia(aux) or no:
            while no:
                push(aux,no)
                no = no.esq

            no=pop(aux)
            print(f'Valor: {no.info}')
            no = no.dir




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

print('\n Nao recursivo 1')
arv.percurso1NaoRecursivo(arv.raiz)

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

arv.removeNo(50)

print('\nPercurso apos a remoção')

arv.preOrdem(arv.raiz)
print('\n')
arv.emOrdem(arv.raiz)
print('\n')
arv.posOrdem(arv.raiz)



arv=Arvore()

arv.montaArvore(80)
arv.montaArvore(50)
arv.montaArvore(20)
arv.montaArvore(65)
arv.montaArvore(120)
arv.montaArvore(35)
arv.montaArvore(30)
