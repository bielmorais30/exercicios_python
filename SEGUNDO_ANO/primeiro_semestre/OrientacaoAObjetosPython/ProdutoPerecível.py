#import Produto
from Produto import Produto

#class ProdutoPerecivel(Produto.Produto):
class ProdutoPerecivel(Produto):

    def __init__(self,codigo,nome,preco,dataValidade):
        super().__init__(codigo,nome,preco)
        self.dataValidade=dataValidade

    def mostraDados(self):
        super().mostraDados()
        print(f'Data Validade: {self.dataValidade}')



p1=ProdutoPerecivel(10,"banana",8.5,"10/05/2024")
p1.mostraDados()


