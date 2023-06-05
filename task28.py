'''
Вводится десятичное число. Реализовать алгоритм его перевода в двоичную
систему счисления через рекурсию. Нельзя использовать функцию bin()

*Пример:*
    10
    *Вывод:*
    1010
'''

n = int(input("Введите число: "))

b = ''

while n > 0:
    b = str(n % 2) + b
    n = n // 2
print(b)



# '''
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# 2 2
# 4
# '''
#
# def sum(a, b):
#     if a == 0:
#         return b
#     return sum(a-1, b+1)    #  или  return sum(a, b-1)+1
#
#
# print(sum(int(input('Введите число (а): ')), int(input('Введите число (b): '))))