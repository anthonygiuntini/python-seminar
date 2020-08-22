# Diamond Printer

space_count = 20  # Max number of spaces to show

symbol_count = space_count // 2 # number of symbols is half number of spaces

increasing = True # if the diamond is growing bigger

while True:
    # Display diamond (show space_count number of spaces and symbol_count number of hashtags)
    print(' ' * space_count + '#' * symbol_count)

    # if the diamond is increasing, increase symbol count by 2 and decrease space count
    if increasing:
        symbol_count += 2
        space_count -= 1
        # change increasing to false if there are no spaces left
        if space_count == 1:
            increasing = False
    # otherwise do the opposite
    else:
        symbol_count -= 2
        space_count += 1
        # change increasing when symbols run out
        if symbol_count == 0:
            increasing = True
        
        
        
        
