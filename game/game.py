import numpy as np
from random import choice


N = 3       # field size

FIRST_PLAYER = 'x'
SECOND_PLAYER = 'o'
EMPTY_CELL = '.'

INIT_FIELD_SET = {
    2: (
        '0', '1',
        '2', '3'
    ),
    3: (
        '0', '1', '2',
        '3', '4', '5',
        '6', '7', '8'
    ),
    4: (
        '0', '1', '2', '3',
        '4', '5', '6', '7',
        '8', '9', 'A', 'B',
        'C', 'D', 'E', 'F'
    ),
}


def get_first_step():
    if choice([FIRST_PLAYER, SECOND_PLAYER]) == FIRST_PLAYER:
        return FIRST_PLAYER, SECOND_PLAYER
    else:
        return SECOND_PLAYER, FIRST_PLAYER



def step(char, field):
    while True:
        cell = input(f"<{char}> Введите координату ячейки: ")
        cell.upper()
        if cell in field and cell != FIRST_PLAYER and cell != SECOND_PLAYER:
            row, col = find_index_cell(cell, field)
            field[row, col] = char
            break
        print("Введите корректную ячейку!")

    return field




def find_index_cell(char, field):
    """
    :param char: Character in the field
    :param field: Field in which to look
    :return: x, y coordinates on the field
    """
    for i in range(N):
        for j in range(N):
            if field[i, j] == char:
                return i, j


def enemy_step(char, field):
    return step(char, field)


def display_field(field):
    print()
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
    # # Через жопу
    # field = np.full((N, N), EMPTY_CELL)
    #
    # for index, value in enumerate(FIELD_SET[N]):
    #     row = index // N
    #     col = index % N
    #     field[row, col] = FIELD_SET[N][index]

    # По-человечески
    field = np.array(INIT_FIELD_SET[N])
    field.resize(N, N)

    return field


def check_sequence(list_, char):
    for value in list_:
        if value != char:
            return False

    return True


def check_win(field, char):
    victory = False

    for row in field:                           # Проверяем строки
        if check_sequence(row, char):
            victory = True

    if check_sequence(field.diagonal(), char):  # Проверяем главную диагональ
        victory = True

    r90 = np.rot90(field)
    for col in r90:                             # Проверяем столбцы
        if check_sequence(col, char):
            victory = True

    if check_sequence(r90.diagonal(), char):    # Проверяем побочную диагональ
        victory = True

    return victory


def display_victory_screen(field):
    for i in range(N):
        for j in range(N):
            if field[i, j] in INIT_FIELD_SET[N]:
                field[i, j] = EMPTY_CELL

    display_field(field)


def main():
    field = init_field()
    display_field(field)
    current_player, other_player = get_first_step()
    player_dict = {
        current_player: step,
        other_player: enemy_step
    }
    while True:
        field = player_dict[current_player](current_player, field)
        if check_win(field, current_player):
            print(f"Игрок <{current_player}> выиграл")
            break
        display_field(field)
        current_player, other_player = other_player, current_player

    display_victory_screen(field)


if __name__ == '__main__':
    main()
