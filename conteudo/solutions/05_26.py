import pandas as pd

df_2014 = pd.read_csv("../data/food_training/training_2014.csv", header=1)
df_2015 = pd.read_csv("../data/food_training/training_2015.csv", header=1)
df_2016 = pd.read_csv("../data/food_training/training_2016.csv", header=1)

frames = [df_2014, df_2015, df_2016]
df = pd.concat(frames)

df = df.reset_index()
df.index

cols_to_remove = ["Unnamed: 5", "Unnamed: 6"]
df = df.drop(cols_to_remove, axis=1)

df[["city", "country"]] = df["Location"].str.split(pat=";", expand=True)

df = df.drop("Location", axis=1)

df["city"] = df["city"].str.lower()

print('df["city"] = df["city"].str.replace(r"/\w*", "", regex=True)\n')

df["city"] = df["city"].str.replace(r"/\w*", "", regex=True)

# display(df["city"].tail())

Solucion aca: https://raw.githubusercontent.com/HumbleData/online_workshop_spanish/main/conteudo/solutions/05_26.py