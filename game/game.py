import numpy as np


N = 3
X = 'X'
O = '0'
EMPTY_CELL = '.'


def get_first_step():
    ...


def step(char):
    ...


def enemy_step(char):
    step(char)


def display_field(field):
    print(u'┌', end='')
    for i in range(N):
        print(u'─', end='')

    print(u'┐')

    for i in range(N):
        print('│', end='')
        for j in range(N):
            print(field[i, j], end='')
        print('│')

    print(u'└', end='')

    for i in range(N):
        print(u'─', end='')

    print(u'┘')

    print()




def init_field():
    field = np.full((N, N), EMPTY_CELL)
    return field


def check_win():
    ...


def main():
    field = init_field()
    display_field(field)


if __name__ == '__main__':
    main()
