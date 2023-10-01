import pandas as pd
df = pd.read_csv("../data/Penguins/penguins.csv")

print(df[df["flipper_length_mm"].isnull()].index)

Solucion aca: https://raw.githubusercontent.com/HumbleData/online_workshop_spanish/main/conteudo/solutions/02_20.py