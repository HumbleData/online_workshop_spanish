import pandas as pd
from IPython.display import display
pd.options.mode.chained_assignment = None

df = pd.read_csv("../data/Penguins/penguins.csv")
df_2 = df.dropna(how="all")
df_3 = df_2.dropna(how="any")
df_4 = df_3.drop_duplicates()
df_4['species'] = df_4['species'].astype('category')

display(df_4.groupby("species").median(numeric_only=True))

Solucion aca: https://raw.githubusercontent.com/HumbleData/online_workshop_spanish/main/conteudo/solutions/02_31.py