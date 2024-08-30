from AbstractGame import AbstractGame

class HangmanGame(AbstractGame):
    def __init__(self, player_username=None, our_categories=None, secret_word=None, max_attempts=8, word_gen=None, score=0):
        self.player_username = player_username
        self._our_categories = our_categories
        self._secret_word = secret_word
        self._guessed_letters = []
        self._incorrect_guesses = []
        self._hangman_status = 0
        self._guessed_words = 0
        self._win_status = 0
        self._max_attempts = max_attempts
        self.word_generator = word_gen
        self.score = score

    def choose_category(self):
        '''Prompt the player to type in a category.'''
        categories = ['Music Genres', 'Cities', 'Animals', 'School Supplies', 'Food', 'Body Organ', 'Color']

        print("\nAvailable categories:")
        for category in categories:
            print(f"- {category}")

        print("")
        chosen_category = input("Please type in your chosen category: ").strip().title()

        print("")
        if chosen_category in categories:
            self._our_categories = chosen_category
            print(f"You chose the {self._our_categories} category. \n")
        else:
            print("Invalid category. Please choose from the available categories.\n")
            self.choose_category()

    def set_secret_word(self, secret_word):
        self._secret_word = secret_word

    def enter_letter(self):
        '''Checks if a letter has been guessed already or is a valid guess, calls update_hangman() and check_guess()'''
        enter_letter = input("\nEnter a Letter: ").strip().lower()
        if len(enter_letter) != 1 or not enter_letter.isalpha():
            print("Invalid input. Please enter a single alphabet character")
        elif enter_letter in self._guessed_letters or enter_letter in self._incorrect_guesses:
            print("\nYou have already guessed that letter")
        else:
            self.update_hangman(enter_letter)
            self.check_guess(enter_letter)

    def check_guess(self, letter):
        '''Checks if the guessed letter is in the secret word and returns a statement of confirmation or negation'''
        if letter in self._secret_word:
            print(f"\nGood guess! {letter} is in the word.\n")
        else:
            print(f"\nSorry, {letter} is not in the word. You have {self._max_attempts - self._hangman_status} attempts left.\n")

    def update_hangman(self, letter):
        if letter in self._secret_word:
            self._guessed_letters.append(letter)
        else:
            self._hangman_status += 1
            self._incorrect_guesses.append(letter)

    def display_result(self):
        if len(self._incorrect_guesses) >= self._max_attempts:
            print(f"\nWe're sorry. You lose.")
            self._win_status = 1
        elif all(letter in self._guessed_letters for letter in self._secret_word):
            self._guessed_words += 1
            print("\nCongratulations! You got it!")
            self.score += 1
            self._win_status = 2
        else:
            return "\n"

    def input_username(self):
        '''Prompt the player to input their username after winning.'''
        username = input("Please enter your username to save your score: ").strip()

        if not username:
            raise ValueError("Username cannot be empty.")

        if username.isalnum():
            self.player_username = username
            print(f"Username {self.player_username} saved! You got {self._guessed_words} words!")
        else:
            print("Invalid username. Please enter a valid username (letters and numbers only).")

    def record_score(self):
        '''Record the player's score in the leaderboard file.'''
        print(f"Recording score for {self.player_username}: {self.score}")

        try:
            with open('leaderboard.txt', 'r') as file:
                scores = file.readlines()
                print("Existing scores:", scores)
        except FileNotFoundError:
            scores = []
            print("Leaderboard file not found, creating a new one.")

        score_dict = {}
        for line in scores:
            parts = line.strip().split(':')
            if len(parts) == 2:
                username, score = parts
                try:
                    score_dict[username] = int(score)
                except ValueError:
                    print(f"Skipping invalid score entry: {line.strip()}")

        print("Scoreboard:", score_dict)

        if self.player_username in score_dict:
            if self.score > score_dict[self.player_username]:
                print(f"Updating score for {self.player_username} from {score_dict[self.player_username]} to {self.score}")
                score_dict[self.player_username] = self.score
            else:
                print(f"Current score ({self.score}) did not beat previous score ({score_dict[self.player_username]}).")
        else:
            score_dict[self.player_username] = self.score
            print(f"Adding new player {self.player_username} with score {self.score}")

        with open('leaderboard.txt', 'w') as file:
            for username, score in score_dict.items():
                file.write(f"{username}:{score}\n")
            print("Scores are recorded.")

    def display_hall_of_fame(self):
        '''Display leaderboard of top 5 players with scores ranked from highest to lowest.'''
        try:
            with open('leaderboard.txt', 'r') as file:
                scores = file.readlines()

            score_list = [(line.strip().split(':')[0], int(line.strip().split(':')[1])) for line in scores]
            sorted_scores = sorted(score_list, key=lambda x: x[1], reverse=True)

            print("\nTop 5 Players on the leaderboard:")
            for rank, (username, score) in enumerate(sorted_scores[:5], start=1):
                print(f"{rank}. {username}: {score}")
        except FileNotFoundError:
            print("No scores found in the leaderboard.")
        except Exception as e:
            print(f"An error occurred while displaying the leaderboard: {e}")

    def reset_guesses(self):
        self._win_status = 0
        self._secret_word = None
        self._guessed_letters.clear()
        self._incorrect_guesses.clear()

    def reset_game(self):
        self._secret_word = None
        self._guessed_words = 0
        self._hangman_status = 0
        self._guessed_letters.clear()
        self._incorrect_guesses.clear()
        self._win_status = 0
