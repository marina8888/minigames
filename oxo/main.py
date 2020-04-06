#james wants to make a fuction that when given three arguments taking : the player and position
# the function should return the board with the player board return
# function should be able to tell you when someone has won or when the game has otherwise ended

#this function uses the global variable
board=[[" "," "," "],
       [" "," "," "],
       [" "," "," "]]

position = (1,1)
player = "x"

def prettyprint():
    print("\u0332".join( ' | ' + board[0][0]+' | '+ board[0][1]+' | '+ board[0][2]+ ' |  '))
    print("\u0332".join( ' | ' + board[1][0]+' | '+ board[1][1]+' | '+ board[1][2]+ ' |  '))
    print("\u0332".join( ' | ' + board[2][0]+' | '+ board[2][1]+' | '+ board[2][2]+ ' |  '))

def play(player, position):
    board[position[0]][position[1]]= player
    prettyprint()

play(player, position)

