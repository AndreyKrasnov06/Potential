import csv

classatk = {}
"""Открытие исходной таблица монтсров"""
with open('monster_game.csv', newline='', encoding="UTF-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        atk = row["attack"]
        monclass = row["MonsterName"].split(' ')[-1]
        if monclass not in classatk:
            classatk = classatk | {monclass: []}
        classatk[monclass] = classatk[monclass] + [atk]

"""Вывод средней силы атаки"""
for key in classatk.keys():
    print(len(classatk[key]), "монстров класса", str.capitalize(key), "средняя сила атаки",
          sum(map(int, classatk[key])) / len(classatk[key]))
