# Екимов Владимир Николаевич
# Практика 26.10.2020


from loop_in_loop import print_matrix
from random import randint


def find_len():
    matrix = [[1, 2],
              [3, 4],
              [5, 6]]

    # с помощью функции len найдите длину и ширину матрицы
    N = len(matrix)     #строки
    M = len(matrix[0])  #столбцы

    print_matrix(matrix)
    print("Размер матрицы", N, "x", M)


def my_matrix(n, m):
    """

    :param n: количество строк
    :param m: количество столбцов
    :return: двумерный массив
    """
    # matrix = [] * n

    for i in range(n):
        print()
        for j in range(m):
            print(m*i + j, end=" ")


def find_min_max_mean(n=3, m=3):
    """

    :param n: количество строк
    :param m: количество столбцов
    :return:
    """

    N = n
    M = m

    random_matrix = [[randint(1, 9) for _ in range(M)] for _ in range(N)]

    mean_value_rows = []  # здесь будут храниться средние значения для каждой строки
    min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
    min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
    max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
    max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки

    print_matrix(random_matrix)

    for row in random_matrix:
        min_index = 0
        max_index = 0
        min_value = row[min_index]  # начальное минимальное значение для каждой строки будет новое
        max_value = row[max_index]  # для максимального значения тоже самое

        for index_col, value in enumerate(row):
            if value < min_value:
                min_value = value
                min_index = index_col
            if value > max_value:
                max_value = value
                max_index = index_col

        min_value_rows.append(min_value)
        min_index_rows.append(min_index)
        max_value_rows.append(max_value)
        max_index_rows.append(max_index)
        mean_value_rows.append(round(sum(row) / len(row), 2))

    print("Минимальные значения:", min_value_rows)
    print("Индексы:", min_index_rows)
    print("Максимальные значения:", max_value_rows)
    print("Индексы:", max_index_rows)

    print("Средние значения:", mean_value_rows)


def find_min_max_mean_column(n=3, m=3):
    """

        :param n: количество строк
        :param m: количество столбцов
        :return:
        """

    N = n
    M = m

    random_matrix = [[randint(1, 9) for _ in range(M)] for _ in range(N)]

    print_matrix(random_matrix)


if __name__ == '__main__':
    # find_len()
    # my_matrix(3, 3)
    # find_min_max_mean()
    find_min_max_mean_column()
