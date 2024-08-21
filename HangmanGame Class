class HangmanGame:
  def __init__(self, player_username=None, our_categories=None, secret_word=None, max_attempts=8):
      self.player_username = None #Public Attribute
      self._our_categories = our_categories #Protected Attribute
      self._secret_word = secret_word #Protected Attribute
      self._guessed_letters = [] #Protected Attribute
      self._incorrect_guesses = [] #Protected Attribute
      self._max_attempts = max_attempts #Protected Attribute

  def update_hangman(self):
      display_word = ''.join([letter if letter in self.guessed_letters else '_' for letter in self.secret_word])
      return display_word

  def display_result(self):
      if self._incorrect_guesses >= self.max_attempts:
          return f"We're sorry. You lose."
      elif all(letter in self.guessed_letters for letter in self.secret_word):
          return "Congratulations! You won!"
      else:
          return "Incorrect."

  def enter_letter (self, letter):
       "Enter a leter and check if it has been guessed already or is a valid guess."
       self.letter = letter.lower()
       if len(self.letter) != 1 or not self.letter.isalpha():
          return "Invalid input. Please eneter a single alphabet character"
       elif self.letter in self._guessed_letters or letter in self._incorrect_guesses:
          return "You have already guessed that letter"
       else:
          self._guessed_letters.append(self.letter)
          return self.check_guess (self.letter)
       
  def check_guess (self, letter):
       "Check if the guesses letter is in the secret word and update incorrect guesses if not."
       if self.letter in self._secret_word:
          return f"Good guess! {self.letter} is in the word."
       else:
          self._incorrect_guesses.append(letter)
          return f"Sorry, {self.letter} is not in the word. You have {self._max_attempts - len(self._incorrect_guesses)} attempts left."

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
