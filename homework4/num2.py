# 2. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

list = [11,52,44,85,12,11,45,3,66,95,21,53,25,62,65,56,32,14,12]
a = [i for i in list if i > list[list.index(i)-1]]
print(a)