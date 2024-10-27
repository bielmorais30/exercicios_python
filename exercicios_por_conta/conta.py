class Conta_Bancaria():
    def __init__(self, nome: str, numero_conta: int, senha: int, saldo: float):
        self.nome = nome
        self.numero_conta = numero_conta
        self.senha = senha
        self.saldo = saldo

    def sacar(self):
        contador = 0 
        while contador < 4:
            

            verifica_conta = int(input("Digite o numero de sua conta: \n"))
            if verifica_conta == self.numero_conta:
                contador = 4
            else:
                if contador == 3:
                    print("Tente novamente mais tarde!")
                    exit()
                print(f"Conta não encontrada, tente novamente: {contador}\n")
                contador += 1
            

        contador = 0
        while contador < 4:

            verifica_senha = int(input("Digite sua senha: \n"))
            if verifica_senha == self.senha:    
                contador = 4
                print(f"Saldo disponível: {self.saldo}")        
                qnt = float(input("Deseja sacar quanto? \n"))
                if qnt > self.saldo:        
                    print("Saldo Insuficiente!!!")
                                
                else:        
                    self.saldo = self.saldo - qnt        
                    print(f"Você sacou R${qnt}\n Saldo atual: R${self.saldo}")
                          
            else:        
                if contador == 3:
                    print("Limite de tentativas exedido, tente novamente mais tarde!")
                    exit()
                print(f"Senha incorreta, tente novamente! {contador}\n")
                contador += 1

    def depositar(self):
        qnt = float(input("Deseja depositar quanto? \nR$"))
        self.saldo += qnt
        print("Saldo atual")

    def extrato(self):
        print(f"Saldo atual: R${self.saldo}")

nome = input("Digite seu nome:  ")
numero_conta = int(input("Digite o numero da conta:  "))        
senha = int(input("Escolha uma senha: \n"))
saldo = float(input("Entre com o saldo da sua conta:  R$"))

conta = Conta_Bancaria(nome, numero_conta, senha, saldo)

op2 = 1

while op2 != 0:
    op = int(input("Qual operação deseja fazer? 1-Depositar  2-Sacar  3-Ver Saldo  4-Encerrar\n"))
    match op:
        case 1:
            conta.depositar()
        case 2:   
            conta.sacar()
        case 3:
            conta.extrato()
        case 4:
            op2 = 0
                                        