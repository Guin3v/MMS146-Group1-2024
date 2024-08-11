# MMS146-Group1-2024
Game Overview

The text-based Hangman game will provide users with a fun and interactive way to play the classic word-guessing game. Players will try to guess a secret word by suggesting letters within a certain number of attempts while avoiding getting "hanged" by making too many incorrect guesses.


For example, for the category ‘Countries’ and word ‘Nepal’, the initial display should be


_ _ _ _ _


For the category ‘Songs’ and word ‘Just the way you are’, the initial display should be:


_ _ _ _    _ _ _    _ _ _    _ _ _    _ _ _


Key Features

1. Category Selection
Let the player choose a category where the random word will come from.

2. Word Selection
Implement a word bank or word generator to select a random word for each game.
Choose words of varying lengths and difficulty levels for player engagement.

3. Gameplay Mechanics
Display the secret word as a series of blanks to be filled in by correct guesses.
Allow players to input letter guesses and provide feedback on correctness.
Track the number of incorrect guesses and update the hangman visual representation accordingly.

4. Game End Conditions
End the game when the player correctly guesses the word or runs out of attempts.
Display the result (win/loss) and reveal the hidden word at the end of the game.

5. Replayability:
Allow players to start a new game after completing or losing a game.
Implement a scoring system

Class Structure

These are the classes and their specifications that you are expected to implement:

1. HangmanGame Class
Attributes:
secret_word - a random word to be guessed by the player
guessed_letters - correct guesses of the player
incorrect_guesses - incorrect guesses of the player
max_attemps - number of incorrect guesses allowed

Methods:
check_guess - check if the guess of the player is correct or not
update_hangman - update the hangman for each turn
display_result - display the result of the game (win/lose)

2. HangmanUI Class
Methods:
display_hangman - display a visual representation of the Hangman
display_word_status - display the word, revealing the letter each the a player makes a correct guess
display_end_game_message - display a message when a player quits the game

3. HangmanWordGenerator Class
Methods
get_random_word - generate a random word from the list of words

Notes in implementing the Hangman Game:

Utilize inheritance and polymorphism to structure classes efficiently.
Use encapsulation for data protection and modularity.
Implement a game loop for user interaction and gameplay progression.
Implement error handling for edge cases like invalid inputs.

BONUS: Add the following features to this game to get bonus points:

Save the word bank to a text file. Every time a player starts a game, a word from the text file is loaded to the game.
Allow players to try to beat their previous best score. The scores of each player must be saved to a text file in order to do this.
Display the Hall of Fame at the end of each game. The Hall of Fame is a list of players who got the highest scores. The list should be the name of the top 5 players and their score, arranged from highest to lowest.
Add an abstract class and implement it in your program.

