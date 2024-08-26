from hangmangame import HangmanGame

class HangmanUI:
    
    def __init__(self, hangman_game: object):
        self.hangman = hangman_game
        self.hall_of_fame = {}
        
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
            
    def display_hall_of_fame(self):
        '''
        Opens the leaderboard text file (leaderboard.txt) 
        and converts each line into an item in a list
        '''
        r = open('leaderboard.txt', 'r')
        lb_list = r.readlines()
        
        '''
        Converts the the list of items into a dictionary by
        reading the list two items at a time. The first item
        is then set as the Key, while the second item is set 
        as the Value for the Dictionary pair. 
        
        This is repeated for all sets of two in the list, for
        the entire list from the text file.
        '''
        for i in range(0, len(lb_list), 2):
            self.hall_of_fame[lb_list[i]] = lb_list[i+1]
            
        '''
        Sorts the dictionary by getting the Values and comparing
        them through the sorted list function. It is reversed to
        show the highest scores and then stored in a new list.
        '''
        list_hof = sorted(self.hall_of_fame.items(), key=lambda x:x[1], reverse=True)
        
        '''
        Once sorted, the first 5 Pairs are then converted back
        into the final hall of fame dictionary.
        '''
        sorted_hof = dict(list_hof[0:5])
        
        '''
        Displays the dictionary/the Top 5 Players recorded
        '''
        print("HALL OF FAME - Top 5 Players")
        print("-----------------------------")
        for key, value in sorted_hof.items():
            print(f'{list(sorted_hof).index(key) + 1}. {key} - Score: {value} Words')
