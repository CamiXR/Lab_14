#Задание 1
import pandas as pd
players = {
    "name":   ["CamiXR", "TheHellcart", "Meravka", "Cremassor", "Egireon105", "Fiazema2000"],
    "level":  [60, 55, 52, 78, 71, 33],
    "klass":  ["Воин", "Маг", "Шаман", "Лучник", "Демонолог", "Паладин"],
    "donate": [500, 1200, 300, 2400, 1800, 150]
}
df = pd.DataFrame(players)
print(df.head(2))

#Задание 2
df.to_csv("dataset.csv", index=False, encoding="utf-8")
df2 = pd.read_csv("dataset.csv", encoding="utf-8")
df2.info()

#Задание 3
result = df[(df["level"] > 50) & (df["klass"] == "Маг")]
print(result)

#Задание 4
top = df.sort_values("donate", ascending=False)

print(top.head(3))
#Задание 5
df["tax"] = df["donate"] * 0.13
print(df[["name", "donate", "tax"]].head(3))

#Задание 6
avg = df.groupby("klass")["donate"].mean()
print(avg)

#Задание 7
rich = df[df["level"] > 50]
rich.to_csv("rich_players.csv", index=False, encoding="utf-8")
print("Сохранено:", len(rich), "строк")
