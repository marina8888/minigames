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
    return (0,0)

def james():
    # Create list of options, rows, cols then diags
    options = []
    # rows
    options.append(len((board[0][0] + board[0][1] + board[0][2]).strip()))
    options.append(len((board[1][0] + board[1][1] + board[1][2]).strip()))
    options.append(len((board[2][0] + board[2][1] + board[2][2]).strip()))
    # cols
    options.append(len((board[0][0] + board[1][0] + board[2][0]).strip()))
    options.append(len((board[0][1] + board[1][1] + board[2][1]).strip()))
    options.append(len((board[0][2] + board[1][2] + board[2][2]).strip()))
    # diags
    options.append(len((board[0][0] + board[1][1] + board[2][2]).strip()))
    options.append(len((board[2][0] + board[1][1] + board[0][2]).strip()))
    # Check lengths
    if max(options) == 0:
        return (1,1) # Start in the middle...
    selector = options.index(max(options))
    # Rows
    if selector in [0, 1, 2]:
        iterator = 0
        for candidate in board[selector]:
            if candidate == ' ':
                return (selector, iterator)
            iterator += 1
    # Cols
    if selector in [3, 4, 5]:
        selector -= 3
        iterator = 0
        for candidate in [x[0] for x in board[selector]]:
            if candidate == ' ':
                return (iterator, selector)
            iterator += 1
    # Diags
    if selector in [6, 7]:
        if selector == 6:
            for iterator in range(3):
                if board[iterator][iterator] == ' ':
                    return (iterator, iterator)
        elif selector == 7:
            for iterator in range(3):
                if board[2-iterator][iterator] == ' ':
                    return (2-iterator, iterator)



if __name__ == "__main__":
    referee()
