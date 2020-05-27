# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.

# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
import timeit
import cProfile


def sieve_func(idx):
    if idx == 1:
        return 2
    n = idx ** 2
    sieve = [i for i in range(n + 1)]
    sieve[1] = 0

    for i in range(2, n + 1):
        if sieve[i] != 0:
            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i
    result = [i for i in sieve if i != 0]
    return result[idx - 1]


print(timeit.timeit('sieve_func(1)', number=1000, globals=globals()))  # 0.00012209999999999999 (кол-во N этементов 1)
print(timeit.timeit('sieve_func(10)', number=1000, globals=globals()))  # 0.0300947 (кол-во N этементов 10)
print(timeit.timeit('sieve_func(100)', number=1000, globals=globals()))  # 4.7531839 (кол-во N этементов 100)

# Сложность O(n**4)

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
cProfile.run('sieve_func(1)')
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 task_2.py:11(sieve_func)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('sieve_func(10)')
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 task_2.py:11(sieve_func)
#      1    0.000    0.000    0.000    0.000 task_2.py:15(<listcomp>)
#      1    0.000    0.000    0.000    0.000 task_2.py:24(<listcomp>)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('sieve_func(100)')


#      1    0.000    0.000    0.006    0.006 <string>:1(<module>)
#      1    0.005    0.005    0.006    0.006 task_2.py:11(sieve_func)
#      1    0.001    0.001    0.001    0.001 task_2.py:15(<listcomp>)
#      1    0.000    0.000    0.000    0.000 task_2.py:24(<listcomp>)
#      1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

def prime_func(idx):
    n = 2
    prime_num = 0
    prime_idx = 0

    while prime_idx < idx:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            prime_num = n
            prime_idx += 1
        n += 1
    return prime_num


print(timeit.timeit('prime_func(1)', number=1000, globals=globals()))  # 0.0004476000000002145 (кол-во N этементов 1)
print(timeit.timeit('prime_func(10)', number=1000, globals=globals()))  # 0.01999070000000014 (кол-во N этементов 10)
print(timeit.timeit('prime_func(100)', number=1000, globals=globals()))  # 1.9111681000000003 (кол-во N этементов 100)

# По всей видимости мы видим сложность O(n**2)

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
cProfile.run('prime_func(1)')
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 task_2.py:59(prime_func)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('prime_func(10)')
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 task_2.py:59(prime_func)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('prime_func(100)')
#      1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#      1    0.002    0.002    0.002    0.002 task_2.py:59(prime_func)
#      1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Во втором варианте мы видим по 3 точкам, что код оптимизирован в 2 раза.
