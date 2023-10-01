import pandas as pd
df = pd.read_csv("../data/Penguins/penguins.csv")

print(df["sex"].value_counts(dropna=False))


print('Solucion (código crudo): https://raw.githubusercontent.com/HumbleData/online_workshop_spanish/main/conteudo/solutions/02_18.py')