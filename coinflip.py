"""
This is just a simple game of a coin flip. I want the program to generate a coin flip and ask the player to make a call for heads or tails. Then the program will let the player know if they were right or not. 
"""

import random

def coinflip():
    """
    Get a coinflip by choosing randomly between 0 and 1 and returning either heads of tails
    """
    
    if random.randint(0,1) == 0:
        return "heads"
    else:
        return "tails"
                
def player_input():
    """
    Get player input either heads or tails
    """
    
    call = ''
    while call not in 'heads tails'.split():
        call = raw_input("Choose either heads of tails: ")
    return call

def again():
    """
    Ask player if they want to play again
    """
    return raw_input('Again?: ').lower().startswith('y')
    
    
print "Welcome to coinflip"


while True:
    flip = coinflip()
    pinput = player_input()
    game = True
    
    while game:
        if pinput == flip:
            print "Yes, it was %s" %flip
            game = False
        else:
            print "No, it was %s" %flip
            game = False
    
    if not again():
        break
