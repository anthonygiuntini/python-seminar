# Hangman.py

import random

# Define characters
# Proper convention is to use all caps for constants
DIAGRAMS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']


word_list = ['cat', 'lemur', 'cheeta', 'cockroach', 'horse', 'pig', 'alpaca', 'barracuda', 'bear', 'panda','whippet', 'zebra']
current_word = ''

current_progress = []
guessed_letters = []

incorrect_guess_num = 0

def update_display(incorrect_guess_int, current_progress_list, guessed_letter_list):
    '''
    Prints out the current diagram and the current word progress.
    '''
    print(DIAGRAMS[incorrect_guess_int])

    print('Progress: ' + ''.join(current_progress_list))

    print('Used Letters: ' + ','.join(guessed_letter_list))

def reset_vars():
    global current_progress, guessed_letters, incorrect_guess_num

    current_progress = []
    guessed_letters = []
    incorrect_guess_num = 0

running = True

# Game loop
while running:

    # Choose current word
    # generate a random index with random.randint(0, to length of list)
    #NOTE: leave out -1 for educational purposes
    current_word = word_list[random.randint(0,len(word_list)-1)]

    # Create a string that has an underscore for each letter in the current word
    current_progress_str = '_' * len(current_word)
    # Then generate a list from that string
    current_progress = list(current_progress_str)

    playing = True
    
    # another loop for the players
    while playing:
        
        # update the display
        update_display(incorrect_guess_num, current_progress, guessed_letters)

        # Get the user's guess
        usr_guess = input('What is your guess: ')

        # see if it was in the current_word
        if usr_guess in current_word:
            # loop through all letters in word and get their index using the enumerate function
            for index, lett in enumerate(current_word):
                # if the letter is the same as the user guess
                if lett == usr_guess:
                    # add it to current_progress at the proper index
                    current_progress[index] = lett

        else:
            # if its not in the current word, increment the incorrect_guess_num
            incorrect_guess_num += 1
            
        # add the letter to guessed_letters
        guessed_letters.append(usr_guess)
            
        # evaluate whether the user has won or lost or still playing
        if '_' not in current_progress:
            # if there are no underscores, then the user must have guessed everything
            print('YOU WON:)\n')
            playing = False
        elif incorrect_guess_num == len(DIAGRAMS)-1:
            # else if the the number of incorrect guesses == the number of diagrams the user lost

            update_display(incorrect_guess_num, current_progress, guessed_letters)
            
            print('YOU LOST:(\n')
            playing = False
            
        else:
            # otherwise move on
            pass

    usr_response = input('Would you like to play again? (y/n): ')
    if usr_response == 'y':
        reset_vars()
    else:
        print('Goodbye')
        running = False
        
