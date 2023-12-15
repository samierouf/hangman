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
    def __init__(self, word_list, num_lives = 5):
        """
        Initialize the Hangman game.

        Parameters:
        - word_list (list): A list of words for the game.
        - num_lives (int): The number of lives the player has at the start of the game (default is 5).
        """
        self.word_list = word_list # list of possible wordd the game may choose
        self.num_lives = num_lives # number of lives the player has to correctly guess the word
        self.word = random.choice(word_list) # thew word chossen at random from the word list 
        self.word_guessed = list('_' for i in range(len(self.word))) # length of the word the player has to guess 
        self.num_letters = len(set(self.word)) # how amny unique letters are in the word
        self.list_of_guesses = [] # list of past guesses the user has made
    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word")

    def ask_for_input(self):
        while True:
            self.guess = input("Guess a letter: ")
            if len(self.guess) != 1 or not self.guess.isalpha():
                print("Invalid letter. Please, enter a singlle alphabetical chractere")
            elif self.guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(self.guess)
                self.list_of_guesses.append(self.guess)
                

# Create an instance of the Hangman class
hangman_game = Hangman(word_list=["apple", "banana", "orange"])

# Call the ask_for_input method
hangman_game.ask_for_input()







