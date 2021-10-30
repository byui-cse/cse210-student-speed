from game.actor import Actor
from game import constants
from game.point import Point
import random

class Word(Actor):
    """A floating collection of letters. The responsibility of Word is keep track of its segments. 
    It contains methods for moving and growing among others.

    Stereotype:
        Structurer, Information Holder

    Attributes:
        _body (List): The word's body (a list of ImportService instances)
    """
    
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Word): An instance of word.
        """
        super().__init__()
        self._word = ""
        #self._points = 0
        #self.set_text("@")
        self.reset()
    
    def get_word(self):
        """Gets all the actor's words.
        
        Args:
            self (Word): An instance of word.
        pass
        """      
        return self._word

    def check_guess(self, Buffer):
        """Prepares the word guess by adding letters.
        
        Args:
            self (Word): an instance of Word.

        Returns:
            list: The word's letters.
        """
        if self._word in Buffer:
            return True
        else:
            return False

    def reset(self):
        """Resets the words by moving them to random positions within the boundaries of the
        screen and reassigning a new random list of five words.
        
        Args:
            self (Word): an instance of Word.
        """
        self._word = random.choice(constants.LIBRARY)

        x = random.randint(1, constants.MAX_X -2)
        y = random.randint(1, constants.MAX_Y - 2)        
        self.set_position(Point(x, y))
        self.set_velocity(Point(1, 0))
        self.set_text(self._word)