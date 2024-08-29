from HangmanWordGenerator import HangmanWordGenerator
from HangmanGame import HangmanGame
from HangmanUI import HangmanUI

'Intialization of the classes for the front end and back end components of the game'
Hangman_BackEnd = HangmanGame(None, None, None, 8, HangmanWordGenerator())
Hangman = HangmanUI(Hangman_BackEnd)

'Main function that utilizes the methods of the classes'
def main():
    'Player chooses category and automatically generates a word form that category'
    Hangman.hangman_game.choose_category()
    secret_word = Hangman.hangman_game.word_generator.get_random_word(Hangman.hangman_game._our_categories)
    
    'Sets the generated word in the HangmanGame class as an attribute'
    Hangman.hangman_game.set_secret_word(secret_word)
    
    '''
    Runs the game loop of displaying the hangman, 
    the word status and prompting the player to enter a letter
    until the player runs out of guesses
    
    If the player guesses the word, they are prompted
    to give another category and given a new word
    to guess
    '''
    while Hangman.hangman_game._hangman_status < Hangman.hangman_game._max_attempts and not Hangman.hangman_game._win_status == '1':
        
        Hangman.display_hangman()
        Hangman.display_word_status()
        
        Hangman.hangman_game.enter_letter()
        Hangman.hangman_game.display_result()
        
        if Hangman.hangman_game._win_status == 2:
            Hangman.hangman_game.reset_guesses()
            main()
    
    'Displays the final state of the hangman'
    Hangman.display_hangman()
    'Prompts player to enter username'
    Hangman.hangman_game.input_username()
    'Stores username and score in the text file'
    Hangman.hangman_game.add_player_score()
    'Prints the Top 5 players'
    Hangman.display_hall_of_fame()
    'Prompts the player if they would like to play again or quit the game'
    Hangman.display_end_game_message()
    if Hangman.try_again_status == 1:
        Hangman.try_again_status = 0
        Hangman.hangman_game.reset_game()
        
        main()
        
'Runs the Main Function'
#driver code
main()
