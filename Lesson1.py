# Екимов Владимир Николаевич
# Практика 12.10.2020

# # имя переменной должно отличаться от имени встроенной функции, а то потеряем функционал
# list_ = list(range(1, 10, 2))
#
# print(list_)

# # Задание 1
# # * Создать список, заполненый целыми числами от N, M с шагом STEP при помощи функции `range`
#
# N = 0
# M = -30
# STEP = -6
#
# print(list(range(N, M, STEP)))

# # Задание 2
# # * Создать список квадратов целых чисел от n до m
#
# n = 1
# m = 10
#
# # цикл for может перебирать что элементы list() что элементы range(), без разницы
# list_ = [i **2 for i in range(n, m + 1)]
#
# print(list_)

# # Задание 3
# # * Создать список квадратов нечетных целых чисел от n до m
#
# n = 1
# m = 10
#
# # оператор % возвращает остаток от деления
# list_ = [i ** 2 for i in range(n, m + 1) if i % 2 == 1]
#
# print(list_)

# # Задание 3*
#
# n = 1
# m = 10
#
# # Ключи сделаю типа Строка, потому что могу
# dict_ = {str(i): i ** 2 for i in range(n, m + 1) if i % 2 == 1}
#
# print(dict_)

# # Задание 4
# # * Ввести массив, состоящий из 14 элементов целого типа. Найти количество элементов четных по значению.
#
# range_ = range(14)
# array = [i for i in range_ if i % 2 == 0]
#
# print(array)
# print(len(array))

# # Задание 4*
# # Посчитать сколько положительных чисел в таком списке
#
# range_ = range(-1000, 1000)
# array = [i for i in range_ if i > 0]
#
# print(len(array))

# #Задание 5
# # * Ввести массив, состоящий из 12 элементов целого типа. Получить новый массив, заменив значение
# # пятого элемента среднеарифметическим исходного массива.
#
# range_ = range(12)
# array = [i for i in range_]
# number_of_elements = len(array)
#
# # Если непонятно чего делает функция sum() устанавливаем на нее курсор и жмем Ctrl+q
# sum_ = sum(array)
#
# new_array = array
# new_array[4] = sum_ / number_of_elements
#
# print(new_array)

# #Задание 5*
# # * Ввести массив, состоящий из 12 элементов целого типа. Получить новый массив, заменив значение
# # пятого элемента среднеарифметическим исходного массива.
#
# range_ = range(12)
# array = [i for i in range_]
#
# # Получить среднее арифметическое только от четных элементов исходного массива и подставить в него же
# new_array = [i for i in array if i % 2 == 0]
# sum_ = sum(new_array)
# number_of_elements = len(new_array)
#
# array[4] = sum_ / number_of_elements
#
# print(array)

# # Задание 6
# # * Задан целочисленный массив, состоящий из 11 элементов. Найти количество элементов, абсолютное
# # значение которых больше среднего арифметического.
#
# array = list(range(-5, 6))
#
# num_ = 0
# average = sum(array) / len(array)
#
# for i in array:
#     if abs(i) > average:  # abs() возвращает значение числа по модулю
#         num_ += 1
#
# print(num_)

# # Домашняя практика
# # * Дано двухзначное число. Определить: входит ли в него цифра 5.
#
# num = 23
# find_num = 5
# num_as_list = [int(s) for s in list(str(num))]
# # print(num_as_list)
#
# if find_num in num_as_list:
#     print('Yep!')
# else:
#     print("Nope!")

# # Домашняя практика 2
# # * Ввести с клавиатуры число и цифру
# # * Определить: входит ли цифра в число
#
# num = int(input('Число > '))
# find_num = int(input('Цифра > '))
# num_as_list = [int(s) for s in list(str(num))]
#
# if find_num in num_as_list:
#     print('Yep!')
# else:
#     print("Nope!")
