import pandas as pd

df_2014 = pd.read_csv("../data/food_training/training_2014.csv", header=1)
df_2015 = pd.read_csv("../data/food_training/training_2015.csv", header=1)
df_2016 = pd.read_csv("../data/food_training/training_2016.csv", header=1)

frames = [df_2014, df_2015, df_2016]
df = pd.concat(frames)

print('df.shape')
display(df.shape)


Solucion aca: https://raw.githubusercontent.com/HumbleData/online_workshop_spanish/main/conteudo/solutions/05_08.py