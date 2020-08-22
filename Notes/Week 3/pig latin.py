# Pig latin

def run_program():
    '''This is a function that asks for the user's input and translates it to pig latin.'''
    
    # Get user input with prompt
    usr_in = input('Enter a sentance:\n')

    # put the user's input into lowercase
    usr_in = usr_in.lower()
    
    # Split the string input into words by splitting at spaces
    usr_words = usr_in.split(' ')

    # Empty list for reconstructing the new sentance later
    new_sentance = []

    # Create a list of vowels and consonants
    # list() will split it by characters its faster than creating the list manually with l = ['a', 'e', 'i', 'o', 'u']
    # a shortcut that involves less typing
    vowels = list('aeiou')
    consonants = list('bcdfghjklmnpqrstvxzwy')

    # Loop through each word in the list usr_words
    for word in usr_words:

        # Create a list of the letters in the word
        letter_list = list(word)

        # rules for the language (From wikipedia)

        # if the first letter in the list is a vowel, keep it and add 'yay' to the end
        if letter_list[0] in vowels:
            letter_list.append('yay')

        # else if the first letter and second letters are cons.
        elif letter_list[0] in consonants and letter_list[1] in consonants:
        
            # Return and remove the first character from the list
            first_char = letter_list.pop(0)
            # add that first character back to the end of the list
            letter_list.append(first_char)

            # Return and remove the second character from the list (note index doesnt change, b/c you already removed the first)
            second_char = letter_list.pop(0)
            # add that first character back to the end of the list
            letter_list.append(second_char)        

            # add 'ay' to the end of the list
            letter_list.append('ay')

        # otherwise just take the first letter
        else:
            # Return and remove the first character from the list
            first_char = letter_list.pop(0)
            # add that first character back to the end of the list
            letter_list.append(first_char)
            
            # add 'ay' to the end of the list
            letter_list.append('ay')
        
        # join the characters in letter_list back together to form a string
        new_word = ''.join(letter_list)

        # add the reconstructed word to the new_sentance list
        new_sentance.append(new_word)

    # Output the sentance
    print(' '.join(new_sentance))

# While loop to allow user to translate multiple times
running = True

while running:
    run_program()

    #ask the user if they want to run again
    user_command = input('Would you like to translate another? (y/n)\n')

    if user_command == 'n':
        # Change running to false to stop the loop
        running = False
    else:
        # Pass does nothing
        pass
    


