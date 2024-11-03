## Atributos do NoArvoreCliente: ##
# - Código              OK            
# - Nome                OK          
# - Saldo               OK
# - esq                 OK
# - dir                 OK
                
class NoArvoreCliente:
    
    def __init__(self, cod, nome, saldo):
        self.cod = cod
        self.nome = nome
        self.saldo = saldo
        self.esq = None
        self.dir = None

## NoArvoreProduto ##
## Atributos:
# - Código              OK
# - Nome                OK
# - PrecoUnitário       OK
# - QuantidadeEmEstoque OK
# - esq                 OK
# - dir                 OK

class NoArvoreProduto:
    def __init__(self, codigo,nome,precoUnitario,quantidadeEmEstoque):
        self.codigo=codigo
        self.nome=nome
        self.precoUnitario= precoUnitario
        self.quantidadeEmEstoque= quantidadeEmEstoque
        self.esq=None
        self.dir=None

## NoArvorePedido ##
## Atributos:
# - códigoPedido        OK
# - dataPedido          OK
# - códigoDoCliente     OK
# - situacaoPedido      OK
# - itemPedido                                      OK
# - esq                 OK
# - dir                 OK
# ‘A’ – Aberto, ‘F’ – Fechado e ‘C’ – Cancelado.


class NoArvorePedido:
    def __init__(self, codigoPedido, dataPedido, codigoDoCliente):
        self.codigoPedido = codigoPedido
        self.dataPedido = dataPedido
        self.codigoDoCliente = codigoDoCliente
        self.situacaoPedido = "A"
        self.itensDePedido = ArvoreItemPedido()
        self.esq = None
        self.dir = None


## ArvoreCliente ##
# Atributo:
# - Raiz                  
# Metodos:                      
# - incluirCliente     OK                       
# - excluirCliente     OK                     
# - alterarCliente     OK         
# - buscarCliente      OK    
# - mostrarCliente     OK     

class ArvoreCliente:
    def __init__(self):
        self.raiz = None

    def incluirCliente(self, cod, nome, saldo):
        print('+' + '-' * (15) + '+')
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
            print('+' + '-' * (15) + '+')
            print("Código de cliente já cadastrado!")
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
        print('+' + '-' * (15) + '+')
        noCliente = self.buscarCliente(cod)
        if not noCliente:
            return
        print("\nNome: ", noCliente.nome )
        noCliente.nome = input(f"Alterar: ")
        print("\nSaldo: ", noCliente.saldo )
        noCliente.saldo = int(input(f"Alterar: "))

        print("\n## Informações do cliente atualizadas! ## ")
        self.mostrarCliente(noCliente)


    def excluirCliente(self, cod, pedidos):
        print('+' + '-' * (15) + '+')
        
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
        
        if pedidos.buscarClienteAssociado(p.cod) > 0:
            print("Erro na exclusão: Cliente com pedido associado!")
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
        
        print(f"\n|Cliente:\n|Cod: {noCliente.cod}\n|Nome: {noCliente.nome}\n|Saldo: {noCliente.saldo}")



## ArvoreProduto ##
# - Raiz                  
# Metodos:                      
# - incluirProduto        OK                  
# - excluirProduto -                                 --Alterar--
#           Só pode ser excluido caso não tenha nenhum itemDePedido associado ao produto
# - alterarProduto        OK     
# - buscarProduto         OK
# - mostrarProduto        OK

class ArvoreProduto:
    def __init__(self):
        self.raiz = None

    def incluirProduto(self, codigo, nome, precoUnitario, quantidadeEmEstoque):
        print('+' + '-' * (15) + '+')
        noProduto = NoArvoreProduto(codigo, nome, precoUnitario, quantidadeEmEstoque)

        if not self.raiz:
            self.raiz = noProduto
            print("Produto cadastrado com sucesso")
            return
        
        p = self.raiz
        q = None

        while p and p.codigo != noProduto.codigo:
            q = p
            if noProduto.codigo < p.codigo:
                p = p.esq
            else:
                p = p.dir
        
        if p: 
            print('+' + '-' * (15) + '+')
            print("Código de produto já cadastrado!")
            return
        
        if q.codigo > noProduto.codigo:
            q.esq = noProduto
        else: 
            q.dir = noProduto

        print("Produto cadastrado com sucesso")

    def buscarProduto(self, codigoProduto):

        if not self.raiz:
            print("\nArvore Produtos está vazia!")
            return

        p = self.raiz

        while p and p.codigo != codigoProduto:
            if codigoProduto < p.codigo:
                p = p.esq
            else:
                p = p.dir
        
        if not p:
            print('+' + '-' * (15) + '+')
            print("Código de produto não encontrado!")
            print('+' + '-' * (15) + '+')
            return
    
        return p    


    def mostrarProduto(self, produto):
        print('+' + '-' * (15) + '+')
        if produto:
            print(f'\nProduto:\n Código: {produto.codigo}\n Nome: {produto.nome}\n Preço: {produto.precoUnitario}\n Quantidade Em Estoque: {produto.quantidadeEmEstoque}')
            return
        
        print("\nProduto inválido!")


    def alterarProduto(self, codProduto):
        print('+' + '-' * (15) + '+')
        produto = self.buscarProduto(codProduto)
        if produto:
            print(f"\nNome: {produto.nome}")
            produto.nome = input("Alterar: ")

            print(f"\nPreço: {produto.precoUnitario}")
            produto.precoUnitario = int(input("Alterar: "))

            print(f"\nQuantidade: {produto.quantidadeEmEstoque}")
            produto.quantidadeEmEstoque = int(input("Alterar: "))

            print("\n## Informações do produto atualizadas! ## ")

            return self.mostrarProduto(produto)
    
    def excluirProduto(self, codigo):
        print('+' + '-' * (15) + '+')
        p = self.raiz
        q = None

        while p and p.codigo != codigo:
            q = p
            if codigo < p.codigo:
                p = p.esq
            else:
                p = p.dir

        if not p:
            print("\nProduto não encontrado!")
            return
        
        if not p.dir:
            v = p.esq
        elif not p.esq:
            v = p.dir
        else:

            t = p # nó pai de v
            v = p.dir   # no que vai entrar no lugar de p
            s = v.esq # sucessor de v


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
        print("\nRemovido com sucesso!")

## ArvorePedido ##
# - Raiz                  
# Metodos:                      
# - incluirPedido                OK
# - excluirPedido                                   OK
#           se existir itens de pedido associado ao pedido, as quantidades, de cada produto deve voltar para o estoque
# - alterarPedido                                   OK  
#           Se pedido fechado ou cancelado, arvore de item de pedido não poderá passar por manutenção.
# - fecharPedido                                --Alterar--
#           Um pedido só pode ser fechado se o mesmo possuir pelo menos um item de pedido associado
#           mostrar todos itens de pedido com o total de cada item e também apresentar o total geral de todos os itens.
# - cancelarPedido                                  OK
#           se existir itens de pedido associado ao pedido, as quantidades, de cada produto deve voltar para o estoque

# Criar metodos na ArvorePedidos para chamar os seguintes metodos da classse ArvoreItemDePedido
#  Assim, para incluir um item de pedido, deve-se informar para qual pedido o item vai ser incluído

#  incluir item de pedido (self, codigoPedido)    OK
#  excluir item de pedido           OK
#  alterar item de pedido           OK            
#  buscar item de pedido            OK
#  mostrar item de pedido.          OK  


# - buscarPedido                 OK
# - mostrarPedido                OK
# - mostrarDetalhesPedido                           NOVO
# - mostrarPedidosEmAberto                           NOVO 
#               Para cada pedido selecionado, mostrar os detalhes do pedido.
# - mostrarPedidosPorProduto                           NOVO 
#               Mostrar em quais pedidos está associado um determinado produto.
# - totalizarTudo                           NOVO 
#               Totalizar separadamente a quantidade de pedidos abertos, a quantidade de pedidos fechados e a quantidade de pedidos cancelados.


# ‘A’ – Aberto, ‘F’ – Fechado e ‘C’ – Cancelado.
# Um pedido só pode ser excluído se estiver com a situação do pedido igual a ‘F’ ou igual a ‘C’.
# Um pedido só pode ser alterado se estiver com a situação do pedido igual a ‘A’.

class ArvorePedido:
    def __init__(self):
        self.raiz = None

    def incluirItemDePedido(self, codigoDoPedido, codigoProduto, quantidade, preco, arvoreProduto):
        pedido = self.buscarPedido(codigoDoPedido)
        if pedido.situacaoPedido == "F"  or pedido.situacaoPedido == "C":
            print('+' + '-' * (15) + '+')
            print("Erro, pedido fechado ou cancelado!")
            return
        pedido.itensDePedido.incluirItemDePedido(codigoProduto, quantidade, preco, arvoreProduto)

    def excluirItemDePedido(self, codigoDoPedido, codigoProduto, arvoreProduto):
        pedido = self.buscarPedido(codigoDoPedido)
        if pedido.situacaoPedido == "F"  or pedido.situacaoPedido == "C":
            print('+' + '-' * (15) + '+')
            print("Erro, pedido fechado ou cancelado!")
            return
        if not pedido.itensDePedido.raiz:
            print("Arvore Item De Pedidos está vazia!")

        pedido.itensDePedido.excluirItemDePedido(codigoProduto, arvoreProduto)


    def alterarItemDePedido(self, codigoDoPedido, codProduto, arvoreProduto):
        pedido = self.buscarPedido(codigoDoPedido)
        if pedido.situacaoPedido == "F"  or pedido.situacaoPedido == "C":
            print('+' + '-' * (15) + '+')
            print("Erro, pedido fechado ou cancelado!")
            return
        pedido.itensDePedido.alterarItemDePedido(codProduto, arvoreProduto)

    def buscarItemDePedido(self, codigoDoPedido, codigoProduto):
        pedido = self.buscarPedido(codigoDoPedido)
        if pedido.situacaoPedido == "F"  or pedido.situacaoPedido == "C":
            print('+' + '-' * (15) + '+')
            print("Erro, pedido fechado ou cancelado!")
            return
        pedido.itensDePedido.buscarItemDePedido(codigoProduto)

    def mostrarItemDePedido(self, codigoDoPedido, itemDePedido):
        pedido = self.buscarPedido(codigoDoPedido)
        if pedido.situacaoPedido == "F"  or pedido.situacaoPedido == "C":
            print('+' + '-' * (15) + '+')
            print("Erro, pedido fechado ou cancelado!")
            return
        pedido.itensDePedido.mostrarItemDePedido(itemDePedido)

                            ######

    def incluirPedido(self, codigoPedido, dataPedido, codigoDoCliente, arvoreClientes):
        print('+' + '-' * (15) + '+')
        if not arvoreClientes.buscarCliente(codigoDoCliente):
            print("O codigo de cliente informado não existe!")
            return 
        
        noPedido = NoArvorePedido(codigoPedido, dataPedido, codigoDoCliente)
        
        if not self.raiz:
            self.raiz = noPedido
            print("\nPedido adicionado com sucesso!")
            return

        p = self.raiz
        q = None

        while p and p.codigoPedido != noPedido.codigoPedido:
            q = p
            if noPedido.codigoPedido < p.codigoPedido:
                p = p.esq
            else:
                p = p.dir

        if p:
            print('+' + '-' * (15) + '+')
            print("Código de pedido já em uso!")
            return

        if noPedido.codigoPedido < q.codigoPedido:
            q.esq = noPedido
        else:
            q.dir = noPedido

        print("\nPedido adicionado com sucesso!")



    def buscarPedido(self, codigoPedido):
        if not self.raiz:
            print("\nArvore Pedido está vazia!")
            return

        p = self.raiz

        while p and p.codigoPedido != codigoPedido:
            if codigoPedido < p.codigoPedido:
                p = p.esq
            else:
                p = p.dir
        
        if not p:
            print('+' + '-' * (15) + '+')
            print("Código de pedido não encontrado!")
            return
    
        return p    


    def mostrarPedido(self, pedido, clientes = None):
        print('+' + '-' * (15) + '+')
        if pedido and clientes:
            print(f'Pedido {pedido.codigoDoCliente}:')
            clientes.mostrarCliente(clientes.buscarCliente(pedido.codigoDoCliente))
            print(f'Código Pedido: {pedido.codigoPedido}\nData: {pedido.dataPedido}\nSituação: {pedido.situacaoPedido}')
            return
        elif pedido:
            print(f'Pedido {pedido.codigoDoCliente}:\nCod Cliente: {pedido.codigoDoCliente}\nCódigo Pedido: {pedido.codigoPedido}\nData: {pedido.dataPedido}\nSituação: {pedido.situacaoPedido}')
            return
        print("Pedido inválido!")



    def alterarPedido(self, codPedido, clientes):
        print('\n+' + '-' * (15) + '+')
        pedido = self.buscarPedido(codPedido)

        if not pedido:
            print("Pedido não encontrado!\n")
            return
        
        if pedido.situacaoPedido != "A":
            print("O pedido não pode ser alterado!")
            print(f"Situação do pedido: {pedido.situacaoPedido}\n")
            return

        print(f"\nCodigo cliente: {pedido.codigoDoCliente}")
        codAux = int(input("Alterar: "))

        if not clientes.buscarCliente(codAux):
            return

        pedido.codigoDoCliente = codAux

        print(f"\nData: {pedido.dataPedido}")
        pedido.dataPedido = input("Alterar: ")

        print(f"\nSituação: {pedido.situacaoPedido}")
        pedido.situacaoPedido = input("Alterar: ")

        print("\n## Informações do pedido atualizadas! ## \n")

        return self.mostrarPedido(pedido) 

    def fecharPedido(self, codPedido):
        pedido = self.buscarPedido(codPedido)

        if pedido and pedido.itensDePedido.raiz:
            print('\n+' + '-' * (15) + '+')
            pedido.situacaoPedido = "F"    
            print("Situação de pedido alterad com sucesso\n'F' - Fechado")  
            pedido.itensDePedido.mostrarTodosItensDePedido(pedido.itensDePedido.raiz)
            print(f"\n\nTotal dos itens: {pedido.itensDePedido.totalDeTodosItensDePedido(pedido.itensDePedido.raiz)}")    
            return
        else:
            print("Erro ao fechar pedido: nenhum item de pedido cadastrado!")

        
    def cancelarPedido(self, codPedido, arvoreProduto):
        pedido = self.buscarPedido(codPedido)

        if pedido:
            print('\n+' + '-' * (15) + '+')
            pedido.situacaoPedido = "C"    
            pedido.itensDePedido.excluirTodosItensDePedido(pedido.itensDePedido, arvoreProduto)
            print("Situação de pedido alterad com sucesso\n'C' - Cancelado")      
            return


    def buscarClienteAssociado(self, codCliente,raiz=None):
        # Se o retorno for > 0 então o codigo de cliente fornecido está vinculado
        if raiz== None:
            raiz = self.raiz
        
        if not raiz:
            return  0
        if raiz.codigoDoCliente == codCliente:
            if not raiz.esq and not raiz.dir:
                return 1
            elif raiz.dir and raiz.esq:
                return (1 + self.buscarClienteAssociado(codCliente, raiz.dir) +  self.buscarClienteAssociado(codCliente, raiz.esq))
            elif raiz.dir:
                return (1 + self.buscarClienteAssociado(codCliente, raiz.dir))
            else:
                return (1 + self.buscarClienteAssociado(codCliente, raiz.esq))
        else:
            if not raiz.esq and not raiz.dir:
                return 0    
            elif raiz.dir and raiz.esq:
                return (0 + self.buscarClienteAssociado(codCliente, raiz.dir) +  self.buscarClienteAssociado(codCliente, raiz.esq))
            elif raiz.dir:
                return (0 + self.buscarClienteAssociado(codCliente, raiz.dir))
            else:
                return (0 + self.buscarClienteAssociado(codCliente, raiz.esq))
    
    def excluirPedido(self, codigoPedido, arvoreProduto):
        print('+' + '-' * (15) + '+')
        
        p = self.raiz
        q = None

        while p and p.codigoPedido != codigoPedido:
            q = p
            if codigoPedido > p.codigoPedido:
                p = p.dir
            else:
                p = p.esq

            # while vai parar com o p.codigoPedido = codigoPedido

        if not p:
            print("\nNão cadastrado!")
            return
        
        if p.situacaoPedido == "A":
            print("Erro ao excluir pedido: situação do pedido em aberto")
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
                    
            p.itensDePedido.excluirTodositensDePedido(p.itensDePedido.raiz, arvoreProduto)
            p = None
        print("\nRemovido com sucesso!")

class NoArvoreItemPedido:
    def __init__(self, codigoProduto, quantidade, preco):
        self.codigoProduto = codigoProduto
        self.quantidade = quantidade
        self.preco = preco
        self.esq = None
        self.dir = None



class ArvoreItemPedido:
#  incluir item de pedido - OK
#           O produto do item deve ter sido cadastrado préviamente na arvore de produtos
#           Checar a quantidade do item do pedido. naoCadastrado if quantidadeItemProduto > quantidadeNoEstoque 
#           Se itemPedido incluido com sucesso então atualizar estoque do produto estoque = estoque - quantidade 

#  excluir item de pedido - OK
#           Quando excluido, a quantidade do produto deve retornar ao estoque do produto     
#        
#  alterar item de pedido - OK
#           Quando a quantidade for alterada, atualizar o estoque do produto tanto pra mais ou para menos

#  buscar item de pedido    OK
#  mostrar item de pedido.  OK
    def __init__(self):
        self.raiz = None

    def incluirItemDePedido(self, codigoProduto, quantidade, preco, arvoreProduto):
        print('+' + '-' * (15) + '+')
        itemDePedido = NoArvoreItemPedido(codigoProduto, quantidade, preco)

        produto = arvoreProduto.buscarProduto(codigoProduto)


        if not produto:
            print("Codigo de Produto Inválido!")
            return 
        
        if produto.quantidadeEmEstoque < quantidade:
            print("Quantidade excede o estoque do produto!")
            return
            
        

        if not self.raiz:
            self.raiz = itemDePedido
            print("Item de pedido incluido com sucesso")
            produto.quantidadeEmEstoque = produto.quantidadeEmEstoque - quantidade
            return
        
        p = self.raiz
        q = None

        while p and p.codigoProduto != itemDePedido.codigoProduto:
            q = p
            if itemDePedido.codigoProduto < p.codigoProduto:
                p = p.esq
            else:
                p = p.dir
        
        if p: 
            print('+' + '-' * (15) + '+')
            print("Código do Item De Pedido já cadastrado!")
            return

        if q.codigoProduto > itemDePedido.codigoProduto:
            q.esq = itemDePedido
        else: 
            q.dir = itemDePedido

        produto.quantidadeEmEstoque = produto.quantidadeEmEstoque - quantidade
        print("Item de Pedido cadastrado com sucesso!")

    

    def excluirItemDePedido(self, codigoProduto, arvoreProduto):
        print('+' + '-' * (15) + '+')
        produto = arvoreProduto.buscarProduto(codigoProduto)
        p = self.raiz
        q = None

        while p and p.codigoProduto != codigoProduto:
            q = p
            if codigoProduto < p.codigoProduto:
                p = p.esq
            else:
                p = p.dir

        if not p:
            print("\nItem de pedido não encontrado!")
            return
        
        if not p.dir:
            v = p.esq
        elif not p.esq:
            v = p.dir
        else:

            t = p # nó pai de v
            v = p.dir   # no que vai entrar no lugar de p
            s = v.esq # sucessor de v


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

        produto.quantidadeEmEstoque = produto.quantidadeEmEstoque + p.quantidade
        p = None
        
        
        print("\nRemovido com sucesso!")

    
    def buscarItemDePedido(self, codigoProduto):
        if not self.raiz:
            print("\nArvore Item Pedido está vazia!")
            return

        p = self.raiz

        while p and p.codigoProduto != codigoProduto:
            if codigoProduto < p.codigoProduto:
                p = p.esq
            else:
                p = p.dir
        
        if not p:
            print('+' + '-' * (15) + '+')
            print("Item de pedido não encontrado!")
            return
    
        return p    

    def mostrarItemDePedido(self, itemDePedido):
        print('+' + '-' * (15) + '+')
        if itemDePedido:
            print(f'\nItem De Pedido:\n Código Produto: {itemDePedido.codigoProduto}\n Quantidade: {itemDePedido.quantidade}\n Preço: {itemDePedido.preco}')
            return
        
        print("\nItem De Pedido inválido!")


    def alterarItemDePedido(self, codProduto, arvoreProduto):
        print('+' + '-' * (15) + '+')
        produto = arvoreProduto.buscarProduto(codProduto)
        itemPedido = self.buscarItemDePedido(codProduto)
        if itemPedido:
            print(f"\nCodigo do Produto: {itemPedido.codigoProduto}")
            
            produto.quantidadeEmEstoque += itemPedido.quantidade
            while True:
                print(f"\nEstoque: {produto.quantidadeEmEstoque}")
                
                auxQnt = int(input("Alterar: "))
                if auxQnt > produto.quantidadeEmEstoque:
                    print("\nQuantidade ultrapassa o estoque do item!")
                    continue
                else:
                    itemPedido.quantidade = auxQnt
                    produto.quantidadeEmEstoque = produto.quantidadeEmEstoque - itemPedido.quantidade
                    break
            print(f"\nPreço: {itemPedido.preco}")
            itemPedido.preco = int(input("Alterar: "))

            print("\n## Informações do Item de Pedido atualizadas! ## ")

            return self.mostrarItemDePedido(itemPedido)

    def excluirTodosItensDePedido(self, raiz, arvoreProduto):
        if not raiz:
            return
        
        produto = arvoreProduto.buscarProduto(raiz.codProduto)
        produto.estoque += raiz.quantidadeEmEstoque

        self.excluirItemDePedido(raiz.esq, arvoreProduto)
        self.excluirItemDePedido(raiz.dir, arvoreProduto)
        raiz = None


    def mostrarTodosItensDePedido(self,raiz):
        # mostrar todos itens de pedido com o total de cada item e também apresentar o total geral de todos os itens.
        if raiz:
            self.mostrarItemDePedido(raiz)
            print(f"Total: {raiz.quantidade * raiz.preco}")
            if raiz:
                self.mostrarTodosItensDePedido(raiz.esq)
                self.mostrarTodosItensDePedido(raiz.dir)
                
    def totalDeTodosItensDePedido(self, raiz):
        if raiz:
            return raiz.quantidade * raiz.preco + self.totalDeTodosItensDePedido(raiz.esq) + self.totalDeTodosItensDePedido(raiz.dir)
        return 0
arvoreDeCLientes = ArvoreCliente()

arvoreDeCLientes.incluirCliente(5, "Joao", 500)

# arvoreDeCLientes.incluirCliente(2, "Gabriel", 1000)
# arvoreDeCLientes.incluirCliente(3, "Bryan", 0)


# arvoreDeCLientes.mostrarCliente(arvoreDeCLientes.buscarCliente(2))

# arvoreDeCLientes.alterarCliente(2)

# arvoreDeCLientes.excluirCliente(1)

# arvoreDeCLientes.mostrarCliente(arvoreDeCLientes.buscarCliente(2))
# arvoreDeCLientes.mostrarCliente(arvoreDeCLientes.buscarCliente(1))

produtos = ArvoreProduto()

produtos.incluirProduto(1, "Produto1", 10, 2)
produtos.incluirProduto(2, "Produto2", 20, 4)
produtos.incluirProduto(3, "Produto3", 30, 7)

produtos.mostrarProduto(produtos.buscarProduto(3))

# produtos.alterarProduto(2)
# produtos.excluirProduto(2)

# produtos.mostrarProduto(produtos.buscarProduto(2))

pedidos = ArvorePedido()

pedidos.incluirPedido(3, "25/10/2024", 5, arvoreDeCLientes)
# pedidos.incluirPedido(2, "25/10/2024", 2, arvoreDeCLientes)
# pedidos.incluirPedido(4, "25/10/2024", 2, arvoreDeCLientes)
# pedidos.incluirPedido(5, "25/10/2024", 2, arvoreDeCLientes)

# pedidos.mostrarPedido(pedidos.buscarPedido(2))
# pedidos.alterarPedido(2, arvoreDeCLientes)
# pedidos.cancelarPedido(3)
# pedidos.alterarPedido(3, arvoreDeCLientes)
# pedidos.mostrarPedido(pedidos.buscarPedido(2), arvoreDeCLientes)
# input()
# print(pedidos.buscarClienteAssociado(2))
# arvoreDeCLientes.excluirCliente(2, pedidos)
# pedidos.alterarPedido(2, arvoreDeCLientes)
# pedidos.excluirPedido(2)

# ItemsDePedidos = ArvoreItemPedido()

pedidos.incluirItemDePedido(3, 1, 7, 10, produtos)
pedidos.incluirItemDePedido(3, 2, 10, 11, produtos)

produtos.mostrarProduto(produtos.buscarProduto(1))

# pedidos.excluirItemDePedido(3, 1, produtos)
produtos.mostrarProduto(produtos.buscarProduto(2))
pedidos.incluirItemDePedido(3, 2, 3, 10, produtos)
pedidos.incluirItemDePedido(3, 3, 1, 20, produtos)
pedidos.mostrarItemDePedido(3, pedidos.buscarItemDePedido(3, 2))
pedidos.alterarPedido(3, arvoreDeCLientes)
pedidos.alterarItemDePedido(3, 2, produtos)

produtos.mostrarProduto(produtos.buscarProduto(2))
# pedidos.raiz.itensDePedido.mostrarTodosItensDePedido(pedidos.raiz.itensDePedido.raiz)
# print(pedidos.raiz.itensDePedido.totalDeTodosItensDePedido(pedidos.raiz.itensDePedido.raiz))
pedidos.fecharPedido(3)

