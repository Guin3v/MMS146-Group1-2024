from hangmangame import HangmanGame

class HangmanUI:
    
    def __init__(self, hangman_game: object):
        self.hangman = hangman_game
    
    def display_hangman(self):
        guesses = len(self.hangman._incorrect_guesses)
        if guesses == 0:
                print(
                    """
                  |
                  |
                  |
                  |
                  |
           --------
                    """
                )
        elif guesses == 1:
                print(
                    """
              -----
                  |
                  |
                  |
                  |
                  |
           --------
                    """
                )
        elif guesses == 2:
                print(
                    """
              -----
              |   |
                  |
                  |
                  |
                  |
           --------
                    """
                )
        elif guesses == 3:
                print(
                    """
              -----
              |   |
              O   |
                  |
                  |
                  |
           --------
                    """
                )
        elif guesses == 4:
                print(
                    """
              -----
              |   |
              O   |
              |   |
                  |
                  |
           --------
                    """
                )
        elif guesses == 5:
                print(
                    """
              -----
              |   |
              O   |
             /|   |
                  |
                  |
           --------
                    """
                )
        elif guesses == 6:
                print(
                    """
              -----
              |   |
              O   |
             /|\  |
                  |
                  |
           --------
                    """
                )
        elif guesses == 7:
                print(
                    """
              -----
              |   |
              O   |
             /|\  |
             /    |
                  |
           --------
                    """
                )
        elif guesses == 8:
               print(
                      """
              -----
              |   |
              O   |
             /|\  |
             / \  |
                  |
           --------
                    """
               )
               
    def display_word_status(self):
        '''
        Display the word, revealing the letter each time the player makes a correct guess
        '''
        word_status = ''.join([letter if letter in self.hangman._guessed_letters else '_' for letter in self.hangman._secret_word])
        print(f"\nWord: {word_status}")
    
    def display_end_game_message(self):
        pass
