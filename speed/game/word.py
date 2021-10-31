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
        #super().__init__()
        #self.all_words = constants.LIBRARY
        #self.new_word = random.choice(self.all_words)
        #self._points = len(self.new_word)
        #x = random.randint(1, constants.MAX_X - 2)
        #y = random.randint(1, constants.MAX_Y - 2)
        #self._position =Point(x,y)
        #self._velocity = Point(1,0)
        super().__init__()

        self.set_text(constants.LIBRARY[random.randint(0, len(constants.LIBRARY) - 1)])
        self.set_position(Point(0, random.randint(constants.MAX_Y / 4, constants.MAX_Y - 4))) 
        self.set_velocity(Point(random.randint(1, 3), 0))

        self.all_words = constants.LIBRARY
        self.new_word = random.choice(self.all_words)
        self._points = len(self.new_word)
        x = random.randint(2, constants.MAX_X)
        y = random.randint(2, constants.MAX_Y)
        self._position =Point(x,y)
        self._velocity = Point(1,0)

        
    
    def move_text(self):
        self.set_position(self.get_position().add(self.get_velocity()))        

    
    
    def check(self):
        """Resets the words by moving it to a random position within the boundaries of the screen and reassigning the points to a random number.
        
        Args:
            self (Word): an instance of Word.
        """
        if (self.get_position().get_x() + (len(self.get_text()) - 1) > constants.MAX_X):
            return False
        return True