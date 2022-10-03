# Реализуйте алгоритм перемешивания списка.

import random

n = int(input('Введите размер списка => '))
min = int(input('Введите минимальное значение => '))
max = int(input('Введите максимальное значение => '))
source_list = list([random.randint(min, max) for i in range(n)])
print(f"Исходный лист => {source_list}")
random.shuffle(source_list)
print(f"Лист после перемешивания => {source_list}")