# Пройтись по своим предыдущим ДЗ и где возможно использовать ускореную обработку данных
# (достаточно 3 примеров)


# Задача 1. Задайте список из n чисел последовательности (1 + 1/n)^n. Вывести консоль сам список и сумму его элементов.

#1. Способ оригинал

# n = int(input('Введите количество чисел: '))
# my_list = []
# for i in range(1, n + 1):
#     my_list.append(round((1 + 1/i) ** i, 2))
# print(my_list)
# sum = 0
# for i in range(len(my_list)):
#     sum += my_list[i]
# print(f'Сумма элементов списка = {sum}')

#2. Способ с list Comprehension

# n = int(input('Введите количество чисел: '))
# my_list = []
# my_list = [i for i in range(1, n)]
# print(my_list)
# sum = 0
# for i in range(len(my_list)):
#     sum += my_list[i]
# print(f'Сумма элементов списка = {sum}')


# Задача 2.Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

#1. Способ

from random import uniform

# size = int(input('Введите размер списка '))
# my_list = []
# for i in range(size):
#     i = uniform(0, 10)
#     my_list.append(round(i, 2))
# print(my_list)
# new_list = []
# for i in my_list:
#     i = i % 1
#     new_list.append(round(i,2))
# print(new_list)
# min = new_list[0]
# max = 0
# for i in range(len(new_list)):
#         if max < new_list[i]:
#             max = new_list[i]
#         if min > new_list[i]:
#              min = new_list[i]
# dif = max - min
# print(f'max = {max}, min = {min}')
# print(f'Разница между max и min = {(round(dif, 2))}')


#2. Способ с использованием функций map и lambda

# size = int(input('Введите размер списка '))
# my_list = []
# for i in range(size):
#     i = uniform(0, 10)
#     my_list.append(round(i, 2))
# print(my_list)
# new_list = []
# l = list(map(lambda i: round(i%1, 2), my_list))
# new_list = l
# print(new_list)
# min = new_list[0]
# max = 0
# for i in range(len(new_list)):
#         if max < new_list[i]:
#             max = new_list[i]
#         if min > new_list[i]:
#              min = new_list[i]
# dif = max - min
# print(f'max = {max}, min = {min}')
# print(f'Разница между max и min = {(round(dif, 2))}')


# Задача 3.

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import random
#
# # 1 способ
#
# size = int(input('Введите размер списка: '))
# my_list = []
# for i in range(size):
#     my_list.append(random.randint(0, 10))
# print(my_list)
# sum = 0
# count = 0
# for i in my_list:
#     if count % 2 == 1:
#         sum += i
#     count += 1
# print(f'Сумма чисел с нечетными индексами равна = {sum}')

# 2 способ

# size = int(input('Введите размер списка: '))
# my_list = []
# for i in range(size):
#     my_list.append(random.randint(0, 10))
# print(my_list)
# list = [my_list[index] for index in range(1, len(my_list) + 1, 2)]
# print(f'Сумма чисел с нечетными индексами равна = {sum(list)}')



