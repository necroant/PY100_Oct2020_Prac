# Екимов Владимир Николаевич
# Практика 12.10.2020

from random import randint

# # Задача 1
#
#
# N = -10  # нижняя граница
# M = 10   # верхняя граница
# K = 5    # сколько у нас будет случайных чисел
#
# list_ = [randint(N, M) for i in range(K)]
#
# pos = []
# neg = []
#
# # print(list_)
#
# for value in list_:
#     if value > 0:
#         pos.append(value)
#     else:
#         neg.append(value)
#
# print(pos, neg)


# # Задача 2
# # Полярный медведь это декартов медведь после преобразования координат
#
# X = int(input("X:"))    # функция input() всегда возвращает строку
# Y = int(input("Y:"))    # поэтому нужно использовать функцию приведения к int
#
# if Y >= 0:
#     if X >= 0:
#         print("1 область")
#     else:
#         print("2 область")
# else:   # Y < 0
#     if X < 0:
#         print("3 область")
#     else:   # X >= 0
#         print("4 область")
#
# Есличесн 4 условия через elif на одном уровне иерархии было бы нагляднее
#
# if X > 0 and Y > 0:
#     print("1 область")
# elif Y > 0 > X:
#     print("2 область")
# elif X < 0 and Y < 0:
#     print("3 область")
# elif Y < 0 < X:
#     print("4 область")
# else:
#     print("Точка находится на координатной оси")

# # Задача 3
# # * Получить список цифр числа N
# # * Найти сумму всех цифр
#
# N = input("Введите число:")
#
# # если приводим строку к списку, каждый символ попадает в отдельный элемент списка
# result = [int(i) for i in list(N)]
#
# sum_ = 0
#
# # for i in result:  # это в лоб
# #     sum_ += i
#
# sum_ = sum(result)  # это встроенной функцией
#
# print(sum_)

# # Задача 4
# # * Получить список цифр числа N
# # * Найти сумму четных всех цифр
#
# N = input("Введите число:")
#
# # если приводим строку к списку, каждый символ попадает в отдельный элемент списка
# result = [int(i) for i in list(N) if int(i) % 2 == 0]
#
# sum_ = 0
#
# # for i in result:  # это в лоб
# #     sum_ += i
#
# sum_ = sum(result)  # это встроенной функцией
#
# print(sum_)

# # Задача 5
# # * Получить список цифр числа N
# # * Найти минимальную (максимальную) цифру числа
#
# N = input("Введите число:")
#
# # если приводим строку к списку, каждый символ попадает в отдельный элемент списка
# result = [int(i) for i in list(N)]
#
# min_ = result[0]
# max_ = result[0]
#
# for i in result:
#     min_ = min(min_, i)
#     max_ = max(max_, i)
#
# # или
#
# min_ = min(result)  # функции min и max умеют искать в списке
# max_ = max(result)
#
# print(min_, max_)

# # Задача 6
# # * Получить список цифр числа N
# # * Найти разность первой и последней цифры
#
# N = input("Введите число:")
#
# # если приводим строку к списку, каждый символ попадает в отдельный элемент списка
# result = [int(i) for i in list(N)]
#
# sub = result[0] - result[-1]    # вот так совсем красиво, нулевой индекс для 1 элемента, -1 для последнего

# # Задача 7
# # * Найти минимальное (максимальное) число в массиве и в какой позиции оно находится
#
# # _ потому что переменная-итератор нам не нужна
# # мы просто хотим выполнить цикл N раз
#
# N = 10
# rand_list = [randint(-10, 10) for _ in range(N)]
#
# pos = 0
# max_value = rand_list[pos]
#
# for i in range(len(rand_list)):
#     if rand_list[i] > max_value:
#         max_value = rand_list[i]
#         pos = i
#
# print(max_value)    # выводим максимальный элемент
# print(pos)          # позиция макс. элемента

# # Задача 8
# # * Найти минимальное (максимальное) число в массиве и в какой позиции оно находится
# # * использовать enumerate(), не через жопу как в задаче 7
#
# # _ потому что переменная-итератор нам не нужна
# # мы просто хотим выполнить цикл N раз
#
# N = 10
# rand_list = [randint(-10, 10) for _ in range(N)]
#
# pos = 0
# max_value = rand_list[pos]
#
# # функция enumerate позволяет составить кортеж из пар индекс-значение для перечисляемого элемента
# # данная функция работает со всеми итерируемыми объектами
# for i, value in enumerate(rand_list):
#     if value > max_value:
#         max_value = value
#         pos = i
#
# print(max_value)    # выводим максимальный элемент
# print(pos)          # позиция макс. элемента

# # Задача 9
# # * Найти 2 наименьших числа в массиве
#
# N = 10
# rand_list = [randint(-10, 10) for _ in range(N)]
#
# min1 = rand_list[0]
# min2 = rand_list[1]
#
# if min1 > min2:     # в первой переменной будет храниться самое меньшее значение, во второй следующее с конца
#     min1, min2 = min2, min1
#
# # передвигаем минимальный элемент во 2 позицию, записываем новый минимальный в первую
# for current_value in rand_list[2:]:
#     if current_value < min1:
#         min1, min2 = current_value, min1

# # Задача 10
# # *Дан массив целых чисел из N элементов. Найти индекс последнего минимального элемента.
#
# N = 30
# rand_list = [randint(-10, 10) for _ in range(N)]
#
# pos = 0
# min_value = rand_list[pos]
#
# for i, value in enumerate(rand_list):
#     if value <= min_value:
#         min_value = value
#         pos = i
#
# print(pos)

# # Задача 11
# # *Подсчитать среднее арифметическое положительных и отрицательных элементов в массиве.
#
# N = 10
# rand_list = [randint(-10, 10) for _ in range(N)]
#
# #--------------------Вариант 1--------------------
# positive = 0
# q_pos = 0
# negative = 0
# q_neg = 0
#
# for value in rand_list:
#     if value > 0:
#         positive += value
#         q_pos += 1
#     elif value < 0:
#         negative += value
#         q_neg += 1
#
# print(positive / q_pos)
# print(negative / q_neg)
#
# # --------------------Вариант 2--------------------
# positive = [i for i in rand_list if i > 0]
# negative = [i for i in rand_list if i < 0]
#
# print(sum(positive) / len(positive))
# print(sum(negative) / len(negative))


# # Задача 12
# # *В данном массиве найдите наибольшую серию подряд идущих элементов, расположенных по возрастанию.
#
# N = 10
# rand_list = [randint(0, 10) for _ in range(N)]
# cur_sequence = 1
# max_sequence = 1
#
# for i in range(1, len(rand_list)):
#     if rand_list[i] > rand_list[i-1]:
#         cur_sequence += 1
#     else:
#         max_sequence = cur_sequence
#         cur_sequence = 1
#
# # костыль на случай если последовательность в конце массива окажется самой длинной
# max_sequence = cur_sequence if cur_sequence > cur_sequence else max_sequence
#
# print(rand_list)
# print(max_sequence)


# Задача 13
# *Вывести первые 3 отрицательных значения из списка

N = 6
rand_list = [randint(-10, 10) for _ in range(N)]

negatives = []

for value in rand_list:
    if value < 0:
        negatives.append(value)
        print("negative value found, appending list")
    if len(negatives) == 3:
        print("total of 3 negative values found, ending search")
        break

# обратите внимание - break прерывает выполнение именно цикла, и вне его не работает
# интерпретатор подавится если написать break например в теле функции

if len(negatives) < 3:
    print("3 negatives not found, eat shit")

print(negatives)
