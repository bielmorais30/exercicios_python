import pandas as pd

aa = pd.read_excel("novo_arquivo.xlsx")

#modificando
aa.at[8, "idade"] = 69

aa.at[9, "idade"] = 69

aa.at[9, "idade"] = pd.NA

print(aa[aa["idade"] >= 18])