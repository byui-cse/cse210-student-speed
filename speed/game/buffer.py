from game.actor import Actor
from game.point import Point
from game import constants

class Buffer(Actor):
    """Points earned. The responsibility of Buffer is to keep track of the players letters.

    Stereotype:
        Information Holder

    Attributes: 
        _word (string): The letters in the word so far.
    """
   
    def __init__(self):
        # you need to call the superclass init function
        # add all attributes
        # set the position equal to 1, MAX_Y using the Point class
        # self.set_postion(postion)
        # self.set_text(as demonstarted in requirements)
        
        _text = ""
        

    
    def add_letter(self, letter):
        # set word equal to word + letter
        # reset self.set_text(as demonstarted in requirements)
        """Adds the given letter to the word and sets the buffer text with the word and letter.
        
        Args:
            self (set_text): An instance of word.
            letter (letter): An instance of letter
        """
        #word = word + letter
        #self.set_text(f"Buffer: {word}")

        pass

    
    def get_word(self):
        # return the word
        pass

    
    def reset(self):
        # set word equal to an empty string
        pass