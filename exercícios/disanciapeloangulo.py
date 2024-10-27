from math import sin, cos, radians, degrees, pi
graus = float(input("Ãngulo (Graus): "))
metros = float(input("\nMetros: "))

comprimento = metros / cos(radians(graus))
print(f"Comprimento: {comprimento:.1f}m")