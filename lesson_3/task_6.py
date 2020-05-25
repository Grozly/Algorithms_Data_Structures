# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'{array}')


index_of_min = 0
index_of_max = 0
for i in range(1, len(array)):
    if array[i] > array[index_of_max]:
        index_of_max = i
    if array[i] < array[index_of_min]:
        index_of_min = i

if index_of_max > index_of_min:
    print(f'{array[index_of_min + 1:index_of_max]} - сумма: {sum(array[index_of_min + 1:index_of_max])}')
else:
    print(f'{array[index_of_max + 1:index_of_min]} - сумма: {sum(array[index_of_max + 1:index_of_min])}')

