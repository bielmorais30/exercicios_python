import Produto

class ItemPedido:
    def __init__(self, produto, quantidade, preco):
        self.Produto = produto
        self.quantidade = quantidade
        self.preco = preco

    def print(self):
        print(self.quantidade, self.preco)
a = ItemPedido(Produto.Produto(1, "teste", "M", 2), 3, 4)

a.print()

