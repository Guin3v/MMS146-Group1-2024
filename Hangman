#Tentative implementation of combining the HangmanGame and HangmanUI objects into final program.

from HangmanUI import HangmanUI
from HangmanGame import HangmanGame        

#The 8 within the HangmanGame class represents the max attempts, I simplified it to test the display_hangman() method
test = HangmanUI(HangmanGame(8))
while len(test.hangman._incorrect_guesses) < test.hangman._max_attempts:
    test.display_hangman()
    test.hangman.enter_letter()
test.display_hangman()

