# write your code here

def print_line(line):
    out = '| '
    for i in line:
        out += i + ' '
    out += '|'
    print(out)


def win(board, winner):
    win_pattern = winner * 3
    row1 = board[:3]
    row2 = board[3:6]
    row3 = board[6:]
    col1 = board[0::3]
    col2 = board[1::3]
    col3 = board[2::3]
    diag1 = board[0::4]
    diag2 = board[2::2][:3]
    return win_pattern in [row1, row2, row3, col1, col2, col3, diag1, diag2]


def impossible(board):
    x = board.count('X')
    o = board.count('O')

    return abs(x - o) > 1 or (win(board, 'X') and win(board, 'O'))


def print_board(board):
    print('---------')
    for board_line in [(board[:3]), (board[3:6]), (board[6:])]:
        print_line(board_line)
    print('---------')


def occupied(board, x, y):
    row3 = board[6:]
    board = [(board[:3]), (board[3:6]), row3]
    position = board[y - 1][x - 1]
    return position in ['X', 'O']


def out_of_bounds(x, y):
    return x > 3 or y > 3


def game_finished(board):
    return win(board, 'X') or win(board, 'Y') or board.find(' ') < 0


def print_result(board):
    if impossible(board):
        print('Impossible')
    elif win(board, 'X'):
        print('X wins')
    elif win(board, 'O'):
        print('O wins')
    elif not game_finished(board):
        print('Game not finished')
    else:
        print('Draw')


def occupy(board, player, x, y):
    index = (y - 1) * 3 + x - 1
    return board[:index] + player + board[index + 1:]


def make_move(board, player):
    error = True
    while error:
        coordinates = input('> ').strip().split()
        if not all(e.isdigit() for e in coordinates):
            print('You should enter numbers!')
            continue
        y, x = [int(i) for i in coordinates]
        if out_of_bounds(x, y):
            print('Coordinates should be from 1 to 3!')
            continue
        elif occupied(board, x, y):
            print('This cell is occupied! Choose another one!')
            continue
        else:
            board = occupy(board, player, x, y)
            print_board(board)
            error = False
    return board


def main():
    board = ' ' * 9
    print_board(board)
    current_player = 'X'
    while not game_finished(board):
        print(f'Current player is {current_player}')
        board = make_move(board, current_player)
        current_player = 'X' if current_player in ['O', ''] else 'O'
    print_result(board)


main()
