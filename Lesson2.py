# Екимов Владимир Николаевич
# Практика 12.10.2020

# # Задача 1
#
# from random import randint
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

# Задача 3
# * Получить список цифр числа N
# * Найти сумму всех цифр

N = input("Введите число:")

# если приводим строку к списку, каждый символ попадает в отдельный элемент списка
result = [int(i) for i in list(N)]

sum_ = 0
for i in result:
    sum_ += i

print(sum_)

