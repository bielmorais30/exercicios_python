jovens = 0
menor_peso = float('inf')
for i in range(5):
    idd = int(input("\nIdade: "))
    peso = float(input("Peso: "))
    print('_________________')

    if idd >= 10 and idd <= 50:
        jovens = jovens + 1
    if idd >= 60:
        if menor_peso > peso:
            menor_peso = peso
        
if menor_peso == float('inf'):
    print('Não tem idosos!')
elif menor_peso != float('inf'):
    print(f'Menor Peso: {menor_peso}')

print(f'Jovens: {jovens}')

