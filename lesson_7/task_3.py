# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки, который
# не рассматривался на уроках (сортировка слиянием также недопустима).
import random

m = int(input('Введите m для генерации массива длиной 2m + 1: '))
SIZE = 2*m + 1
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'{array}')


def get_median(arr):
    end = len(arr) - 1
    start = 0
    mid = len(arr) // 2
    while True:
        left = start
        right = end
        counter = 0
        while left < right:
            if arr[left] >= arr[left + 1]:
                if arr[left] == arr[left + 1]:
                    counter += 1
                else:
                    arr[left], arr[left + 1] = arr[left + 1], arr[left]
                left += 1
            else:
                arr[left + 1], arr[right] = arr[right], arr[left + 1]
                right -= 1
        if left < mid:
            start = left + 1
        elif left > mid:
            if left - counter <= mid:
                return arr[left]
            else:
                end = left - 1
        else:
            return arr[left]


median = get_median(array)
print(median)