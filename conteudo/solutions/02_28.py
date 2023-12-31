import pandas as pd
from IPython.display import display
pd.options.mode.chained_assignment = None

df = pd.read_csv("../data/Penguins/penguins.csv")
df_2 = df.dropna(how="all")
df_3 = df_2.dropna(how="any")
df_4 = df_3.drop_duplicates()

df_4['species'] = df_4['species'].astype('category')
# código alternativo para evitar la advertencia
# df_4.loc[:, 'species'] = df_4['species'].astype('category')


display(df_4.dtypes)


print('Solucion (código crudo): https://raw.githubusercontent.com/HumbleData/online_workshop_spanish/main/conteudo/solutions/02_28.py')
