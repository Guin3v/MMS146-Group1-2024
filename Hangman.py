from HangmanWordGenerator import HangmanWordGenerator
from HangmanGame import HangmanGame
from HangmanUI import HangmanUI

def main():
    word_generator = HangmanWordGenerator('wordbank.txt')
    
    # Define default values for the required arguments
    default_category = ""
    default_secret_word = ""
    default_max_attempts = 8 
    default_score = 0
    
    hangman_game = HangmanGame(
        our_categories=default_category,
        secret_word=default_secret_word,
        max_attempts=default_max_attempts,
        word_gen=word_generator,
        score=default_score
    )
    
    hangman_ui = HangmanUI(hangman_game)
    
    while True:
        hangman_game.choose_category()
        secret_word = word_generator.get_random_word(hangman_game._our_categories)
        hangman_game.set_secret_word(secret_word)

        while hangman_game._win_status == 0:
            hangman_ui.display_word_status()
            hangman_ui.display_hangman()
            hangman_game.enter_letter()
            hangman_game.display_result()

        if hangman_game._win_status == 2:
            hangman_game.input_username()
            hangman_game.record_score()
            hangman_game.display_hall_of_fame()
        elif hangman_game._win_status == 1:
            print("Game Over!")
            hangman_game.display_hall_of_fame()

        try_again_status = hangman_ui.display_end_game_message()

        if try_again_status == 1:
            hangman_game.reset_game()
            '''Reset the game state'''
        else:
            break   
        '''Exit the main loop if the player chooses not to play again'''

if __name__ == "__main__":
    main()


