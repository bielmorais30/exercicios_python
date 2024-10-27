import datetime
Gb = float(input("Tamanho do Arquivo: GBytes "))
velocidade = float(input("Velocidade De Donwload: Mbit/s "))
tempo = (Gb * 1024)/(velocidade/8)
# horas = tempo // (60*60)
# minutos = tempo // 60
# segundos = tempo % 60
print(f"{datetime.timedelta(seconds=tempo)}")
