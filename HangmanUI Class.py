from hangmangame import HangmanGame

class HangmanUI:
    
    def __init__(self, hangman_game: object):
        self.hangman = hangman_game
    
    def display_hangman(self):
        '''
        Checks the self.__incorrect_guesses list within the HangmanGame class for the number of wrong letters 
        '''
        guesses = len(self.hangman._incorrect_guesses)
        'Displays the appropriate state of the Hangman'
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
        """
        Prompts the player if they would like to play again or quit the game.
        """
        TryAgain_choice = str(input("Would you like to play again? Y|N \n")).upper()
        
        if TryAgain_choice == 'Y':
            print("\nYou've chosen to play again. Good Luck!")
            HangmanUI(self.hangman) #Subject to change in final implementation
        elif TryAgain_choice == 'N':
            Quit_Choice = str(input("Would you like to quit? Y|N \n")).upper()
            
            if Quit_Choice == "Y":
                print("\nYou've chosen to quit the game. Thank you for Playing!")
                raise SystemExit
            elif Quit_Choice == "N":
                print("")
                self.display_end_game_message()
            else:
                print("Invalid Input.")
                self.display_end_game_message()
        else:
            print("Invalid Input.")
            self.display_end_game_message()
