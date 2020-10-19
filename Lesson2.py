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


# Задача 2

X = int(input("X:"))    # функция input() всегда возвращает строку
Y = int(input("Y:"))    # поэтому нужно использовать функцию приведения к int

if Y >= 0:
    if X >= 0:
        print("1 область")
    else:
        print("2 область")
else:   # Y < 0
    if X < 0:
        print("3 область")
    else:   # X >= 0
        print("4 область")
