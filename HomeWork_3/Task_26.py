# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи]

number = int(input('Ввелите число => '))
num_1 = 0
num_2 = 1
fibonacci_1 = [0]
for i in range(number):
    num_1, num_2 = num_2, num_1 + num_2
    fibonacci_1.append(num_1)
num_1 = 0
num_2 = 1
fibonacci_2 = []
for i in range(number):
    num_1, num_2 = num_2, num_1 - num_2
    fibonacci_2.append(num_1)
fibonacci_2.reverse()
print(fibonacci_2 + fibonacci_1)
