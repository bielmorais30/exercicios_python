class Cliente:
    def __init__(self, cpf, nome, data_nasc, sexo):
        self.cpf = cpf
        self.nome = nome
        self.data_nasc = data_nasc
        self.sexo = sexo

class Produto:
    def __init__(self, idProduto, nome, valor):
        self.idProduto = idProduto
        self.nome = nome
        self.valor = valor


class ItemPedido:
    def __init__(self, numeroPedido, produto, quantidade, status):
        self.numeroPedido = numeroPedido
        self.produto = produto
        self.quantidade = quantidade
        self.status = status

class Pedido:
    def __init__(self, cliente):
        self.itens = ListaLigada()
        self.cliente = cliente
        # numeroPedido, cliente, status_pedido, itens):
        # self.numeroPedido = numeroPedido
        # self.cliente = cliente
        # self.status_pedido = status_pedido
        # self.itens = itens

        ## Criar função para adicionar pedidos

    def adicionarItemPedido(self, itemPedid):
        self.itens.insereOrdenadoNmrPedido(itemPedid)

    def mostrarItens(self):
        atual = self.itens.inicio
        while atual:
            print("----------------------------------")
            print(f'Numero Pedido: {atual.pedido.numeroPedido}')
            print(f'Status: {atual.pedido.status}')
            print(f'Quantidade: {atual.pedido.quantidade}')
            print("Produto:")
            print(f'L____ Id Produto: {atual.pedido.produto.idProduto}')
            print(f'L____ Produto Nome: {atual.pedido.produto.nome}')
            print(f'L____ Preço: R${atual.pedido.produto.valor}')
            
            print(f"\nValor do Item: R${atual.pedido.produto.valor*atual.pedido.quantidade}")
            atual = atual.proximo
    
    def excluirItemPedido(self, numeroPedido):
        self.itens.excluirPedido(numeroPedido)





class ListaNo:

    def __init__(self, pedido):
        self.pedido = pedido
        self.proximo = None


class ListaLigada:

    def __init__(self):
        self.inicio = None

    def insereInicio(self, pedido):
        no = ListaNo(pedido)
        no.proximo = self.inicio
        self.inicio = no

    def insereDepois(self, p, pedido):
        no = ListaNo(pedido)
        no.proximo = p.proximo
        p.proximo = no

    def excluirPedido(self, numeroPedido):
        atual = self.inicio
        if atual == None:
            return print(f"+++++++++++EXCLUSÂO+++++++++++++\nErro, não há pedidos na lista!\n++++++++++++++++++++++++++++++++")
        if atual.pedido.numeroPedido == numeroPedido:
            self.inicio = atual.proximo
            return print(f"Pedido: {atual.pedido.numeroPedido} - {atual.pedido.produto.nome}  x  {atual.pedido.quantidade}\nExcluido com sucesso!")
        anterior = atual
        atual = atual.proximo
        while atual:
            if atual.pedido.numeroPedido == numeroPedido:
                anterior.proximo = atual.proximo
                return print(f"+++++++++++EXCLUSÂO+++++++++++++\nPedido: {atual.pedido.numeroPedido} - {atual.pedido.produto.nome}  x  {atual.pedido.quantidade}\nExcluido com sucesso!\n++++++++++++++++++++++++++++++++")
            else:
                anterior = atual
                atual = atual.proximo
        print("+++++++++++EXCLUSÂO+++++++++++++")        
        print("Numero do pedido Inválido")
        print("++++++++++++++++++++++++++++++++") 


        


    def mostraLista(self):
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

    def insereOrdenadoNmrPedido(self, x):
        atual = self.inicio
        if not atual or x.numeroPedido < atual.pedido.numeroPedido:
            self.insereInicio(x) ####### 
            return
        proxi = atual
        while proxi and proxi.pedido.numeroPedido < x.numeroPedido:
            atual = proxi ### mudei o inicio para atual
            proxi = proxi.proximo

        if not proxi or proxi.pedido.numeroPedido > x.numeroPedido:
            self.insereDepois(atual, x)  ##### 
        else:
            print("\n Elemento anteriormente cadastrado!")
    

cli1 = Cliente(1234, "Gabriel", "30/04/2005", "Masculino")
cli2 = Cliente(4321, "Diogo", "15/04/2004", "Travequinho")

# pz = Pedido(1, cli1, "A caminho")
# p2 = Pedido(2, cli2, "A caminho")
# p3 = Pedido(3, cli2, "Empacotando")
# p4 = Pedido(4, cli1, "Aguardando Pagamento")

banana = Produto(100, "banana", 10)
melancia = Produto(101, "melancia", 20)
uva = Produto(102, "uva", 15)

item1 = ItemPedido(1, banana, 5, "A caminho")
item2 = ItemPedido(2, uva, 2, "Preparando")
item3 = ItemPedido(3, melancia, 1, "Aguardando Pagamento")

pedido1 = Pedido(cli1)

pedido1.adicionarItemPedido(item2)
pedido1.adicionarItemPedido(item3)
pedido1.adicionarItemPedido(item1)

pedido1.mostrarItens()

pedido1.excluirItemPedido(3)

pedido1.mostrarItens()

# lista = ListaLigada()
# lista.insereOrdenadoNmrPedido(p4)
# lista.insereOrdenadoNmrPedido(p2)
# lista.insereOrdenadoNmrPedido(p1)
# lista.insereOrdenadoNmrPedido(p3)

# lista.mostraLista()