import tkinter as tk

tela = tk.Tk()
tela.geometry("350x500")
tela.title("Dacte RN Firefox")

lbl_estado = tk.Label(tela, text="Estado:")
lbl_estado.place(x=10,y=15)
ipt_estado = tk.Text(height=1, width=10)
ipt_estado.place(x=70, y=15)


lbl_ano = tk.Label(tela, text="Ano:")
lbl_ano.place(x=10,y=45)
ipt_ano = tk.Text(height=1, width=10)
ipt_ano.place(x=70, y=45)


lbl_mes = tk.Label(tela, text="Mês:")
lbl_mes.place(x=10,y=75)
ipt_mes = tk.Text(height=1, width=10)
ipt_mes.place(x=70, y=75)


lbl_CNPJ = tk.Label(tela, text="CNPJ:")
lbl_CNPJ.place(x=10,y=105)
ipt_CNPJ = tk.Text(height=1, width=21)
ipt_CNPJ.place(x=70, y=105)


lbl_serie = tk.Label(tela, text="Série:")
lbl_serie.place(x=10,y=135)
ipt_serie = tk.Text(height=1, width=10)
ipt_serie.place(x=70, y=135)


lbl_Numero = tk.Label(tela, text="Número:")
lbl_Numero.place(x=10,y=165)
ipt_Numero = tk.Text(height=1, width=15)
ipt_Numero.place(x=70, y=165)

btn_Ac = tk.Button(tela, text="Ac", width=7, anchor="w")
btn_Ac.place(x=200, y=165)


lbl_Forma = tk.Label(tela, text="Forma:")
lbl_Forma.place(x=10,y=195)
ipt_Forma = tk.Text(height=1, width=10)
ipt_Forma.place(x=70, y=195)


lbl_Codigo = tk.Label(tela, text="Código:")
lbl_Codigo.place(x=10,y=225)
ipt_Codigo = tk.Text(height=1, width=15)
ipt_Codigo.place(x=70, y=225)


lbl_Captcha = tk.Label(tela, text="Captcha:")
lbl_Captcha.place(x=10,y=280)
ipt_Captcha = tk.Text(height=1, width=10)
ipt_Captcha.place(x=70, y=280)

btn_Captcha = tk.Button(tela, text="Captcha", width=11)
btn_Captcha.place(x=170, y=280)



btn_Navegar = tk.Button(tela, text="Navegar", width=11)
btn_Navegar.place(x=200, y=415)




tk.mainloop()