# Modify the diamond printer script below to remove the space between the diamonds.

# AKA it should look like this:

                      ######
                       ####
                        ##
                       ####
                      ######

# not this:

                     ########
                      ######
                       ####
                        ##
                         
                        ##
                       ####
                      ######

space_count = 20
symbol_count = space_count // 2
loop_count = 0

increasing = True

while True:
    print(' ' * space_count + '#' * symbol_count)

    if increasing:
        symbol_count += 2
        space_count -= 1
        if space_count == 1:
            increasing = False
    else:
        symbol_count -= 2
        space_count += 1
        if symbol_count == 0:
            increasing = True
        
        
        
        
