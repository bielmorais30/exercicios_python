# Exercícios de Programação – Árvore Binária
# 1. Escrever uma função recursiva em python para calcular a altura de uma árvore binária de busca.
# 2. Escrever uma função recursiva em python para verificar se duas arvores binárias de busca são iguais
# 3. Escreve uma função recursiva em python para transformar uma árvore binária em sua imagem especular.
# 4. Escrever uma função não recursiva em python para percorrer uma árvore binária de busca

class NoArvoreBinaria:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
        
    def montaArvore(self,x):

        if self.raiz == None:
            no=NoArvoreBinaria(x)
            self.raiz=no
            return
        q=None
        p=self.raiz
        while p and p.valor!=x:
            q=p
            if x<p.valor:
                p=p.esq
            else:
                p=p.dir
        if p:
            print(f'informacao ja cadastrada')
            return
        p=NoArvoreBinaria(x)
        if x < q.valor:
            q.esq = p
        else:
            q.dir = p
        
    def emOrdem(self, raiz):
        if raiz:
            self.emOrdem(raiz.esq)
            print(f'no visitado em emOrdem {raiz.valor}')
            self.emOrdem(raiz.dir)
    
    def espelhar(self, raiz):
        if raiz:
            raiz.esq, raiz.dir = raiz.dir, raiz.esq
            self.espelhar(raiz.esq)
            self.espelhar(raiz.dir)
        return
    
    def verificarIgualdade(self, raiz1, raiz2):
        
        if raiz1 is None and raiz2 is None:
            return True
        
        if raiz1 is None or raiz2 is None:
            return False
        
        if raiz1.valor != raiz2.valor:
            return False
        
        return (self.verificarIgualdade(raiz1.esq, raiz2.esq) and self.verificarIgualdade(raiz1.dir, raiz2.dir))
            
    def calcularAltura(self, raiz):
        if not raiz:
            return -1
        
        altura_esq = self.calcularAltura(raiz.esq)
        altura_dir = self.calcularAltura(raiz.dir)
        
        if altura_dir > altura_esq:
            return altura_dir + 1
        else: 
            return altura_esq + 1
           
            
arvore = ArvoreBinaria()

arvore.montaArvore(10)
arvore.montaArvore(5)
arvore.montaArvore(35)
arvore.montaArvore(20)

arvore2 = ArvoreBinaria()

arvore2.montaArvore(10)
arvore2.montaArvore(5)
arvore2.montaArvore(35)
arvore2.montaArvore(20)
arvore2.montaArvore(22)


print(arvore.verificarIgualdade(arvore.raiz, arvore2.raiz))

# arvore.emOrdem(arvore.raiz)
# arvore.espelhar(arvore.raiz)
# print("Espelhado:")
# arvore.emOrdem(arvore.raiz)

# print("Altura: ",arvore.calcularAltura(arvore.raiz))
 