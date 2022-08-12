import numpy as np

# ------------------ CONSTANTS ------------------ #
l = [[' ', ' ', ' '],
     [' ', ' ', ' '],
     [' ', ' ', ' ']]


# ------------------ MECHANISM ------------------ #
def is_someone_wins(l):
    n = 3  # shape of the matrix (list)
    winner = -1  # No one

    # rows
    for i in range(n):
        row = ''.join(l[i])
        if row == 'X' * n:
            winner = 0
        elif row == 'O' * n:
            winner = 1

    # columns
    ## transpose
    l = np.transpose(l)
    ## Do the same thing as rows
    ## todo: I no my code is no longer DRY
    for i in range(n):
        col = ''.join(l[i])
        if col == 'X' * n:
            winner = 0
        elif col == 'O' * n:
            winner = 1

    # Diagonals
    first_diag = ''.join(map(str, np.diag(l)))
    ## rotate the matrix then extract the diagonal
    second_diag = ''.join(map(str, np.rot90(l).diagonal()))
    collect = [first_diag, second_diag]
    if 'X' * n in collect:
        winner = 0
    elif 'O' * n in collect:
        winner = 1

    return winner


# ------------------ ACTUAL WORK ------------------ #
print('Please write your names.')
players_name = input('Player 1: '), input("Player 2: ")
print('lets get started')

for game_turn in range(9):

    # which player turn
    if game_turn % 2 != 0:  # 1,2,4,5,7,
        print(f'Turn of {players_name[1]}. ')  # The Second Player
        symbol = "O"
    else:
        print(f'Turn of {players_name[0]}.')  # The First Player
        symbol = 'X'

    # ------------------ INPUT DATA and Fill l ------------------ #
    while True:

        row, col = list(
            map(int, input(f'    Write you want to put your symbol, following this format: row,col\n>>').split(',')))
        # TODO: exc handling for row col to be integers
        if l[row - 1][col - 1] == ' ':  # condition is always True or what
            # List filling
            l[row - 1][col - 1] = symbol
            break
        else:
            print("    This area isn't empty. try again> ")

    # ------------------ DISPLAY ------------------ #
    a = f'{l[0][0]} | {l[0][1]} | {l[0][2]}\n' \
        '---------\n' \
        f'{l[1][0]} | {l[1][1]} | {l[1][2]}\n' \
        '---------\n' \
        f'{l[2][0]} | {l[2][1]} | {l[2][2]}'
    print(a)

    # ------------------ MECHANISM ------------------ #
    winner = is_someone_wins(l)
    if winner == 1:
        print(f'{players_name[1].capitalize()} in the winner of the game.')
        break
    elif winner == 0:
        print(f'{players_name[0].capitalize()} in the winner of the game.')
        break


if winner == -1:
    print('No winner, Try again.')

