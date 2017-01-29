import random

def game():
    # generate a random number between 1 and 10 
    secret_num = random.randint(1, 10)
    guesses = []
    
    while len(guesses) < 3:
        try:   
            # get a number guess from the player
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("{} isn't a number!".format(guess))
        else:
            # compare guess to secret number
            if guess == secret_num:
                print("Congrats, you got it. the number was {}".format(secret_num))
                break
            elif guess < secret_num:
                print("Wrong! My number is higher than {}.".format(guess))
            else:
                print("Wrong! My number is lower than {}.".format(guess))
            guesses.append(guess)
    else:
        print("Haha, you didn't get it. My number was {}, loser".format(secret_num))
    
    play_again = input("Do you want to play again? Y/n ")
    if play_again.lower() != 'n':
        game()
    else:
        print("Peace")
game()   