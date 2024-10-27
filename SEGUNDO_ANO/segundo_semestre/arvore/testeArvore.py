class NoArvore:
    
    def __init__(self, info):
        self.info=info
        self.esq=None
        self.dir=None
        
class Arvore:
    
    def __init__(self):
        self.raiz=None
    
    
    def montarArvore(self,x):
        
        if self.raiz == None:
            no = NoArvore(x)
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
            print(f'informação ja cadastrada!')
            return
        p=NoArvore(x)
        if x < q.info:
            q.esq = p
        else:
            q.dir = p
                  
            