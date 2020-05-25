# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
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
array[index_of_min], array[index_of_max] = array[index_of_max], array[index_of_min]

print(' '.join([str(x) for x in array]))