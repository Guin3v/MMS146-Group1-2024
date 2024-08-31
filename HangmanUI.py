class HangmanUI:
    
    def __init__(self, hangman_game: object):
        self.hangman_game = hangman_game
        self.try_again_status = 0
        self.hall_of_fame = {}
    
    def display_hangman(self):
        '''
        Checks the self.__incorrect_guesses list within the HangmanGame class for the number of wrong letters 
        '''
        guesses = self.hangman_game._hangman_status
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
        word_status = ''.join([letter if letter in self.hangman_game._guessed_letters else '_' for letter in self.hangman_game._secret_word])
        print(f"Word: {word_status}")
    
    def display_end_game_message(self):
        """
        Prompts the player if they would like to play again or quit the game.
        """
        TryAgain_choice = str(input("Would you like to play again? Y|N \n")).upper()
        
        if TryAgain_choice == 'Y':
            print("\nYou've chosen to play again. Good Luck!")
            self.try_again_status = 1
            return self.try_again_status
        elif TryAgain_choice == 'N':
            Quit_Choice = str(input("\nWould you like to quit? Y|N \n")).upper()
            if Quit_Choice == "Y":
                print("\nYou've chosen to quit the game. Thank you for Playing!\n")
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
    
    def display_hall_of_fame(self):
        '''Display the top 5 players with the highest scores'''
        try:
            with open('leaderboard.txt', 'r') as file:
                scores = file.readlines()
            
            score_list = [(line.strip().split(':')[0], int(line.strip().split(':')[1])) for line in scores]
            sorted_scores = sorted(score_list, key=lambda x: x[1], reverse=True)

            print("\nHALL OF FAME - Top 5 Players:")
            print("------------------------------")
            for rank, (username, score) in enumerate(sorted_scores[:5], start=1):
                print(f"{rank}. {username}: {score} Words")
        except FileNotFoundError:
             print("No scores found in the leaderboard.")
        except Exception as e:
            print(f"An error occurred while displaying the leaderboard: {e}") 
