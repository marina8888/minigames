
def play(board):
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

