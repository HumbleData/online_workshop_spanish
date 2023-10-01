import pandas as pd
pd.options.mode.chained_assignment = None

df = pd.read_csv("../data/Penguins/penguins.csv")
df_2 = df.dropna(how="all")
df_3 = df_2.dropna(how="any")
df_4 = df_3.drop_duplicates()
df_4['species'] = df_4['species'].astype('category')

print(df_4.min(numeric_only=True))


print('Solucion (código crudo): https://raw.githubusercontent.com/HumbleData/online_workshop_spanish/main/conteudo/solutions/02_29.py')