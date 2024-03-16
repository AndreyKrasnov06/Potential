import csv

"""Хеш функция"""


def generate_hash(s: str):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИКЛМНОПРСТУФХЙЧЪЫЬЭЮЯ '
    d = {l: i for i, l in enumerate(alphabet, 1)}
    p = 67
    m = 1e9 + 9
    hash_value = 0
    p_pow = 1
    for c in s:
        hash_value = (hash_value + d[c] * p_pow) % m
        p_pow = (p_pow * p) % m
    return int(hash_value)


monster_hash = []
"""Открытие исходной таблица монтсров"""
with open('monster_game.csv', newline='', encoding="UTF-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["opportunity"])
        monster_hash.append(
            [row["MonsterName"] + row["opportunity"] + row["probability"], generate_hash(row["opportunity"])])

print(monster_hash)

"""Вывод данных"""
with open('hash_table.csv', 'w', newline='', encoding='utf8') as file:
    fieldnames = ['key', 'value']
    w = csv.DictWriter(file, fieldnames=fieldnames)
    w.writeheader()
    for row in monster_hash:
        w.writerow({'key': row[0], 'value': row[1]})
