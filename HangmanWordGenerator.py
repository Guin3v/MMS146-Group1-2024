import random

class HangmanWordGenerator:
    def __init__(self, wordbank_file='wordbank.txt'):
        self.wordbank_file = wordbank_file
        self.word_bank = self.load_word_bank()  # Fixed the typo here

    def load_word_bank(self):
        '''Load the word bank from the text file and return a dictionary of categories and words'''
        word_bank = {}
        try:
            with open(self.wordbank_file, 'r') as file:
                for line in file:
                    category, word = line.strip().split(':')
                    word_bank[category.strip()] = [word.strip() for word in word.split(',')]
        except FileNotFoundError:
            print("The wordbank.txt file was not found")
        except Exception as e:
            print(f"An error occurred while loading the word bank: {e}")
        return word_bank

    def get_random_word(self, category):
        '''Get a random word from the specified category'''
        if category in self.word_bank:
            return random.choice(self.word_bank[category])
        else:
            raise ValueError(f"Category '{category}' not found in the word bank.")

