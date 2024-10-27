class Memoria:
    def __init__(self):
        self.clientes = []
        self.produtos = []
        self.pedidos = []

    def clientesIsNull(self):
        if len(self.clientes) == 0:
            return True
        else:
            False

    def produtosIsNull(self):
        if len(self.produtos) == 0:
            return  True
        else:
            False

    def pedidosIsNull(self):
        if len(self.clientes) == 0:
            return  True
        else:
            False

    def mostrarClientesMemoria(self):
        if len(self.clientes) == 0:
           return print("\n--------------------------------------------\nNenhum Cliente Cadastrado Na Memória!\n--------------------------------------------")
         
        id_falso = 1
        for cli in self.clientes:
            print("--------------------------------------------")
            print(f"Cliente {id_falso}:")
            print(f"CPF: {cli.cpf}")
            print(f"Nome: {cli.nome}")
            print(f"Nascimento: {cli.data_nasc}")
            print(f"Sexo: {cli.sexo}")
            print("--------------------------------------------\n")
            id_falso += 1

    def mostrarProdutosMemoria(self):
        if len(self.produtos) == 0:
           return print("\n--------------------------------------------\nNenhum Produto Cadastrado Na Memória!\n--------------------------------------------\n")
            
        for produto in self.produtos:
            print("--------------------------------------------")
            print(f"ID: {produto.idProduto}")
            print(f"Nome: {produto.nome}")
            print(f"Valor: {produto.valor}")
            print("--------------------------------------------\n")


    def mostrarPedidosMemoria(self):
        if len(self.pedidos) == 0:
           return print("\n--------------------------------------------\nNenhum Pedido Cadastrado Na Memória!\n--------------------------------------------\n")
            
        for pedido in self.pedidos:
            print("============================================")
            print("============================================")
            print(f"Cod Do Pedido: {pedido.codPedido}")
            print(f"Cliente: {pedido.cliente.nome}")
            print(f"Itens:  ")
            pedido.mostrarItens()
            print("============================================")
            print("============================================\n")

    def retornarCliente(self, cpf_cliente):
        achou = False
        # if len(self.clientes) == 0:
        #    return print("\n--------------------------------------------\nNenhum Cliente Cadastrado Na Memória!\n--------------------------------------------")
        for cli in self.clientes:
            ##retornar cliente com o id
            if cli.cpf == cpf_cliente:
                achou = True
                return cli
                
        # if not achou:
        #     return print("\n--------------------------------------------\nCPF Não Cadastrado!\n--------------------------------------------")
    
    def retornarPedido(self, codPedido):
        achou = False
        if len(self.pedidos) == 0:
           return print("\n--------------------------------------------\nNenhum Pedido Cadastrado Na Memória!\n--------------------------------------------")
        for pedido in self.pedidos:
            if pedido.codPedido == codPedido:
                achou = True
                return pedido
                
        if not achou:
            return print("\n--------------------------------------------\nCódio De Pedido Inválido!\n--------------------------------------------")
            
    def retornarProduto(self, idProduto):
        achou = False
        if len(self.produtos) == 0:
           return print("\n--------------------------------------------\nNenhum Produto Cadastrado Na Memória!\n--------------------------------------------")
        for produto in self.produtos:
            if produto.idProduto == idProduto:
                achou = True
                return produto
                
        if not achou:
            return print("\n--------------------------------------------\nID Do Produto Inválido!\n--------------------------------------------")
            
            

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
    def __init__(self, codPedido, cliente):
        self.itens = ListaLigada()
        self.codPedido = codPedido
        self.cliente = cliente
        # numeroPedido, cliente, status_pedido, itens):
        # self.numeroPedido = numeroPedido
        # self.cliente = cliente
        # self.status_pedido = status_pedido
        # self.itens = itens

        ## Criar função para adicionar pedidos

    def adicionarItemPedido(self, itemPedido):
        self.itens.insereOrdenadoNmrPedido(itemPedido)

    def mostrarItens(self):
        if self.itens.inicio != None:
            atual = self.itens.inicio
            while atual:
                print("----------------------------------")
                print(f'Numero Item Pedido: {atual.pedido.numeroPedido}')
                print(f'Status: {atual.pedido.status}')
                print(f'Quantidade: {atual.pedido.quantidade}')
                print("Produto:")
                print(f'  L____ Id Produto: {atual.pedido.produto.idProduto}')
                print(f'  L____ Produto Nome: {atual.pedido.produto.nome}')
                print(f'  L____ Preço: R${atual.pedido.produto.valor}')
                
                print(f"\nValor do Item: R${atual.pedido.produto.valor*atual.pedido.quantidade}")
                atual = atual.proximo
        else:
            print("\n--------------------------------------------\nLista De Itens Vazia!\n--------------------------------------------")
    
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

memoria = Memoria()
    
print("=====================================")
print("           Trabalho Pedidos          ")
print("=====================================")
while True:
    print("Qual operação deseja realizar?:")
    print("1-Cadastrar Cliente    2-Cadastrar Produto    3-Criar Pedido")
    print("4-Mostrar Clientes     5-Mostrar Produtos     6-Mostrar Pedidos")
    print("7-Adicionar Item       8-Cadastrar Produto    9-Criar Pedido")
    ## ADICIONAR EXCLUIR E PESQUISAR APARTIR DE IDS

    print("0-Exit")

    op = int(input(":  "))

    if op == 1:
        
        print("----Cadastrar Cliente-----")
        while True:
            cpf = input("CPF: ")
            if cpf == "sair" or cpf == "voltar":
                break
            if memoria.retornarCliente(cpf) == None:
                nome = input("Nome: ")
                nasc = input("Nascimento: ")
                sexo = input("Sexo: ")
                cli = Cliente(cpf, nome, nasc, sexo)
                memoria.clientes.append(cli)
                print("\n-------------------------------")
                print("Ciente Adicionado Com Sucesso!")
                print("-------------------------------")
                break
            else:
                print("CPF já cadastrado!!!")


    if op == 2:
        print("\n----Cadastrar Produto-----")
        id_produto = int(input("(Criar)ID:  "))
        nome_produto = input("Nome do Produto:  ")
        valor_produto = int(input("Valor do Produto:  "))
        produto = Produto(id_produto, nome_produto, valor_produto)
        ## Adicionar validação, verificar se já existe um produto com aquele ID no array da memória
        memoria.produtos.append(produto)
        print("\n-------------------------------")
        print("Produto Adicionado Com Sucesso!")
        print("-------------------------------")

    if op == 3:
        if not memoria.clientesIsNull():
            print("\n----Criar Pedido-----")
            codPedido = input("(Criar) Código do Pedido:  ")
            while True:
                cliente = memoria.retornarCliente(input("CPF do CLiente:  "))
                if cliente != "Sair" or cliente != "Voltar":
                    if cliente != None:
                        break
                    else:
                        print("\n--------------------------------------------\nCPF Não Cadastrado!\n--------------------------------------------")
                else:
                    break
            if cliente == None:
                print("\n-------------------------------")
                print("Falha ao Criar Pedido!")
                print("-------------------------------")
            else:
                ## Adicionar validação, verificar se já existe um produto com aquele ID no array da memória
                pedido = Pedido(codPedido ,cliente)
                memoria.pedidos.append(pedido)
                print("\n-------------------------------")
                print("Pedido Adicionado Com Sucesso!")
                print("-------------------------------")
        else:
            print("\n-------------------------------")
            print("Você deve Cadastrar Um Cliente Primeiramente!")
            print("-------------------------------")
    # if op == 3:
    #     print("\n----Criar Pedido-----")
    #     numero_pedido = int(input("Numero do Pedido:  "))
    #     id_produto = input("ID do Produto:  ")
    #     quantidade = input("Quantidade:  ")
    #     status = input("Status do Pedido:  ")
    #     staus = Produto(id_produto, nome_produto, valor_produto)
    #     ## Adicionar validação, verificar se já existe um produto com aquele ID no array da memória
    #     memoria.produtos.append(produto)
    #     print("\n-------------------------------")
    #     print("Produto Adicionado Com Sucesso!")
    #     print("-------------------------------")

    if op == 4:
        memoria.mostrarClientesMemoria()

    if op == 5:
        memoria.mostrarProdutosMemoria()

    if op == 6:
        memoria.mostrarPedidosMemoria()

    if op == 7:
        if not memoria.pedidosIsNull() and not memoria.produtosIsNull():
            print("\n----Adicionar Item-----")
            pedido = memoria.retornarPedido(input("Código do Pedido:  "))
            if pedido != None:
                codItemPedido = input("(Criar) Código do Item Do Pedido:  ")
                produto = memoria.retornarProduto(int(input("ID Do Produto:  ")))
                if produto != None:
                    quantidade = int(input("Quantidade:  "))
                    status = input("Status do Pedido:  ")
                    ## Adicionar validação, verificar se já existe um produto com aquele ID no array da memória
                    itemPedido = ItemPedido(codItemPedido, produto, quantidade, status)
                    pedido.adicionarItemPedido(itemPedido)
                    print("\n-------------------------------")
                    print("Item Adicionado ao Pedido Com Sucesso!")
                    print("-------------------------------")
                        
                else:
                    print("\n-------------------------------")
                    print("Falha ao Encotrar o Produto!")
                    print("-------------------------------")

        else:
            if memoria.pedidosIsNull():
                print("\n-------------------------------")
                print("Você deve criar um Pedido primeiro!")
                print("-------------------------------")
            if memoria.produtosIsNull():
                print("\n-------------------------------")
                print("Você deve criar um Produto primeiro!")
                print("-------------------------------")


    if op == 0:
        break
    


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

pedido1 = Pedido(00 ,cli1)

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