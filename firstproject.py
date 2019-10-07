
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('------')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('------')
    print(board[1]+'|'+board[2]+'|'+board[3])

#test_board = [' ']*10
# display_board(test_board)
def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('player1:choose X or O').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return('O','X')    

      
def place_marker(board,marker,position):
    board[position] = marker

# place_marker(test_board,'$',8)
# display_board(test_board)      

def win_check(board,mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark)or
       (board[4] == mark and board[5] == mark and board[6] == mark)or
       (board[7] == mark and board[8] == mark and board[9] == mark)or
       (board[1] == mark and board[4] == mark and board[7] == mark)or
       (board[2] == mark and board[5] == mark and board[8] == mark)or
       (board[3] == mark and board[6] == mark and board[9] == mark)or
       (board[1] == mark and board[5] == mark and board[9] == mark)or
       (board[3] == mark and board[5] == mark and board[7] == mark))

#display_board(test_board)
# win_check(test_board,'X')
import random 

def choose_first():   
    
    flip = random.randint(0,1)

    if flip == 0:
        return 'player1'
    else:
        return 'player2'  

def space_check(board,position):

    return board[position] == ' '

def full_board_check():

    for i in range(1,10):
        if space_check(board,i):
            return False
        return True     

def player_choice():

    position = 0

    while position not in [ 1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('choose a position: (1-9) '))
    return position    

def replay():
    input('play again? enter Yes or No ')

    return choice == 'Yes'                      
    
  













                        
    
  

















































