from game import constants
from game.actor import Actor
from game.point import Point
import random

class Word(Actor):

    """A list of many actors creating a list of words. Facilitates the points per word, 
    and the generation of new words.

    Stereotypes:
        Information Holder

    Attributes:
        _words (list): a list to contain all of our instances of word actors.
        _points (int): keeping track of points in a given word.
    """
   
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Word): An instance of word.
        """
        # call the superclass()
        # set all attributes
        # call _prepare_list()
        super().__init__()
        self.all_words = constants.LIBRARY
        self._words_list = {}

  
    def get_all(self):
        # return all words
        return self._words_list

    
    def move_word(self, word, x, y):
        # direction equal to x,y using the Point class
        # word = self._words[word]
        # word.set_velocity equal to direction
        # word.move_next()
        pass

    
    def word_check(self, word):
        # loop through the range of words
            # set text equal to self._words at current index
            # if text.get_text() is equal to word
                # call the set points function and pass the current word
                # set the current word to a new random word
                # return points
        # return 0
        pass

   
    def _add_word(self, text, position, velocity):
        text = Actor()# word set it equal to Actor()
        self.get_text = text # set the test of our word equal to text
        self.get_position = position # set the position of our word to position
        self.get_velocity = velocity# set the velocity of our word to velocity
        self._words_list.append(text)    # append word to words
        

  
    def _prepare_list(self):
       
            
            
            
            
            
            
        for i in range(constants.STARTING_WORDS):                       # for range of the constant STARTING_WORDS
            random_word = self.all_words[random.randint(0,10000)]       # set text equal to a random word from constant LIBRARY
            x = random.randint(2, constants.MAX_X)                      # set x equal to half of the constant MAX X 
            y = random.randint(2, constants.MAX_Y)                      # set y equal to half of the constant MAX Y
            position = self.set_position(x,y)                                      # set position equal to x, y - current index using the Point class
            velocity = Point(1,0)                                       # set velocity equal to 1,0 using Point class

            self._add_word(random_word,position, velocity )             # call the add_word function and pass, text, position, velocity

    def _set_points(self, word):
        # set _points equal to the length of word
        pass