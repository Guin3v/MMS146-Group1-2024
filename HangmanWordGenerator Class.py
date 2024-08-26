import random 

class HangmanWordGenerator:
  def __init__ (self):
    self.categories = {
          'Music Genres': [ 'Rock', 'Jazz', 'Pop', 'Classical', 'Blues',
                        'Alternative Rock', 'Metal', 'Funk', 'Country', 'Hip Hop'],

          'Cities' : ['Paris', 'London', 'New York', 'Tokyo', 'Seoul', 'Dubai',
                      'Manila', 'Jakarta', 'Kuala Lumpur', 'Rome'],
           
        
          'Animals' : ['Giraffe', 'Duck', 'Penguin', 'Parrot', 'Monkey',
                       'Turtle', 'Jaguar', 'Mantis', 'Shark', 'Spider'],

          'School Supplies': ['Paper', 'Highlighter', 'Marker', 'Eraser', 'Glue'
                              'Crayons', 'Watercolor', 'Pencil', 'Ballpen', 'Notebook'],  

          'Food': ['Yogurt', 'Tomato', 'Bagel', 'Chocolate', 'Potato', 'Croissant',
                   'Asparagus', 'Barbecue', 'Dragonfruit', 'Jalapeno']   
  
            }
    

    def get_secret_word (self, category): 
      if category in self.categories: 
        word = random.choice(self.categories[category])
        return word
''' if the category exists, it gets a random word from the categories and the word  gets returned'''
      else:
  ''' if category is not in the list'''
        raise ValueError ("Category not found")
