# The first player has to play as X and the second player plays as O.

grid = [[' ' for row in range(3)] for i in range(3)]


def game_grid():
    print('---------')
    print(f'| {grid[0][0]} {grid[0][1]} {grid[0][2]} |')
    print(f'| {grid[1][0]} {grid[1][1]} {grid[1][2]} |')
    print(f'| {grid[2][0]} {grid[2][1]} {grid[2][2]} |')
    print('---------')


def move(tic_tac_toe):
    while True:
        try:
            coordinates = [int(i) for i in input().split()]
            if len(coordinates) == 2:
                x, y = coordinates[0] - 1, coordinates[1] - 1  # convert to indexes
                if x not in [0, 1, 2] or y not in [0, 1, 2]:
                    print('Coordinates should be from 1 to 3!')
                    continue
            else:
                continue

        except ValueError:
            print('You should enter numbers!')

        else:
            if grid[x][y] != ' ':
                print('This cell is occupied! Choose another one!')
                continue

            grid[x][y] = tic_tac_toe
            game_grid()
            return


def game_end():
    count_x = len([j for row in grid for j in row if j == 'X'])
    count_o = len([j for row in grid for j in row if j == 'O'])

    if abs(count_x - count_o) in [0, 1]:

        # winning lines
        row_1 = grid[0]
        row_2 = grid[1]
        row_3 = grid[2]
        col_1 = [row[0] for row in grid]
        col_2 = [row[1] for row in grid]
        col_3 = [row[2] for row in grid]
        diag_1 = [grid[i][i] for i in range(3)]
        diag_2 = [grid[i][j] for i in range(3) for j in range(3)[::-1] if i + j == 2]

        win_list = [row_1, row_2, row_3, col_1, col_2, col_3, diag_1, diag_2]

        for row in win_list:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                print(row[0], 'wins')
                return True

        if all(i != ' ' for row in grid for i in row):
            print('Draw')
            return True

        if any(i == ' ' for row in grid for i in row):
            print('Game not finished')

    elif abs(count_x - count_o) > 1:
        print('Impossible')


def game(turn):
    while True:
        if turn == first_player:
            move(first_player)
        else:
            move(second_player)
        turn = second_player if turn == first_player else first_player
        if game_end() is True:
            break
        else:
            continue


if __name__ == '__main__':
    first_player = 'X'
    second_player = 'O'
    game_grid()
    game(first_player)
