from Проект.logic import init_field, is_win, has_empty_ceil
FIRST_PLAYER_SYMBOL = "X"
SECOND_PLAYER_SYMBOL = "O"

def main():
    field = init_field()
    print_field(field)

    while True:
        player_step(field, FIRST_PLAYER_SYMBOL)
        if is_win(field):
            break
        print_field(field)
        if not has_empty_ceil(field):
            break

        enemy_step(field, SECOND_PLAYER_SYMBOL)
        if is_win(field):
            break
        print_field(field)
        if not has_empty_ceil(field):
            break


def get_first_player():
    ...


def chang_players():
    ...


def print_field(field: list[list]):
    ...
    print()


def player_step(field, player_symbol):
    x = int(input("Введите x"))
    y = int(input("Введите y"))
    is_empty_ceil(field, (x, y))

def enemy_step(field, player_symbol):
    player_step(field, player_symbol)


