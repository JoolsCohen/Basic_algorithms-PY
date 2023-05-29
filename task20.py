"""
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:

● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.

А русские буквы оцениваются так:

● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.

Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только
английские, либо только русские буквы.

Ввод:
ноутбук

Вывод:
12

"""

global_dict = {'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'C': 1, 'Т': 1, 'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
               'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2, 'D': 2, 'G': 2,
               'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3, 'B': 3, 'C': 3, 'M': 3, 'P': 3,
               'Й': 4, 'Ы': 4, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
               'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5, 'K': 5,
               'Ш': 6, 'Э': 6, 'Ю': 6, 'J': 6, 'X': 6,
               'Ф': 7, 'Щ': 7, 'Ъ': 7, 'Q': 7, 'Z': 7}

string = input('Введите слово: ').upper()
result = 0
for item in string:
    result += global_dict[item]
print(result)

# 2 вариант решения задачи
#
# points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP',
#              4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
# points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ',
#              4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
# word = input('Введите слово: ').upper()  # upper переводит все буквы в верхний регистр
# count = 0
# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in points_en:
#             if i in points_en[j]:
#                 count = count + j
#     else:
#         for j in points_ru:
#             if i in points_ru[j]:
#                 count = count + j
# print(count)




