class Produto:

    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    def mostraDados(self):
        print(f'Cdigo: {self.codigo}  Nome: {self.nome}  Preco: {self.preco}')

# p1 = Produto(10,"banana",8.5)
# p1.mostraDados()

# p2 =Produto(20,"couve",5.35)
# p2.mostraDados()
