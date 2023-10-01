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

df["city"] = df["city"].str.replace(r"/\w*", "", regex=True)

dict_capitals = {
    "Denmark": "copenhague",
    "France": "paris",
    "Italy": "rome",
    "Spain": "madrid",
    "United Kingdom": "london",
}

unknown_city = df["city"] == "unknown"
df.loc[unknown_city, "city"] = df.loc[unknown_city, "country"].map(dict_capitals)

dict_cities = df.loc[df['country'].notnull(), ['city', 'country']].set_index('city').to_dict()['country']

dict_cities.update(
    {
        "bristol": "United Kingdom",
        "gothenburg": "Sweden",
        "graz": "Austria",
        "lyon": "France",
        "murcia": "Spain",
        "parma": "Italy",
    },
)

null_country = df["country"].isnull()
df.loc[null_country, "country"] = df.loc[null_country, "city"].map(dict_cities)

print('null_country = df["country"].isnull()')
print('df.loc[null_country, "country"] = df.loc[null_country, "city"].map(dict_cities)')


print('Solucion (código crudo): https://raw.githubusercontent.com/HumbleData/online_workshop_spanish/main/conteudo/solutions/05_32.py')