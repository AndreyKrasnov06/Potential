import csv

regen_list = []
dophod_list = []
attack_boost_list = []

"""Открытие исходной таблица монтсров"""
with open('monster_game.csv', newline='', encoding="UTF-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        opportunity = row["opportunity"]
        if opportunity == "регенерация":
            regen_list.append(float(row["health"]) * float(row["probability"]) / 100)
        elif opportunity == "дополнительный ход":
            summa = float(row["attack"]) + float(row["protection"]) + float(row["health"]) + float(row["speed"])
            dophod_list.append(summa * float(row["probability"]) / 100)
        elif opportunity == "усиление атаки":
            attack_boost_list.append(float(row["attack"]) * float(row["probability"]) / 100)

"""Определение максимальный значений"""
maxregen = max(regen_list)
maxdophod = max(dophod_list)
maxattack = max(attack_boost_list)

"""запись значений в таблицу"""
with open('monster_opportunity.csv', 'w', newline='', encoding="UTF-8") as csvfile:
    fieldnames = ['opportunity', 'power']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'opportunity': 'регенерация', 'power': str(maxregen)})
    writer.writerow({'opportunity': 'дополнительный ход', 'power': str(maxdophod)})
    writer.writerow({'opportunity': 'усиление атаки', 'power': str(maxdophod)})

print(f"Регенерация: {maxregen}")
print(f"Дополнительный ход: {maxdophod}")
print(f"Усиление атаки: {maxattack}")
