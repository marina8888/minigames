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


def play(symbol, position):
    board[position[0]][position[1]] = symbol
    prettyprint()


def winner(player):
    won = False
    # Check rows
    row0 = board[0][0] == board[0][1] == board[0][2] != ' '
    row1 = board[1][0] == board[1][1] == board[1][2] != ' '
    row2 = board[2][0] == board[2][1] == board[2][2] != ' '
    if row0 or row1 or row2:
        won = True
    # Check columns
    col0 = board[0][0] == board[1][0] == board[2][0] != ' '
    col1 = board[0][1] == board[1][1] == board[2][1] != ' '
    col2 = board[0][2] == board[1][2] == board[2][2] != ' '
    if col0 or col1 or col2:
        won = True
    # Check diganals
    diag0 = board[0][0] == board[1][1] == board[2][2] != ' '
    diag1 = board[2][0] == board[1][1] == board[0][2] != ' '
    # Check for draw
    filled = [x != ' ' for x in board[0]] + [x != ' ' for x in board[1]] + [x != ' ' for x in board[2]]
    draw = all(filled)
    if diag0 or diag1:
        won = True
    if won:
        if player == 0:
            print('Marina wins the game!')
        else:
            print('James wins the game!')
    if draw:
        print('Game is a draw!')
        exit(0)
    return won


def ok_move(position):
    if board[position[0]][position[1]] != ' ':
        return False
    return True


def referee():
    player = random.randint(0, 1)
    # Decide who starts randomly (player 0 = marina, player 1 = james)
    while (not winner(int(not player))):
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
    if board[1][1] ==' ':
        return (1, 1)

    # Check diganals 1
    elif board[0][0] == board[2][2] and board[1][1] == ' ':
        return (1,1)
    elif board[2][0] == board[0][2] and board[1][1] == ' ':
        return (1,1)
    # Check diganals 2
    elif board[0][0] == board[1][1] and board[2][2] == ' ':
        return (2,2)
    elif board[1][1] == board[2][2] and board[0][0] == ' ':
        return (0,0)
    # Check diganals 3
    elif board[0][2] == board[1][1] and board[2][0] == ' ':
        return (2,0)
    elif board[2][0] == board[1][1] and board[0][2] == ' ':
        return (0,2)

    # Check columns set 1
    elif board[0][0] == board[1][0] and board[2][0] == ' ':
        return (2,0)
    elif board[1][0] == board[2][0] and board[0][0] == ' ':
        return (0,0)
    elif board[2][0] == board[0][0] and board[1][0] == ' ':
        return (1,0)

    # Check columns set 2
    elif board[0][1] == board[1][1] and board[2][1] == ' ':
        return (2,1)
    elif board[1][1] == board[2][1] and board[0][1] == ' ':
        return (0,1)
    elif board[2][1] == board[0][1] and board[1][1] == ' ':
        return (1,1)

    # Check columns set 3
    elif board[0][2] == board[1][2] and board[2][2] == ' ':
        return (2,2)
    elif board[1][2] == board[2][2] and board[0][2] == ' ':
        return (0,2)
    elif board[2][2] == board[0][2] and board[1][2] == ' ':
        return (1,2)

    # Check rows set 1
    elif board[0][0] == board[0][1] and board[0][2] == ' ':
        return (0,2)
    elif board[0][1] == board[0][2] and board[0][0] == ' ':
        return (0,0)
    elif board[0][2] == board[0][0] and board[0][1] == ' ':
        return (0,1)

# Check rows set 2
    elif board[1][0] == board[1][1] and board[1][2] == ' ':
        return (1,2)
    elif board[1][1] == board[1][2] and board[1][0] == ' ':
        return (1, 0)
    elif board[1][2] == board[1][0] and board[1][1] == ' ':
        return (1, 1)

    # Check rows set 3
    elif board[2][0] == board[2][1] and board[2][2] == ' ':
        return (2,2)
    elif board[2][1] == board[2][2] and board[2][0] == ' ':
        return (2, 0)
    elif board[2][2] == board[2][0] and board[2][1] == ' ':
        return (2, 1)

    #fill in diagonals
    elif board[0][0] == ' ':
        return (0,0)
    elif board[2][0] == ' ':
        return (2, 0)
    elif board[0][2] == ' ':
        return (0, 2)
    elif board[2][2] == ' ':
        return (2, 2)

    # fill in columns
    elif board[1][0] == ' ':
        return (1, 0)
    elif board[0][1] == ' ':
        return (0, 1)
    elif board[2][1] == ' ':
        return (2, 1)
    elif board[1][2] == ' ':
        return (1, 2)
    else:
        return (0,0)

def james():
    return (0, 0)


if __name__ == "__main__":
    referee()
