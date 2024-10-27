nAcidentes = int(input("Entre com o numero de acidentes: "))
horasHomensTrabalhadas = int(input("Digite as Horas Homens Trabalhadas: "))
diasDebitados = int(input("Digite os dias Debitados: "))
qnt = int(input("Digite a quantidade de dias pessoas acidentadas com afastamento: "))
totalDiasPerdidos = 0

for i in range(qnt):
    diasPerdidos = int(input(f"Digite os dias perdidos da {i+1}° pessoa: 9"))
    totalDiasPerdidos += diasPerdidos

resultado = nAcidentes * 1000000 / horasHomensTrabalhadas

print("Coeficiente De Frequencia: ", resultado)

coGravidade = totalDiasPerdidos * 1000000 / horasHomensTrabalhadas

print("Dias Computados: ", coGravidade)