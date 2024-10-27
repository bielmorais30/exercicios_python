import tkinter as tk
from ClasseCliente import Cliente
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserirInicio(self, valor):
        no = No(valor)
        no.proximo = self.inicio
        self.inicio = no
    
    def insereFinal(self, valor):
        atual = self.inicio

        if atual == None:
            self.inserirInicio(valor)
            return
        while atual.proximo:
            atual = atual.proximo
        
        no = No(valor)
        atual.proximo = no

    def insereDepois(self, p, valor):
        no = No(valor)
        no.proximo = p.proximo
        p.proximo = no

    def mostrarLista(self):
        atual = self.inicio
        while atual:
            print(atual.valor)
            atual = atual.proximo

class Clientes:
    def __init__(self):
        self.clientes = ListaEncadeada()

    def inserirCliente(self, cliente):
        self.clientes.insereFinal(cliente)

    def mostrarClientes(self):
        atual = self.clientes.inicio
        while atual:
            print(atual.valor.cpf)
            print(atual.valor.nome)
            print(atual.valor.data_nasc)
            print(atual.valor.sexo)
            atual = atual.proximo

meusClientes = Clientes()

def cadastrarCliente():
    cpf = str(ipt_cpf.get())
    var_nome = str(ipt_nome.get())
    nasc = str(ipt_nasc.get())
    sexo = str(ipt_sexo.get())
    print(var_nome)
    cli = Cliente(cpf, var_nome, nasc, sexo)
    meusClientes.inserirCliente(cli)
    print(f"{var_nome} Cadastrado Com Sucesso!")
    meusClientes.mostrarClientes()






tela = tk.Tk("Pedidos")

tela.geometry("1700x500")
tela.title("Clientes")

lbl_cpf = tk.Label(tela, text="CPF:")
lbl_cpf.place(x=10,y=15)
ipt_cpf = tk.Entry()
ipt_cpf.place(x=90, y=15)


lbl_nome = tk.Label(tela, text="Nome:")
lbl_nome.place(x=10,y=45)
# ipt_nome = tk.Text(height=1, width=10)
# ipt_nome.place(x=90, y=45)
ipt_nome = tk.Entry(width=25, bg="white", font=("Comic Sans MS", "10"))
ipt_nome.place(x=90, y=45)


lbl_nasc = tk.Label(tela, text="Nascimento:")
lbl_nasc.place(x=10,y=75)
ipt_nasc = tk.Entry()
ipt_nasc.place(x=90, y=75)


lbl_sexo = tk.Label(tela, text="Sexo:")
lbl_sexo.place(x=10,y=105)
ipt_sexo = tk.Entry()
ipt_sexo.place(x=90, y=105)



salvarCliente = tk.Button(tela, text="Enviar", command=lambda: cadastrarCliente())##estudar lambda
salvarCliente.place(x=90, y=135)


tela.mainloop()