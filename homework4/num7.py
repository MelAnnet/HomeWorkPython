# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.
from math import factorial
def numbers_range(n):
    for i in range(n):
        yield factorial(i)
count = 6
a = numbers_range(count)
for i in range(count):
    print(next(a))
