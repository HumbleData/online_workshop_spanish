import pandas as pd
df = pd.read_csv("../data/Penguins/penguins.csv")

print(df["species"].value_counts(normalize=True))


print('Solucion (código crudo): https://raw.githubusercontent.com/HumbleData/online_workshop_spanish/main/conteudo/solutions/02_19.py')