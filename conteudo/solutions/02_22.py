import pandas as pd
df = pd.read_csv("../data/Penguins/penguins.csv")

df_2 = df.dropna(how="all")


print('Solucion (código crudo): https://raw.githubusercontent.com/HumbleData/online_workshop_spanish/main/conteudo/solutions/02_22.py')