class HangmanGame:
    def __init__(self, player_username=None, our_categories=None, secret_word=None, max_attempts=8, word_gen=object):
        self.player_username = None #Public Attribute
        self._our_categories = our_categories #Protected Attribute
        self._secret_word = secret_word #Protected Attribute
        self._guessed_letters = [] #Protected Attribute
        self._incorrect_guesses = [] #Protected Attribute
        self._hangman_status = 0 #Protected Attribute
        self._guessed_words = 0 #Protected Attribute
        self._win_status = 0 #Protected Attribute
        self._max_attempts = max_attempts #Protected Attribute
        self.word_generator = word_gen #Protected Attribute

    def choose_category(self):
        '''Prompt the player to type in a category.'''
        categories = ['Music Genres', 'Cities', 'Animals', 'School Supplies', 'Food', 'Body Organ', 'Color']
  
        print("\nAvailable categories:")
        for category in categories:
            print(f"- {category}")
    
        print("")
        chosen_category = input("Please type in your chosen category: ").strip().title()
        
        print("")
        if chosen_category in categories:
            self._our_categories = chosen_category
            print(f"You chose the {self._our_categories} category. \n")
                
        else:
            print("Invalid category. Please choose from the available categories.\n")
            self.choose_category()
  
    def set_secret_word(self, secret_word):
        self._secret_word = secret_word
  
    def enter_letter (self):
        "Checks if a letter has been guessed already or is a valid guess, calls update_hangman() and check_guess()"
        enter_letter = str(input("\nEnter a Letter: "))
        letter = enter_letter.lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Invalid input. Please enter a single alphabet character")
        elif letter in self._guessed_letters or letter in self._incorrect_guesses:
            print("\nYou have already guessed that letter")
        else:
            self.update_hangman(letter)
            self.check_guess(letter)
  
    def check_guess (self, letter):
        "Checks if the guessed letter is in the secret word and returns a statement of confirmation or negation"
        if letter in self._secret_word:
            print(f"\nGood guess! {letter} is in the word.\n")
        else:
            print(f"\nSorry, {letter} is not in the word. You have {self._max_attempts - self._hangman_status} attempts left.\n")
  
    def update_hangman(self, letter):
        if letter in self._secret_word:
            self._guessed_letters.append(letter)
        else:
            self._hangman_status += 1
            self._incorrect_guesses.append(letter)
        
    def display_result(self):
        if len(self._incorrect_guesses) >= self._max_attempts:
            print(f"\nWe're sorry. You lose.")
            self._win_status = 1
        elif all(letter in self._guessed_letters for letter in self._secret_word):
            self._guessed_words += 1
            print("\nCongratulations! You got it!")
            self._win_status = 2
        else:
            return "\n"
  
    def input_username(self):
        '''Prompt the player to input their username after winning.'''
        username = input("Please enter your username to save your score: ").strip()
            
        if not username:
            raise ValueError("Username cannot be empty.")
            
        if username.isalnum():
            self.player_username = username
            print(f"Username {self.player_username} saved! You got {self._guessed_words} words!")
        else:
            print("Invalid username. Please enter a valid username (letters and numbers only).")

    def add_player_score(self):
        l = open('leaderboard.txt', 'a')
        l.write(f'{self.player_username}\n')
        l.write(f'{self._guessed_words}\n')

    def reset_guesses(self):
        self._win_status = 0
        self._secret_word = None
        self._guessed_letters.clear()
        self._incorrect_guesses.clear()   
        
    def reset_game(self):
        self._secret_word = None
        self._guessed_words = 0
        self._hangman_status = 0
        self._guessed_letters.clear()
        self._incorrect_guesses.clear()
