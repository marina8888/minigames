import random
import time

# Board object
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]


# Helper functions
def prettyprint():
    print("\u0332".join(' | ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2] + ' |  '))
    print("\u0332".join(' | ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2] + ' |  '))
    print("\u0332".join(' | ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2] + ' |  '))


def play(player, position):
    board[position[0]][position[1]] = player
    prettyprint()


def winner():
    # Check rows
    row0 = board[0][0] == board[0][1] == board[0][2] != ' '
    row1 = board[1][0] == board[1][1] == board[1][2] != ' '
    row2 = board[2][0] == board[2][1] == board[2][2] != ' '
    if row0 or row1 or row2:
        return True
    # Check columns
    col0 = board[0][0] == board[1][0] == board[2][0] != ' '
    col1 = board[0][1] == board[1][1] == board[2][1] != ' '
    col2 = board[0][2] == board[1][2] == board[2][2] != ' '
    if col0 or col1 or col2:
        return True
    # Check diganals
    diag0 = board[0][0] == board[1][1] == board[2][2] != ' '
    diag1 = board[2][0] == board[1][1] == board[0][2] != ' '
    if diag0 or diag1:
        return True
    return False


def ok_move(position):
    if board[position[0]][position[1]] != ' ':
        return False
    return True


def referee():
    player = random.randint(0, 1)
    # Decide who starts randomly (player 0 = marina, player 1 = james)
    while (not winner()):
        if player == 0:
            position = marina()
            if ok_move(position):
                print('Marina plays:')
                play('x', position)
            else:
                print("Invalid move by Marina - James wins!")
                exit(0)
        else:
            position = james()
            if ok_move(position):
                print('James plays:')
                play('o', position)
            else:
                print("Invalid move by James - Marina wins!")
                exit(0)
        player = int(not player)
        time.sleep(3)


# AI Players
def marina():
    return (0, 0)


def james():
    return (0, 0)


if __name__ == "__main__":
    referee()
