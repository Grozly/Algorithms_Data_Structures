# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'{array}')

min1, min22 = float('inf'), float('inf')
for x in array:
    if x <= min1:
        min1, min2 = x, min1
    elif x < min2:
        min2 = x

print(f'1:  {min1}\n2:  {min2}')