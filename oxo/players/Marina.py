

def play(board):
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
