word = 'apple'
'''
while True: # while loop
    guess = input('guess a letter:') # asks user for input
    if guess.isalpha() == True and len(guess) == True: # checks if user input is valid if so loop ends else continues
        break
    else:
        print("Invalid letter, Please eter a single alphabetical character")

if guess in word: # checks if the letter the user guessed is in the word
    print(f"Good guess {guess} is in the word")
else:
    print(f"Sorry, {guess} is not in the word. Try again")

'''

def check_guess(guess): # function check_uess that initally makes the letter lower case checkes if the letter is present in the word using the users input
    guess = guess.lower()
    if guess in word:
        print(f"Good guess {guess} is in the word")
    else:
        print(f"Sorry, {guess} is not in the word. Try again")

def ask_for_input():# fucntion that asks for the user to guess a letter and checks if it valid. guess unction used to see if letter is in the woed
    while True: # while loop
        guess = input('guess a letter:') # asks user for input
        if guess.isalpha() == True and len(guess) == 1: # checks if user input is valid if so loop ends else continues
            break
        else:
            print("Invalid letter, Please eter a single alphabetical character")
    
    check_guess(guess)

ask_for_input()




