'''
Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз
каждый символ уже встречался. Количество повторов добавляется к символам с помощью
постфикса формата _n.

Input: a a a b c a a d c d d

Output: a_0 a_1 a_2 b_0 c_0 a_3 a_4 d c_1 d_1 d_2

Для решения данной задачи используйте функцию split()
'''

s = 'a a a b c a a d c d d'
s = s.split()
print(s)
final_string = ''
for i in range(len(s)):
    if s[0:i].count(s[i]) == 0:
        final_string += f' {s[i]}'
    else:
        final_string += f' {s[i]}_{s[0:i].count(s[i])}'
print(final_string)


# word = input("Введите строку: ").split()
# result = {}
# for i in word:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#         result[i] += 1
#     else:
#         print(i, end=' ')
#         result[i] = 1





# line = input('Введите символы строки через пробел: ').split() # создаем список, пользователь вводит
# res = {}                                                      # создаем словарь
# for i in line:                                                # циклом по списку
#     if i in res:                                              # заполняем словарь, где символ=ключ
#         print(f'{i}_{res[i]}', end='  ')
#     else:
#         print(f'{i}_{0}', end='  ')
#     res[i] = res.get(1, 0)+1
# # print(res) {'d': 1, 'f': 1, 's': 1, 'g': 1, 'e': 1, 't': 1, 'l': 1}