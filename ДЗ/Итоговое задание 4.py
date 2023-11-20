# Задача 4. Крестики нолики
# Напишите программу, которая реализует игру Крестики-нолики.
# Ваши классы в этой задаче могут выглядеть так:
#
# class Cell:
#    #  Клетка, у которой есть значения
#    #   - занята она или нет
#    #   - номер клетки
#
# class Board:
#    #  Класс поля, который создаёт у себя экземпляры клетки
#
# class Player:
#    #  У игрока может быть
#    #   - имя
#    #   - на какую клетку ходит
# Сделать классами


ALL_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
X, O, BLANK = 'X', 'O', ' '


def main():
    print('Вас приветствует игра "Крестики-Нолики"!')
    game_board = get_blank_board()
    current_player, next_player = X, O

    while True:
        print(get_board_str(game_board))

        move = None
        while not is_valid_space(game_board, move):
            print('Какой у {}\' ход? (1-9)'.format(current_player))
            move = input('> ')
        update_board(game_board, move, current_player)

        if is_winner(game_board, current_player):
            print(get_board_str(game_board))
            print(current_player + ' победил в игре!')
            break
        elif is_board_full(game_board):  # Проверяем на ничью.
            print(get_board_str(game_board))
            print('В игре ничья!')
            break
        current_player, next_player = next_player, current_player
    print('Спасибо за игру!')


# class Board:

def get_blank_board():
    board = {}
    for space in ALL_SPACES:
        board[space] = BLANK  # Все клетки начинаются в пустом состоянии.
    return board


def get_board_str(board):
    return '''
        {}|{}|{}    1 2 3
        -+-+-
        {}|{}|{}    4 5 6
        -+-+-
        {}|{}|{}    7 8 9'''.format(board['1'], board['2'], board['3'],
                                    board['4'], board['5'], board['6'],
                                    board['7'], board['8'], board['9'])


def is_valid_space(board, space):
    """Возвращает True, если space на board представляет собой допустимый номер клетки, причем эта клетка пуста."""
    return space in ALL_SPACES and board[space] == BLANK


def is_winner(board, player):
    """Возвращает True, если игрок player победил на этой доске."""
    b, p = board, player

    return ((b['1'] == b['2'] == b['3'] == p) or  # Верхняя строка
            (b['4'] == b['5'] == b['6'] == p) or  # Средняя строка
            (b['7'] == b['8'] == b['9'] == p) or  # Нижняя строка
            (b['1'] == b['4'] == b['7'] == p) or  # Левый столбец
            (b['2'] == b['5'] == b['8'] == p) or  # Средний столбец
            (b['3'] == b['6'] == b['9'] == p) or  # Нижний столбец
            (b['3'] == b['5'] == b['7'] == p) or  # Диагональ
            (b['1'] == b['5'] == b['9'] == p))  # Диагональ


def is_board_full(board):
    """Возвращает True, если все клетки на доске заполнены."""
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False  # Если хоть одна клетка пуста — возвращаем False.
    return True  # Незаполненных клеток нет, возвращаем True.


def update_board(board, space, mark):
    """Присваиваем клетке (space) на доске (board) значение (mark)."""
    board[space] = mark


if __name__ == '__main__':
    main()  # Вызываем main(), если этот модуль не импортируется,
    # а запускается.
