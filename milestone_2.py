import random
word_list = ['apple', 'cherry', 'melon', 'pineapple', 'mango'] # List of 5 different fruits assigned to varaible called word list
print(word_list)  # Prints the word list
word = random.choice(word_list) # Random item from list assigened to variable 'word'
print(word)

guess = input('guess a letter: ') # User gueess a letter and it is stored in variable 'guess'
if len(guess) == 1 and guess.isalpha() == True: # If statment to see if user input is a singuar letter
    print('Good guess!')
else:
    print('Oops! That is not a valid input')
