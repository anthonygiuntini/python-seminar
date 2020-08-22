#What do I do?
# and what would I be useful for?

import random
import time
import math

input_text = input(':')

text_l = list(input_text)

running = True

prev_words = []
count = 1

length = len(text_l)
displaying = True
lett_count = 0
for letter in input_text:
    if input_text.count(letter) > lett_count:
        lett_count = input_text.count(letter)

MAX_ITER = math.factorial(length)//math.factorial(lett_count)   #calculates the number of combinations
print('Number of possible combinations: %d' %(MAX_ITER))
if MAX_ITER > 1500:
    print('The program will stop displaying text to improve speed')
    displaying = False


t1 = time.time()

while running:
    random.shuffle(text_l)
    word = ''.join(text_l)
    
    if word not in prev_words:
        if displaying:
            print(str(len(prev_words))+ '. ' + word)
        prev_words.append(word)
            
    if len(prev_words) >= MAX_ITER:
        running = False
        print('\n\nDone.')
        print('Iterations: ' + str(count))

    count += 1

tf = time.time() - t1
print('Time: %fs' % (tf))
