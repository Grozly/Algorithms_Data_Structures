# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Найти сумму n элементов следующего ряда чисел:
# 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

# OC Windows 10
# Python 3.8.3

# Первая задача
from count_s import count_s
n = 60
a = 1
b = 0

for i in range(n):
    b += a
    a /= -2

print(b)

my_sum = 0
var_lst = (n, a, b)
for i in var_lst:
    my_sum += count_s(i)
print(f'Под переменные задействованно {my_sum} байт памяти')  # Задействовано 46 байт.

# Вторая задача
summa_2 = 1 * (1 - (-0.5) ** n) / (1 - (-0.5))
print(f'{summa_2}')

my_sum = 0
var_lst = [summa_2]
for i in var_lst:
    my_sum += count_s(i)
print(f'Под переменные задействованно {my_sum} байт памяти')  # Задействовано 16 байт.

# Третья задача


def my_func3(n):
    func_dict = {0: 0, 1: 1, 2: 0.5}

    def _my_func3(n, a = 1.0):
        if n in func_dict:
            return func_dict[n]
        func_dict[n] = a + _my_func3(n - 1, a / -2)
        return func_dict[n]

    return _my_func3(n)

m = my_func3(n)
print(f'{m}')

my_sum = 0
var_lst = [my_func3, m]
for i in var_lst:
    my_sum += count_s(i)
print(f'Под переменные задействованно {my_sum} байт памяти')  # Задействовано 84 байт.

# Вывод очевиден, чем меньше переменных, тем меньше код занимает памяти.