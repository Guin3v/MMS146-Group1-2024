from HangmanWordGenerator import HangmanWordGenerator
from HangmanGame import HangmanGame
from HangmanUI import HangmanUI

def main():
    word_generator = HangmanWordGenerator('wordbank.txt')
    
    '''Define default values for the required arguments'''
    default_category = ""
    default_secret_word = ""
    default_max_attempts = 8
    
    '''Initialize the game with the default score of 0'''
    hangman_game = HangmanGame(
        our_categories=default_category,
        secret_word=default_secret_word,
        max_attempts=default_max_attempts,
        word_gen=word_generator
    )
    
    hangman_ui = HangmanUI(hangman_game)
    
    while True:
        '''Reset game state before each round'''
        hangman_game.reset_guesses()
        
        hangman_game.choose_category()
        secret_word = word_generator.get_random_word(hangman_game._our_categories)
        hangman_game.set_secret_word(secret_word)

        '''start the game process'''
        while hangman_game._win_status == 0:
            hangman_ui.display_word_status()
            hangman_ui.display_hangman()
            hangman_game.enter_letter()
            hangman_game.display_result()

            '''Check if the player has exhausted all attempts'''
            if hangman_game._hangman_status >= hangman_game._max_attempts:
                hangman_game._win_status = 1 
                break

        '''check the result of the game'''
        if hangman_game._win_status == 2:  # Player guessed the word correctly
            print(f"Your current score is: {hangman_game.score}")
            continue  # Keep playing until attempts are exhausted
        elif hangman_game._win_status == 1:  # Player failed to guess the word
            print("Game Over!")
            hangman_game.input_username()
            hangman_game.record_score()
            hangman_game.display_hall_of_fame()
            
            '''Ask if the player wants to play again'''
            play_again = input("Do you want to play again? (Y/N): ").strip().upper()
            if play_again == 'Y':
                hangman_game.reset_game()  # Reset the game state for a new round
                continue  # Start a new round
            else:
                break  # Exit the main loop

if __name__ == "__main__":
    main()
