'''
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах. Пользователь вводит 2 числа:
n - кол-во элементов первого множества, m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.

Input
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18

Output
6 12
'''
# Первое решение через метод
import random
n, m = map(int, input('Сколько элементов в 1 и 2 наборе чисел? Вводим через "пробел": ').split())
def intersection_list(list1, list2):
    return list(set(list1) & set(list2))
print('Введите первый набор чисел через "пробел": ')
list1 = [int(i) for i in input().split()]
# list1 = [random.randrange(1, 50, 1) for i in range(n)]
print(list1)
print('Введите второй набор чисел через "пробел": ')
list2 = [int(i) for i in input().split()]
# list2 = [random.randrange(1, 50, 1) for i in range(m)]
print(list2)
print(*sorted(intersection_list(list1, list2)))

#Второе решение
import random
# n, m = map(int, input('Сколько элементов в 1 и 2 наборе чисел? Вводим через "пробел": ').split())
# list1 = []
# print('Введите первый набор чисел через "пробел": ')
# # list1 = [int(i) for i in input().split(, )] # лень постоянно набирать числа, поэтому прописала рандом
# list1 = [random.randrange(1, 50, 1) for i in range(n)]
# print(list1)
# list2 = []
# print('Введите второй набор чисел через "пробел": ')
# # list2 = [int(i) for i in input().split(, )] # лень постоянно набирать числа, поэтому прописала рандом
# list2 = [random.randrange(1, 50, 1) for i in range(n)]
# print(list2)
# set1 = set(list1)
# set2 = set(list2)
# set_inter = set1.intersection(set2) # intersection возвращает новое множество, со всеми элементами к-ые есть и в 1 и во 2 множестве
# print('Во введенных наборах встречаются числа: ', end='')
# print(*sorted(set_inter))
