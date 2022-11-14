def change_pole(pole: list, a: int, b: int, zn: str) -> tuple:
    """
    Вводим в поле новое значение
    :param pole:
    :param a:
    :param b:
    :param zn:
    :return:
    """
    new_pole = pole.copy()
    new_pole[a][b] = zn

    return new_pole


def draw(pole: list) -> None:
    """
    Рисуем начальное поле
    :param pole:
    :return:
    """
    for i in pole:
        for i1 in i:
            print(i1, end=' ')
        print()


def get_ceil_zn(pole: list, ceil_number: list[list]):
    """
    Присвоение нового значения ячейке
    :param pole:
    :param ceil_number:
    :return:
    """
    return pole[ceil_number[0]][ceil_number[1]]


def is_win(pole: list) -> bool:
    """
    Проверка выигрышной комбинации
    :param pole:
    :return:
    """
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


def get_input_cell(pole: list) -> tuple:
    """
    Проверки для ячейки, что сюда можно поставить
    :param pole:
    :return:
    """
    while True:
        # Проверка, что ввели число
        try:
            a = int(input('Введите координату 1 '))
            b = int(input('Введите координату 2 '))
        except ValueError:
            print("Нужно ввести число")
            continue  # заново запускаем цикл
        else:
            # проверка что не вышли за границы поля
            if not 0 <= a <= len(pole) or not 0 <= b <= len(pole):
                print(f"Вышли за границы поля")
                continue
        if pole[a][b] == '_':
            return a, b
        else:
            print("Ячейка занята")

def get_char_val(text: str, req_list: list) -> int:
    """
    Проверяет и возвращает строку из необходимого списка элементов
    :param text:
    :param req_list:
    :return:
    """
    while True:
        val = input(text)
        if val not in req_list:
            print(f"Значение должно лежать в {req_list}")
            continue
        return val


if __name__ == "__main__":
    """
    Запуск приложения
    :return:
    """
    pole = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]    # Создаём поле 3x3
    draw(pole)    # Рисуем начальное поле
    print()
    current_player = get_char_val("Кто первым ходит? X или 0\n", ["X", "0"])  # input Кто первый ходит
    len_field = 9
    step = 0  # счетчик числа ходов
    while True:
        a, b = get_input_cell(pole)    # Проверка ячейки
        pole = change_pole(pole, a, b, current_player)    # Вводим в поле новое значение
        draw(pole)    # Рисуем поле с новым значением
        step += 1
        if is_win(pole):    # Проверка выигрышной комбинации
            print(f"Победа игрока {current_player}")
            break
        if step == len_field:    # Проверка на ничью
            print("Ничья")
            break
        current_player = "X" if current_player == "0" else "0"




