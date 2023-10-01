import pandas as pd
from IPython.display import display
df = pd.read_csv("../data/Penguins/penguins.csv")

display(df["bill_length_mm"])


print('Solucion (código crudo): https://raw.githubusercontent.com/HumbleData/online_workshop_spanish/main/conteudo/solutions/02_08.py')