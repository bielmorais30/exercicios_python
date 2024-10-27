class Gato:
    def __init__(self, nome: str, idade: int, acordado: bool):
        self.nome = nome
        self.idade = idade
        self.acordado = acordado

    def myname(self):
        return self.nome
    
    def acordar(self):
        if self.acordado == True:
            print(f"O {self.nome} já está acordado!")
        else:
            self.acordado = True
            print(f"Você acordou o {self.nome}!!!")

    def dormir(self):
        if self.acordado == True:
            self.acordado = False
            print(f"Agora {self.nome} está dormindo ZzzzZzzz!!!") 
        else:
            print(f"{self.nome} já está dormindo!!!")

    def miar(self):
        if self.acordado == True:
            print("Miauuuu!!!!")
        else:
            print(f"{self.nome} está dormindo! Acorde-o primeiro!")

    def printar(self):
        print(self.nome, self.idade, self.acordado)

nome = input("Digite o nome do seu gato: ")
idd = int(input("Digite a idade do seu gato: "))
try:
    op = int(input("Seu gato está dormindo? 1-Sim 2-Não "))
except:
    print("Entre com uma das duas opções!")
    exit()

status = True

if op == 1:
    status = False


gato = Gato(nome, idd, status)
while op != 5:
    op = int(input(f"O que deseja que o fazer com o gato? 1-Acordar o {gato.nome} 2-Colocar o {gato.nome} pra dormir 3-Fazer o {gato.nome} miar 5-Fechar \n"))

    if op == 1:
        gato.acordar()
    if op == 2:
        gato.dormir()
    if op == 3:
        gato.miar()
    if op == 4:
        gato.printar()


               