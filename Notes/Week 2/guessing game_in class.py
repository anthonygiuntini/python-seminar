# Guessing game

import random

# generate a random number
random_num = random.randint(1,15)

# number of guesses 
max_guess = 5

#number of guesses the user has had
guess_num = 0

while guess_num < 5:

    guesses_remaining = max_guess - guess_num

    #number of guesses remaining
    print('You have ' + str(guesses_remaining) + ' guesses remaining')

    usr_guess = input('Enter your guess: ')

    if int(usr_guess) != random_num:
        print('WRONG!!!!!')
    else:
        print('You Won!!! (this time)')
        break
    
    guess_num = guess_num + 1
