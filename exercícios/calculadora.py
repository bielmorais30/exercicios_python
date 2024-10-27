import tkinter.messagebox
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

op = int(input("Opções: \n1. Soma dos dois valores. \n2. Diferença dos dois valores (maior - menor). \n3. Multiplicação dos dois valores.\n4. Divisão dos dois valores (1º pelo 2º).\nEscolha: "))
resultado = 0

if op <= 4:
    if op == 1:
        print(f"Soma: {num1}+{num2}")
        resultado = (num1+num2)
    elif op == 2:
        if num1 > num2:
            print(f"Soma: {num1}-{num2}", end="")
            resultado = (num1-num2)
        else:
            print(f"Soma: {num2}-{num1}", end="")
            resultado = (num2-num1)
    elif op == 3:
        print(f"Soma: {num1}*{num2}", end="")
        resultado = (num1*num2)
    elif op == 4:
        print(f"Soma: {num1}/{num2}", end="")
        resultado = (num1/num2)

    print(f" = {resultado}")
else:
    print("Opção Invalida!!!")
    tkinter.messagebox.showerror(title="Error", message="Entre com uma opção valida!")