from game.actor import Actor
from game.buffer import Buffer
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
        self.goal_words = []
        self._points = 0
        self.set_text("@")
        self.reset_goal_words()
    
    def get_words(self):
        """Gets all the actor's words.
        
        Args:
            self (Word): An instance of word.
        pass
        """
        # Open the file in read mode
        with constants.LIBRARY as words: 
        # with open("/words.txt", "r") as file:
            # allText = file.read()
            # words = list(map(str, allText.split()))
  
            # select random string of 5 words in self.goal_words list
            for n in range(1,5):
                self.goal_words.append(random.choice(words)) 

            return self.goal_words  

    def check_guess(self, Buffer):
        """Prepares the word guess by adding letters.
        
        Args:
            self (Word): an instance of Word.

        Returns:
            list: The word's letters.
        """
        for word in self.goal_words:
            if word in Buffer:
                return True
            else:
                False

    def reset_goal_words(self):
        """Resets the words by moving them to random positions within the boundaries of the
        screen and reassigning a new random list of five words.
        
        Args:
            self (Word): an instance of Word.
        """
        self.goal_words = []
        self.goal_words.append(random.choice(words)) 
        x = random.randint(1, constants.MAX_X -2)
        y = random.randint(1, constants.MAX_Y - 2)
        position = Point(x, y)
        self.set_position(position)