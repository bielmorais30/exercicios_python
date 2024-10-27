## Atributos do NoArvoreCliente: ##
# - Código                          
# - Nome                          
# - Saldo           
# - esq
# - dir 
                

## ArvoreCliente ##
# Atributo:
# - Raiz                  
# Metodos:                      
# - incluirCliente     OK                       
# - excluirCliente                          
# - alterarCliente     OK         
# - buscarCliente      OK    
# - mostrarCliente     OK     

class NoArvoreCliente:
    
    def __init__(self, cod, nome, saldo):
        self.cod = cod
        self.nome = nome
        self.saldo = saldo
        self.esq = None
        self.dir = None

class ArvoreCliente:
    def __init__(self):
        self.raiz = None

    def incluirCliente(self, cod, nome, saldo):
        noCliente = NoArvoreCliente(cod, nome, saldo)
        if self.raiz == None:
            self.raiz = noCliente
            print("Cliente cadastrado com Successo!")
            return
        
        q = None
        p = self.raiz

        while p and p.cod != cod:  ## Vai andando até chegar ou no None correto ou no mesmo código
            q = p 

            if cod < p.cod:
                p = p.esq
            else:
                p = p.dir

        if p:
            print("\nCódigo de cliente já cadastrado!")
            return
        p = noCliente

        if q.cod > p.cod:
            q.esq = p
        else:
            q.dir = p

        print("\nCliente cadastrado com Successo!")

    def buscarCliente(self, cod):
        if self.raiz == None:
            print("A arvore de clientes está vazia!")
            return
        
        p = self.raiz
        while p and p.cod != cod:
            if cod < p.cod:
                p = p.esq
            else:
                p = p.dir
        
        if not p:
            print("\nCodigo de Cliente não encontrado!")
            return
        
        return p
    

    def alterarCliente(self, cod):
        noCliente = self.buscarCliente(cod)
        if not noCliente:
            return
        print("\nNome: ", noCliente.nome )
        noCliente.nome = input(f"Alterar: ")
        print("\nSaldo: ", noCliente.saldo )
        noCliente.saldo = input(f"Alterar: ")

        print("\n## Informações do cliente atualizadas! ## ")
        self.mostrarCliente(noCliente)


    def excluirCliente(self, cod):
        
        p = self.raiz
        q = None

        while p and p.cod != cod:
            q = p
            if cod > p.cod:
                p = p.dir
            else:
                p = p.esq

            # while vai parar com o p.cod = cod

        if not p:
            print("\nNão cadastrado!")
            return
        
        # V sucessor em ordem que vai subistituir o p

        if not p.esq:   # Se não tiver nó na esquerda
            v = p.dir
        elif not p.dir: # Se não tiver nó na direita
            v = p.esq
        else:           # Se tiver dois nós
            
            t = p     # t - pai do nó v
            v = p.dir # v sucessor em ordem que vai subistituir o p
            s = v.esq # s - filho esquerdo de v
            
            while s:   # enquanto o v tiver um sucessor
                t = v
                v = s
                s = s.esq  # ou v.esq

            if t != p:  # se o pai não for o nó a ser removido

                t.esq = v.dir  # atribui a esquerda do pai a direita do filho
                v.dir = p.dir  # pegando os atributos de p para subistituilo

            v.esq = p.esq      # como v.esq = None nesse ponto então basta pegar a esquerda de p para substituilo

        if not q:   # pai do nó p
            # p é a raiz da arvore
            self.raiz = v
        else:
            if p == q.esq:
                q.esq = v
            else:
                q.dir = v
                    
            
            p = None
        print("\nRemovido com sucesso!")





    def mostrarCliente(self, noCliente):
        if not noCliente:
            print("\nClinte inválido")
            return
        
        print(f"\nCliente:\n Cod: {noCliente.cod}\n Nome: {noCliente.nome}\n Saldo: {noCliente.saldo}")






minhaArvore = ArvoreCliente()

minhaArvore.incluirCliente(2, "Joao", 500)

minhaArvore.incluirCliente(1, "Gabriel", 1000)


minhaArvore.mostrarCliente(minhaArvore.buscarCliente(2))

minhaArvore.alterarCliente(2)

minhaArvore.excluirCliente(1)

minhaArvore.mostrarCliente(minhaArvore.buscarCliente(2))
minhaArvore.mostrarCliente(minhaArvore.buscarCliente(1))