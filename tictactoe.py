"""
This is a game of Tic tac toe. 
"""

from __future__ import print_function
from IPython.display import clear_output
import random

def show_board(board):
   """
    show the game board to players
   """
   clear_output()
   print('   |   |')
   print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
   print('   |   |')
   print('-----------')
   print('   |   |')
   print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
   print('   |   |')
   print('-----------')
   print('   |   |')
   print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
   print('   |   |')


def player_input():
    '''
    Ask player 1 if they want to use  X or O as their marker
    '''
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = raw_input('Player 1: Do you want to be X or O?').upper()
        
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    '''
    Place player marker in the right space
    '''
    
    board[position] = marker

def win_check(board, mark):
    '''
    Check to see if a player won the game
    '''
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))
    
def choose_first():
    '''
    Randomly decide which player goes first
    '''
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
        
def space_check(board, position):
    return board[position] == ' '
    
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
    
def player_choice(board):
    
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = raw_input('Choose your next position (1-9) ')
    return int(position)
    
def replay():
    return raw_input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
 
print("Welcome to Tic Tac Toe!") 
    
while True:
    theboard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True
    
    while game_on:
        if turn == 'Player 1':
            
            show_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player1_marker, position)
            
            if win_check(theboard, player1_marker):
                show_board(theboard)
                print('Congratulations Player 1! You have won the game!')
                game_on = False
            else:
                if full_board_check(theboard):
                    show_board(theboard)
                    print('This game is a draw!')
                    break
                else:
                    turn = 'Player 2'
                    
        else:
            
            show_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player2_marker, position)
            
            if win_check(theboard, player2_marker):
                show_board(theboard)
                print('Congratualations Player 2! You have won the game!')
                game_on = False
            else:
                if full_board_check(theboard):
                    show_board(theboard)
                    print('This game is a draw!')
                    break
                else:
                    turn = 'Player 1'
                    
                    
    if not replay():
        break
    
        


