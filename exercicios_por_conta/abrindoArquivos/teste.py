import random 

op = int(input("1-Animais 2-Adjetivos: "))

if op == 1:
    meuArquivo = open("animais.txt", "r")
elif op == 2:
    meuArquivo = open("adjetivos.txt", "r")
else:
    print("Opção inválida.")
    exit()

data = meuArquivo.read()
meuArquivo.close()
words = data.split()

word_pos = random.randint(0, len(words)-1)
print("O Diogo é", words[word_pos])