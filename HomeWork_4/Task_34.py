# Даны два файла, в каждом из которых находится запись многочлена, приравненного к нулю. Задача - сформировать файл, содержащий сумму многочленов (суммируем подобные слагаемые). 
# Пример: 
# Файл :		2*x**2 + 4*x + 5 = 0 
# Файл :		4*x**2 + 7*x + 9 = 0 
# Файл: (содержит результат)	6*x**2 + 11*x + 14 = 0 
# Пример: 
# Файл :		2*x**3 + 4*x**2 + 5*x + 1 = 0 
# Файл :		4*x**2 + 7*x + 9 = 0 
# Файл: (содержит результат)	2*x**3 + 8*x**2 + 12*x + 10 = 0 

with open('file_1.txt', 'w') as file:
    file.write('2*x^2 + 4*x + 5')
with open('file_2.txt', 'w') as file:
    file.write('4*x^2 + 7*x + 9')

with open('file_1.txt','r') as file:
    file_1 = file.readline()
    list_of_file_1 = file_1.split()

with open('file_2.txt','r') as file:
    file_2 = file.readline()
    list_of_file_2 = file_2.split()

with open('file_1_and_2.txt', 'w') as file:
    file.write(f'{list_of_file_1} + {list_of_file_2}')
