'''
По данному целому неотрицательному n вычислите значение n!.
N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
Решить задачу используя цикл while

Input: 5

Output: 120
'''

print('Введите целое неотрицательное число N: ')
n = int(input())
factotial = 1
while n > 1:
    factotial *= n
    n -= 1
print(f'Факториал N равен {factotial}')