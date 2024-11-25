# 1. Escreva uma função em python para retirar todos os elementos impares de uma árvore binária de busca.

# 2. Escreva uma função em python que retorne um vetor com os elementos menores que um dado valor N em uma árvore binária de busca.

# 3. Mostre que, se um nó em uma árvore binária de pesquisa tem dois filhos, então o seu sucessor não tem filho à esquerda e o seu predecessor não tem filho à direita.

class Arvore:
    def __init__(self):
        self.raiz = None

    def adicionarNo(self, x):
        no = NoArvore(x)

        if self.raiz == None:
            self.raiz = no
            print("======= Nó Adicionado com Sucesso! =======\n\n")
            return
        
        q = None
        p = self.raiz

        while p and p.valor != x:
            q = p
            if x > p.valor:
                p = p.dir
            else:
                p = p.esq

        if p:
            print("======= Erro: Valor Informado Já Se Encontra na Arvore  =======\n\n")
            return
        
        if no.valor > q.valor:
            q.dir = no
        else:
            q.esq = no

        print("======= Nó Adicionado com Sucesso! =======\n\n")

    def retirarNo(self, valor):
        p = self.raiz
        q = None

        while p and p.valor != valor:
            q=p

            if valor > p.valor:
                p = p.dir
            else: 
                p = p.esq

        if not p:
            print("======= Valor Informado Não Se Encontra Na Arvore! =======\n\n")
            return
        
        if not p.dir:
            v = p.esq
        elif not p.esq:
            v = p.dir
        else:

            t = p       # nó pai de v
            v = p.dir   # nó que vai entrar no lugar de p
            s = v.esq   # sucessor de v
        
            while s:
                t = v
                v = s
                s = v.esq
            
            if t != p:
                t.esq = v.dir
                v.dir = p.dir
            
            v.esq = p.esq

        if not q:
            self.raiz = v
        else:
            if p == q.esq:
                q.esq = v
            else:
                q.dir = v

        p = None
        print(f"======= ({valor})  Removido com sucesso! =======\n\n") 

    def preOrdem(self,p):
        if p:
            print(f'no visitado em preOrdem {p.valor}')
            self.preOrdem(p.esq)
            self.preOrdem(p.dir)

    def retirarImpares(self, raiz):
        
        if not raiz:
            return

        self.retirarImpares(raiz.esq)
        self.retirarImpares(raiz.dir)

        if raiz.valor % 2 != 0:
            self.retirarNo(raiz.valor)
        
    def menoresQue(self, raiz, n):

        if not raiz:
            return []
        vetor = []
        vetor += self.menoresQue(raiz.esq, n)
        vetor += self.menoresQue(raiz.dir, n)

        if raiz.valor < n:
            vetor.append(raiz.valor) 
        
        return vetor

class NoArvore:
    def __init__(self, valor):
        self.valor = valor
        self.dir = None
        self.esq = None


arvBin = Arvore()

arvBin.adicionarNo(30)
arvBin.adicionarNo(82)
arvBin.adicionarNo(45)
arvBin.adicionarNo(3)
arvBin.adicionarNo(20)
arvBin.adicionarNo(80)
arvBin.adicionarNo(15)
arvBin.adicionarNo(84)

# arvBin.retirarImpares(arvBin.raiz)

arvBin.preOrdem(arvBin.raiz)
# print("\n\n")
# arvBin.retirarNo(45)
# arvBin.preOrdem(arvBin.raiz)

print(arvBin.menoresQue(arvBin.raiz, 80))