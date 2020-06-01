# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
# (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.
from collections import Counter
from collections import deque

companys = Counter()
n = int(input("Введите кол-во компаний: "))
s = 0
for i in range(n):
    new_company = input(str(i + 1) + '-ая компания: ')
    profit1 = int(input('Прибыль за 1 квартал: '))
    profit2 = int(input('Прибыль за 2 квартал: '))
    profit3 = int(input('Прибыль за 3 квартал: '))
    profit4 = int(input('Прибыль за 4 квартал: '))
    companys[new_company] = profit1 + profit2 + profit3 + profit4
    s += profit1 + profit2 + profit3 + profit4

average = s / n

result_max = deque()
result_min = deque()

for i in companys:
    if companys[i] > average:
        result_max.append(i)
    elif companys[i] < average:
        result_min.append(i)


print(f'\nСредняя прибыль для всех компаний: {average}'
      f'\nКомпании чья прибыль больше средней: {", ".join(result_max)}'
      f'\nКомпании чья прибыль меньше средней: {", ".join(result_min)}')