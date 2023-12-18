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
        """
        Check if the guessed letter is in the word.

        Parameters:
        - guess (str): The letter guessed by the player.
        """
        guess = guess.lower() # converts teh users guess in to lower case
        if guess in self.list_of_guesses: # checks to see if user has already guessed that letter before
            print("You already tried that letter!")
        elif guess in self.word: # if the users guess is present in the word to be predicted. message 
            print(f"Good guess! {guess} is in the word")
            for index, letter in enumerate(self.word): # gets the index and corresponding letter for. for each letter in the word
                if letter == guess: # if th guess is in the letter word_guessed fillis in the coressponding blank
                    self.word_guessed[index] = guess
                    print(self.word_guessed)
            self.num_letters -= 1 # number of letters needed to be predicted go down by 1
        else: # if their guesss is incorrects
            self.num_lives -= 1 # they lose one of the lives. message telling them they are incorrects appreas as well as how many lives they have left
            print(f"Sorry, {guess} is not in the word")
            print(f"You have {self.num_lives} lives left")
        
        self.list_of_guesses.append(guess) # every valid guess is stored in the list iof guesses so user doesnt repeat thesleves



    def ask_for_input(self):
        """
        Ask the user to guess a letter and handle invalid inputs.
        """
        while True:
            self.guess = input("Guess a letter: ") # asks user for input
            if len(self.guess) != 1 or self.guess.isalpha() == False: #checks if the input is valid if not message is printed
                print("Invalid letter. Please, enter a single alphabetical character")
            elif self.guess in self.list_of_guesses: # if they have already gussed that letter for this game they are told so
                print("You already tried that letter!")
            else: # if heir guess is new and valid check guess is activated.
                self.check_guess(self.guess)
                self.list_of_guesses.append(self.guess)
                break




def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
            
        else: #game.num_lives != 0 and game.num_letters <= 0:
            print('Congratulations. You won the game!')
            break



#test
word_list = ['apple', 'cherries', 'melon', 'potato', 'mango']  # List of 5 different fruits assigned to variable called word list
play_game(word_list)