# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

list_1 = [n for n in range(2, 100)]
list_2 = [n for n in range(2, 10)]

for x in list_2:
    count_num = 0
    for z in list_1:
        if z % x == 0:
            count_num += 1

    print(f'Для числа {x} - кратно {count_num} раз из диопазона от 2 до 99')
