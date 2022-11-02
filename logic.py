
def set_ceil(field: list[list], ceil_number, player_symbol):
    """
    Установка значения в ячейку

    :param field:
    :param ceil_number:
    :param player_symbol:
    :return:
    """
    ...

def get_ceil(field: list[list], ceil_number):
    ...

def is_empty_ceil(field, ceil_number: tuple) -> bool:
    """
    Проверка занятости конкретной ячейки

    :param field:
    :param ceil_number:
    :return: Ячейка пуста или нет
    """
    for row in field:
        if ceil in row:
            if ceil is EMPTY_CEIL:
                return True
    return False

EMPTY_CEIL = None

def init_field(size: int = 3) -> list[list]:
    """
    Инициализация поля

    :param size: Размер поля
    :return:Поле, заполненное пустыми ячейками
    """
    return[
        [EMPTY_CEIL] * size for _ in range(size)
    ]


def is_win(field):
    win_comb = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(2, 0), (1, 1), (0, 2)]
    ]

    for i in range(3):

        coord_1, coord_2, coord_3 = ..., ..., ...
        ceil_1 = get_ceil(field, coopd_1)
        ceil_2 = get_ceil(field, coopd_2)
        ceil_3 = get_ceil(field, coopd_3)

        if ceil_1 == ceil_2 == ceil_3 != EMPTY_CEIL:
        return True

# main logic
field = init_field()
print(field)