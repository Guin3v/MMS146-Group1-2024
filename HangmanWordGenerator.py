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
                   'Asparagus', 'Barbecue', 'Dragonfruit', 'Jalapeno'], 

          'Body Organ': ['Skin', 'Heart', 'Brain', 'Intestine', 'Liver',
                        'Kidney', 'Stomach', 'Lungs', 'Bladder', 'Pancreas'],
    
          'Color': ['Blue', 'White', 'Red', 'Orange', 'Brown',
                   'Turquoise', 'Green', 'Fuschia', 'Violet', 'Black']
  
            }
    

  def get_random_word (self, category): 
      if category in self.categories: 
        word = random.choice(self.categories[category])
        return word.lower()

      else:
        raise ValueError ("Category not found")
