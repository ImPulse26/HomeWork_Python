# Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции (случайные) хранятся в файле file.txt (создаётся во время выполнения кода и зависит от количества
# элементов в списке) в одной строке одно число.
# Пример:
# Файл:
# 4
# 5
# 2
# N = 3 => [-3, -2, -1, 0, 1, 2, 3]
# Результат: 1*2*(-1) = -2

import random

Sintaksis_error = True
n = 0
while Sintaksis_error != False:
    string = input('Введите число => ')
    try:
        n = int(string)
        Sintaksis_error = False
        if n == 0:
            print('Невозможно создать список из 0 элементов')
            Sintaksis_error = True
    except ValueError:
        print('Некорректное число, повторите попытку')

list = []
digit = 1
with open('file.txt', 'w') as file:
    count_digits = random.randrange(1, n)
    for i in range(0, count_digits):
        file.writelines(str(random.randrange(0, n+1))+'\n')

for i in range(-n, n+1):
    list.append(i)
print(list)

with open('file.txt', 'r') as file:
    for digits in file:
        digit = digit * list[int(digits)]
print(f"Произведение элементов на указанных позициях => {digit}")
