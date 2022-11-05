
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
    ceil_zn = pole(ceil_number)

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
    for i in range(3):
        coord_1 = win_comb[i][i + 0]
        coord_2 = win_comb[i][i + 1]
        coord_3 = win_comb[i][i + 2]
        ceil_1 = get_ceil_zn(pole, coord_1)
        ceil_2 = get_ceil_zn(pole, coord_2)
        ceil_3 = get_ceil_zn(pole, coord_3)
        if ceil_1 != ceil_2 != ceil_3:
            return True
        else:
            print("WIN")
        break

if __name__ == "__main__":
    pole = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    draw(pole)
    print()
    if is_win(pole):
        pole = change_pole(pole, 0, 0, "X")
        draw(pole)
        print()
    if is_win(pole):
        pole = change_pole(pole, 0, 1, "O")
        draw(pole)
        print()
