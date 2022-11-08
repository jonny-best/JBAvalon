def change_pole(pole, a, b, zn):
    new_pole = pole.copy()
    new_pole[a][b] = zn

    return new_pole


def draw(pole):
    for i in pole:
        for i1 in i:
            print(i1, end=' ')
        print()


def get_ceil_zn(pole, ceil_number):
    return pole[ceil_number[0]][ceil_number[1]]


def is_win(pole):
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

    len_win = len(win_comb[0])  # определили выигрышную длину
    for comb in win_comb:
        first_cell = get_ceil_zn(pole, comb[0])  # определяем кто стоит на первой клетки выигрышной линии
        count = 1  # число совпадений на линии
        for cell in comb[1:]:  # итерируемся от 2-ой до последней клетки выигрышной линии
            value_cell = get_ceil_zn(pole, cell)
            if value_cell == first_cell:  # если значение ячейки совпадает с первой ячейкой
                count += 1
        if count == len_win and value_cell != "_":  # если число совпадений на линии равно искомому и ячейка не пустая
            return True  # возвращаем выигрыш
    return False  # если за время поиска не было ниодного выигрыша, то возвращаем False


def player_torn(pole, a, b, zn):
    pole = change_pole(pole, a, b, zn)
    draw(pole)
    return pole

def none_comb(pole):
    while True:
        len_none_comb = 0
        count = 0
        none_ceil = "_"
        for i in [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]:
            len_none_comb += len(i)
            for j in i:
                if j != none_ceil:
                    count += 1
        if count == len_none_comb:
            return False

if __name__ == "__main__":
    pole = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    draw(pole)
    print()
    while True:
        if not is_win(pole):
            player_torn(pole, a = int(input('Введите координату 1 ')), b = int(input('Введите координату 2 ')),
                    zn=input('Введите значение '))
            print("Победа")
        if none_comb is False:
            print("Ничья")
        else:
            continue



