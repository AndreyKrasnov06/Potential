import csv
def insertion_sort(array, key):
    n = len(array)
    for i in range(1, n):
        x = array[i][key]
        j = i

        while j > 0 and array[j - 1][key] > x:
            array[j] = array[j - 1]
            j -= 1

        array[j][key] = x

    return array

monsterlist = []

with open('monster_game.csv', newline='', encoding="UTF-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        monsterlist.append(row)
print(monsterlist)
print(insertion_sort(monsterlist, "opportunity"))
