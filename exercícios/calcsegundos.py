print("\nCalcular Segundos")
dias = float(input("Dias: "))
horas = float(input("Horas: "))
minutos = float(input("Minutos "))
segundos = float(input("Segundos: "))

tsegundos = segundos + minutos*60 + (horas * 60 * 60) + (dias * 24 * 60 * 60)
print(f"Total: {tsegundos}")