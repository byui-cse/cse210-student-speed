import random
from game import constants
from game.actor import Actor
from game.point import Point
class Word(Actor):
    """A list of Words. The responsibility of word is to keep track of the list of words and generate new ones as needed. 

    Stereotype:
        Information Holder
    Attributes: 
        _points (integer): The number of points the food is worth.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, set's the 
        text and moves the food to a random position within the boundary of the 
        screen.
        
        Args:
            self (Actor): an instance of Actor.
        """
        super().__init__()
        self.all_words = constants.LIBRARY
        self.new_word = random.choice(self.all_words)
        self._points = len(self.new_word)
        x = random.randint(1, constants.MAX_X - 2)
        y = random.randint(1, constants.MAX_Y - 2)
        self._position =Point(x,y)
        self._velocity = Point(1,0)
        
    
    def get_points(self):
        """Gets the points this word is worth.
        
        Args:
            self (Word): an instance of Word.
        Returns:
            integer: The points this Word is worth.
        """
        return self._points

    def reset(self):
        """Resets the words by moving it to a random position within the boundaries of the screen and reassigning the points to a random number.
        
        Args:
            self (Word): an instance of Word.
        """
        self.all_words = constants.LIBRARY
        self.new_word = random.choice(self.all_words)
        self._points = len(self.new_word)
        x = random.randint(1, constants.MAX_X - 2)
        y = random.randint(1, constants.MAX_Y - 2)
        self._position =Point(x,y)
        self._velocity = Point(1,0)