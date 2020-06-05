# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10
MIN_ITEM = 0.0
MAX_ITEM = 49.9
array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'{array}')


def merge(left, right):
    sorted_list = []
    left_idx = 0
    right_idx = 0

    for _ in range(len(left) + len(right)):
        if left_idx < len(left) and right_idx < len(right):
            if left[left_idx] <= right[right_idx]:
                sorted_list.append(left[left_idx])
                left_idx += 1
            else:
                sorted_list.append(right[right_idx])
                right_idx += 1

        elif left_idx == len(left):
            sorted_list.append(right[right_idx])
            right_idx += 1

        elif right_idx == len(right):
            sorted_list.append(left[left_idx])
            left_idx += 1
    return sorted_list


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

sorted = merge_sort(array)
print(f'{sorted}')

