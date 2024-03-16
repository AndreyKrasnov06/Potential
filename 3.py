import csv

"""Открытие исходной таблица монтсров, бесконечный цикл ожидающий слова хватит, сопоставление силы игрокам и монстра, подсчёт количества"""
while (player_force := input("Введите вашу силу атаки ")) != "хватит":
    player_force = int(player_force)
    count = 0
    with open('monster_game.csv', newline='', encoding="UTF-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            health = int(row["health"])
            if health != 0 and player_force > health:
                count += 1
    """Вывод данных"""
    if count == 0:
        print("Вы очень слабы. Сходите и наберитесь опыта!")
    else:
        print(f"Вы сможете победить: {count} монстров")
