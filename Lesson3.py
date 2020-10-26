# Екимов Владимир Николаевич
# Практика 26.10.2020


from loop_in_loop import print_matrix


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


def find_min_max_mean():


if __name__ == '__main__':
    # find_len()
    # my_matrix(3, 3)
