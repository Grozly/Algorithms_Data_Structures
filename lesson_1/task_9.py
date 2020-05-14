# 9. Вводятся три разных числа.
# Найти, какое из них является средним (больше одного, но меньше другого).

print('Ведите 3 разных числа:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if b < a < c or c < a < b:
    print('Среднее:', a)
elif a < b < c or c < b < a:
    print('Среднее:', b)
else:
    print('Среднее:', c)
