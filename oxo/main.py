#james wants to make a fuction that when given three arguments taking : the player and position
# the function should return the board with the player board return
# function should be able to tell you when someone has won or when the game has otherwise ended

#this function uses the global variable
board=[[" "," "," "],
       [" "," "," "],
       [" "," "," "]]

def whostarts
# we need a random function to decide call either marina or james first - function are marina(), james() both return position
# functions marina and james need to return a position that is empty, based on a set of rules written in the function
#function that alternatively calls marina/james then play
#function whowon function that checks if game has ended or if someone won.

position = (1,1)
player = "x"

def prettyprint():
    print("\u0332".join( ' | ' + board[0][0]+' | '+ board[0][1]+' | '+ board[0][2]+ ' |  '))
    print("\u0332".join( ' | ' + board[1][0]+' | '+ board[1][1]+' | '+ board[1][2]+ ' |  '))
    print("\u0332".join( ' | ' + board[2][0]+' | '+ board[2][1]+' | '+ board[2][2]+ ' |  '))

def play(player, position):
    board[position[0]][position[1]]= player
    prettyprint()

def whostarts():
    

play(player, position)

