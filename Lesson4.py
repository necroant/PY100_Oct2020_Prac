# Екимов Владимир Николаевич
# Практика 29.10.2020


# def pow_n(a, n):
#     i = 0
#     result = 1
#     while True:
#         result *= a
#         i += 1
#         if i >= n:
#             break
#     return result
#
#
# def factorial(a):
#     result = 1
#     for i in range(1, a+1):
#         result *= i
#
#     return result
#
#
# def check_pow_2(n):
#     if n < 0:
#     while True:
#         if n % 2 != 0:
#             return False
#         n /= 2
#
#         if n == 1:
#             return True
#         elif n < 1:
#             return False


def dec_to_binary(n):
    result = []
    while True:
        result.append(n % 2)
        n //= 2
        if n <= 1:
            result.append(n)
            break

    return "".join(str(i) for i in result[::-1])     # или result.reverse()


if __name__ == '__main__':
    # print(pow_n(2, 10))
    # print(factorial(5))
    # print(dec_to_binary(34))
    # for i in range(1,17):
    #     print(f"{i:>2}:0х{dec_to_binary(i):>7}")
    for i in range(1, 17):
        print(f"{i:>2}:0х{i:b}")    # встроенное форматирование


    # домашнее задание
    # Подсчитать частоту вхождений в некий текст каждой из букв