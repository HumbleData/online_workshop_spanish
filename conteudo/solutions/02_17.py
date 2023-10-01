import pandas as pd
df = pd.read_csv("../data/Penguins/penguins.csv")

print(df["flipper_length_mm"].isnull().sum())


print('Solucion (código crudo): https://raw.githubusercontent.com/HumbleData/online_workshop_spanish/main/conteudo/solutions/02_17.py')