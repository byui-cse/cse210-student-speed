from game import constants
from game.actor import Actor
from game.point import Point
import random

class Words(Actor):

    """A list of many actors creating a list of words. Facilitates the points per word, 
    and the generation of new words.

    Stereotypes:
        Information Holder

    Attributes:
        _words (list): a list to contain all of our instances of word actors.
        _points (int): keeping track of points in a given word.
    """
   
    def __init__(self):
        # call the superclass()
        # set all attributes
        # call _prepare_list()
        pass

    
    def get_all(self):
        # return all words
        pass

    
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
        # word set it equal to Actor()
        # set the test of our word equal to text
        # set the position of our word to position
        # set the velocity of our word to velocity
        # append word to words
        pass

  
    def _prepare_list(self):
        # for range of the constant STARTING_WORDS
            # set x equal to half of the constant MAX X
            # set y equal to half of the constant MAX Y
            # set text equal to a random word from constant LIBRARY
            # set position equal to x, y - current index using the Point class
            # set velocity equal to 1,0 using Point class
            # call the add_word function and pass, text, position, velocity
        pass

    def _set_points(self, word):
        # set _points equal to the length of word
        pass