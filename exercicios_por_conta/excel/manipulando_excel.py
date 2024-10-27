# pip install openpyxl
# pip install pandas
import pandas as pd

data_frame = pd.read_excel("C:/Users/autologon/Desktop/arquivo_teste.xlsx")

data_frame.to_excel('novo_arquivo.xlsx', index=False)  # index=False para não escrever o índice do DataFrame no arquivo Excel

print(data_frame)
print(f"Quantidade de Pessoas: {data_frame["nome"].count()}", end="  ")
df_filtrado = data_frame[data_frame['idade']  > 18]
print(f"Maiores de idade: {df_filtrado["nome"].count()}")





print(f"Media de idade: {data_frame["idade"].mean()}")


# maiores_18 = data_frame.bfill(limit=5)
# print(maiores_18)