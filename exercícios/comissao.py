sal = float(input("Salário Fixo: R$"))
vendas = float(input("\nValor das Vendas: $"))

comissao = 7.5 / 100 * vendas

print(f"Comissão: R${comissao}")
print(f"Salário Final: R${sal+comissao}")