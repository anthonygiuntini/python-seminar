#Guessing Game Class Example

import random


# Use randint function from random library to pick a random number between 1 and 25
random_num = random.randint(1,15)

# Number of guesses
num_of_guesses = 5

# Set a variable for the user outcome, with a default value of false
usr_won = False

# For loop which loops for number of guesses
# It puts the current guess number in variable
for guess_num in range(0,num_of_guesses):

    # Calculate # of guesses remaining
    guesses_remaining = num_of_guesses - guess_num
    
    # Tell the user how many guesses they have left
    print('You have ' + str(guesses_remaining) + ' guesses remaining.')

    # Prompt user and get input 
    usr_input = input("Guess a number between 1 and 15): ")

    usr_input_int = int(usr_input)

    # Check if user input == random_num
    if usr_input_int == random_num:
        usr_won = True
        # Exit the loop early
        break
    # If it's not equal check if it was greater
    elif usr_input_int > random_num:
        print('Sorry, your guess was too high.')

    # Otherwise it must have been less than
    else:
        print('Sorry, your guess was too low.')

# IF the user won (the usr_won var set to True) congratulate him, otherwise taunt him
if usr_won:
    print('Congrats!! You won')
else:
    print('Sorry (not sorry) you lost')

print('Game Over')
    
    

