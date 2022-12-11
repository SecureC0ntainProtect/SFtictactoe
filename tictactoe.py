import random

# Инициализация карты
field = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-', ]

# Инициализация победных линий
possible_wins = [[0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8],
                 [0, 3, 6],
                 [1, 4, 7],
                 [2, 5, 8],
                 [0, 4, 8],
                 [2, 4, 6]]


def visible_field():
    """Вывод карты на экран"""
    print(' ', 0, 1, 2, sep=' ')
    print(0, ' '.join(field[:3]))
    print(1, ' '.join(field[3:6]))
    print(2, ' '.join(field[6:]))
    print('Для того, чтобы обозначить ячейку,\nнапишите два числа через пробел в формате "x y"')


def get_coordinates(player):
    """Получаем и проверяем координаты"""
    turn = input('Введите свой ход "x y": ').split()
    if len(turn) != 2:
        print('Введите две координаты!')
        print('Для того, чтобы обозначить ячейку,\nнапишите два числа через пробел в формате "x y"')
        return get_coordinates(player)
    if not (turn[0].isdigit() and turn[1].isdigit()):
        print('Введите числа')
        return get_coordinates(player)
    x, y = map(int, turn)
    if not (0 <= x <= 2 and 0 <= y <= 2):
        print('Введите корректные координаты')
        return get_coordinates(player)
    return x, y


def converting_coordinates_2_index(x, y):
    """Конвертируем координаты в индексы"""
    return y * 3 + x


def do_step(player, marked_by_player, marker):
    """Получаем координаты, переводим в индекс, проверяем есть ли такой индекс в сделанных шагах"""
    x, y = get_coordinates(player)
    index = converting_coordinates_2_index(x, y)
    for steps in marked_by_player.values():
        if index in steps:
            print('Это место уже занято(((\n')
            return do_step(player, marked_by_player, marker)
    marked_by_player[player].append(index)
    field[index] = marker


def main():
    """Я хочу кушать. Основная функция"""
    print('Tic-Tac_Toe')
    print('Добро пожаловать, введите имена игроков:')
    player_1 = input('Игрок 1: ')
    player_2 = input('Игрок 2: ')

    if player_1 == player_2:
        print('Имена не могут быть одинаковыми.')
        return main()

    print('Это ваше игровое поле:')
    visible_field()
    random_number = random.randint(0, 1)

    if random_number:
        players = [('X', player_1), ('O', player_2)]
    else:
        players = [('X', player_2), ('O', player_1)]

    marked_by_player = {
        player_1: [],
        player_2: []
    }

    while True:
        for marker, player in players:
            print(f'{player}, ты ходишь:')

            do_step(player, marked_by_player, marker)
            visible_field()
            for possible_win in possible_wins:
                if set(possible_win).issubset(marked_by_player[player]):
                    print(f'Игрок {player} выиграл!')
                    return
            if '-' not in field:
                print('Ничья!')
                return


if __name__ == '__main__':
    main()
