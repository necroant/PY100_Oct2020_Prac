import numpy as np


N = 3
X = 'X'
O = '0'
EMPTY_CELL = '.'

FIELD_SET = {
    2:(
        '0','1',
        '2','3'
    ),
    3:(
        '0','1','2',
        '3','4','5',
        '6','7','8'
    ),
    4:(
        '0','1','2','3',
        '4','5','6','7',
        '8','9','A','B',
        'C','D','E','F'
    ),
}

def get_first_step():
    ...


def step(char, field):
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


def init_field():
    # field = np.full((N, N), EMPTY_CELL)
    #
    # for index, value in enumerate(FIELD_SET[N]):
    #     row = index // N
    #     col = index % N
    #     field[row, col] = FIELD_SET[N][index]

    field = np.array(FIELD_SET[N])
    field.resize(N,N)

    return field


def check_win():
    ...


def main():
    field = init_field()
    display_field(field)


if __name__ == '__main__':
    main()
