import tkinter.messagebox
idade = int(input("Digite sua idade: "))
tempo = int(input("Anos trabalhados: "))

if idade >= 65 or tempo >= 30 or idade >=60 and tempo >= 25:
    print("Você pode aposentar!")  
else:
    print("Você não pode aposentar.")
    tkinter.messagebox.showerror(title="Error", message="Voce não pode se aposentar!")
    
    