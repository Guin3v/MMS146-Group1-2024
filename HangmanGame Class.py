class HangmanGame:
    def __init__(self, player_username=None, our_categories=None, secret_word=None, max_attempts=8):
        self.player_username = None #Public Attribute
        self._our_categories = our_categories #Protected Attribute
        self._secret_word = secret_word #Protected Attribute
        self._guessed_letters = [] #Protected Attribute
        self._incorrect_guesses = [] #Protected Attribute
        self._guessed_words = 0 #Protected Attribute
        self._max_attempts = max_attempts #Protected Attribute

    def choose_category(self):
        '''Prompt the player to type in a category.'''
        categories = ['Music Genres', 'Cities', 'Animals', 'School Supplies', 'Food']
  
        print("Available categories:")
        for category in categories:
            print(f"- {category}")
  
        while True:
            chosen_category = input("Please type in your chosen category: ").strip().capitalize()
            if chosen_category in categories:
                self._our_categories = chosen_category
                print(f"You chose the {self._our_categories} category.")
                return
            else:
                print("Invalid category. Please choose from the available categories.")
  
    def enter_letter (self):
        "Checks if a letter has been guessed already or is a valid guess, calls update_hangman() and check_guess()"
        enter_letter = str(input("Enter a Letter: "))
        letter = enter_letter.lower()
        if len(letter) != 1 or not letter.isalpha():
            return "Invalid input. Please enter a single alphabet character"
        elif letter in self._guessed_letters or letter in self._incorrect_guesses:
            return "You have already guessed that letter"
        else:
            self.update_hangman(letter)
            return self.check_guess(letter)
  
    def check_guess (self, letter):
        "Checks if the guessed letter is in the secret word and returns a statement of confirmation or negation"
        if letter in self._secret_word:
            return f"Good guess! {letter} is in the word."
        else:
            return f"Sorry, {letter} is not in the word. You have {self._max_attempts - len(self._incorrect_guesses)} attempts left."
  
    def update_hangman(self, letter):
        if letter in self._secret_word:
            self._guessed_letters.append(letter)
        else:
            self._incorrect_guesses.append(letter)
        
    def display_result(self):
        if self._incorrect_guesses >= self._max_attempts:
            return f"We're sorry. You lose."
        elif all(letter in self._guessed_letters for letter in self._secret_word):
            self._guessed_words += 1
            return "Congratulations! You got it!"
        else:
            return "Incorrect."
  
    def input_username(self):
        '''Prompt the player to input their username after winning.'''
        while True:
            username = input("Please enter your username to save your score: ").strip()
            
            if not username:
              raise ValueError("Username cannot be empty.")
            
            if username.isalnum():
                self.player_username = username
                print(f"Username '{self.player_username}' saved!")
                return
            else:
                print("Invalid username. Please enter a valid username (letters and numbers only).")

    def add_player_score(self):
        l = open('leaderboard.txt', 'a')
        l.write(self.player_username + '\n')
        l.write(self._guessed_words + '\n')
