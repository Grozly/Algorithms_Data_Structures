# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
# трех уроков. Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# Алексей за основу я взал задачу №4 из урока 2
import timeit
import cProfile


# Первая задача которая у меня была


def my_func1(n):
    a = 1
    b = 0
    for i in range(n):
        b += a
        a /= -2
    return b


print(timeit.timeit('my_func1(1)', number=1000, globals=globals()))  # 0.0004693999999999983  (кол-во N этементов 1)
print(timeit.timeit('my_func1(10)', number=1000, globals=globals()))  # 0.0013935999999999983 (кол-во N этементов 10)
print(timeit.timeit('my_func1(100)', number=1000, globals=globals()))  # 0.007892300000000001 (кол-во N этементов 100)
print(timeit.timeit('my_func1(1000)', number=1000, globals=globals()))  # 0.09026390000000001 (кол-во N этементов 1000)
print(timeit.timeit('my_func1(10000)', number=1000, globals=globals()))  # 0.9843386999999999 (кол-во N этементов 10000)

# Мы наблюдаем линейную зависимость

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
cProfile.run('my_func1(1)')
#      1    0.000    0.000    0.000    0.000 task_1.py:16(my_func1)
cProfile.run('my_func1(10)')
#      1    0.000    0.000    0.000    0.000 task_1.py:16(my_func1)
cProfile.run('my_func1(100)')
#      1    0.000    0.000    0.000    0.000 task_1.py:16(my_func1)
cProfile.run('my_func1(1000)')
#      1    0.000    0.000    0.000    0.000 task_1.py:16(my_func1)
cProfile.run('my_func1(10000)')
#      1    0.001    0.001    0.001    0.001 task_1.py:16(my_func1)

# Вторая задача с использованием while


def my_func2(n):
    a = 1
    b = 0
    while n > 0:
        b += a
        a /= -2
        n -= 1
    return b


print(timeit.timeit('my_func2(1)', number=1000, globals=globals()))  # 0.00023960000000000647 (кол-во N этементов 1)
print(timeit.timeit('my_func2(10)', number=1000, globals=globals()))  # 0.0014220000000000343 (кол-во N этементов 10)
print(timeit.timeit('my_func2(100)', number=1000, globals=globals()))  # 0.011999899999999952 (кол-во N этементов 100)
print(timeit.timeit('my_func2(1000)', number=1000, globals=globals()))  # 0.13545300000000005 (кол-во N этементов 1000)
print(timeit.timeit('my_func2(10000)', number=1000, globals=globals()))  # 1.4344887999999998 (кол-во N этементов 10000)

# Также наблюдаем линейную сложность алгоритма

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
cProfile.run('my_func2(1)')
#      1    0.000    0.000    0.000    0.000 task_1.py:46(my_func2)
cProfile.run('my_func2(10)')
#      1    0.000    0.000    0.000    0.000 task_1.py:46(my_func2)
cProfile.run('my_func2(100)')
#      1    0.000    0.000    0.000    0.000 task_1.py:46(my_func2)
cProfile.run('my_func2(1000)')
#      1    0.000    0.000    0.000    0.000 task_1.py:46(my_func2)
cProfile.run('my_func2(10000)')
#      1    0.001    0.001    0.001    0.001 task_1.py:46(my_func2)


# Задача №3, мне понравилась идея с рекурсией и словарем


def my_func3(n):
    func_dict = {0: 0, 1: 1, 2: 0.5}

    def _my_func3(n, a = 1.0):
        if n in func_dict:
            return func_dict[n]
        func_dict[n] = a + _my_func3(n - 1, a / -2)
        return func_dict[n]

    return _my_func3(n)


print(timeit.timeit('my_func3(1)', number=1000, globals=globals()))  # 0.0006414000000001252 (кол-во N этементов 1)
print(timeit.timeit('my_func3(10)', number=1000, globals=globals()))  # 0.0030730000000001034 (кол-во N этементов 10)
print(timeit.timeit('my_func3(100)', number=1000, globals=globals()))  # 0.03199929999999984 (кол-во N этементов 100)
print(timeit.timeit('my_func3(500)', number=1000, globals=globals()))  # 0.16661700000000002 (кол-во N этементов 500)
print(timeit.timeit('my_func3(900)', number=1000, globals=globals()))  # 0.34961509999999985 (кол-во N этементов 900)

# Также наблюдаем линейную сложность алгоритма

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
cProfile.run('my_func3(1)')
#      1    0.000    0.000    0.000    0.000 task_1.py:80(my_func3)
#      1    0.000    0.000    0.000    0.000 task_1.py:83(_my_func3)
cProfile.run('my_func3(10)')
#      1    0.000    0.000    0.000    0.000 task_1.py:80(my_func3)
#    9/1    0.000    0.000    0.000    0.000 task_1.py:83(_my_func3)
cProfile.run('my_func3(100)')
#      1    0.000    0.000    0.000    0.000 task_1.py:80(my_func3)
#   99/1    0.000    0.000    0.000    0.000 task_1.py:83(_my_func3)
cProfile.run('my_func3(500)')
#      1    0.000    0.000    0.000    0.000 task_1.py:80(my_func3)
#  499/1    0.000    0.000    0.000    0.000 task_1.py:83(_my_func3)
cProfile.run('my_func3(900)')
#      1    0.000    0.000    0.001    0.001 task_1.py:80(my_func3)
#  899/1    0.001    0.000    0.001    0.001 task_1.py:83(_my_func3)

# Общий вывод:
# По моему мненю для данной задачи лучше подходит первая реализация через цикл for,
# хотя и цикл while тоже вполне не плохо справляется с данной задачей.
# У рекурсии маленькая вложенность до 1000 раз.
