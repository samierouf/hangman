import random

class Hangman:
    """
    Hangman class for managing the game state.

    Attributes:
    - word_list (list): A list of words for the game.
    - num_lives (int): The number of lives the player has at the start of the game.
    - word (str): The word to be guessed, picked randomly from the word_list.
    - word_guessed (list): A list of the letters of the word, with _ for each letter not yet guessed.
    - num_letters (int): The number of UNIQUE letters in the word that have not been guessed yet.
    - list_of_guesses (list): A list of the guesses that have already been tried.
    """

    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman game.

        Parameters:
        - word_list (list): A list of words for the game.
        - num_lives (int): The number of lives the player has at the start of the game (default is 5).
        """
        self.word_list = word_list  # List of possible words the game may choose
        self.num_lives = num_lives  # Number of lives the player has to correctly guess the word
        self.word = random.choice(word_list)  # The word chosen at random from the word list
        self.word_guessed = list('_' for _ in range(len(self.word)))  # Length of the word the player has to guess
        self.num_letters = len(set(self.word))  # How many unique letters are in the word
        self.list_of_guesses = []  # List of past guesses the user has made


    def check_guess(self, guess):
        guess = guess.lower() #  lower case the letter
        if guess in self.word: # checks to see if the letter ids in the word
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if guess == self.word[i]:
                    self.word_guessed[i] = guess
                    print(self.word_guessed)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print( f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    
    def ask_for_input(self):
        while True:
            guess = input("Guesss a letter:")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print( "You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)



def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            print(game.num_letters)
            game.ask_for_input()
            
        else: #game.num_lives != 0 and game.num_letters <= 0:
            print('Congratulations. You won the game!')




word_list = ['apple', 'cherries', 'melon', 'potato', 'mango']  # List of 5 different fruits assigned to variable called word list
play_game(word_list)
