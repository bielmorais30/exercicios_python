import tkinter as ttk
class Tela:
    
    def __init__(self, nome="TelaPrincipal", tamanho="350x500"):
        # self.nome = nome
        # self.tamanho = tamanho
        self.main = ttk.Tk()
        self.main.geometry(tamanho)
        self.main.title(nome)
        
    def adicionar_img(self):
        img = ttk.PhotoImage(file="./Poster_Filme.jpg")
        self.lbl = ttk.Label(self.main, image=img).place(x=10,y=15)
           
    
    def rodar(self):
        self.main.mainloop()


    
    