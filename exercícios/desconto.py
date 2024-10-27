preco = float(input("Entre com o valor do produto: R$"))
desconto = preco - 7 / 100 * preco
aumento = preco + 5.5 / 100 * preco
print(f"Valor com desconto:{desconto:.2f}")
print(f"Valor com aumento:{aumento:.2f}")