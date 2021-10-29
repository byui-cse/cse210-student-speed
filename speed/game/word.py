from game.actor import Actor
from game.buffer import Buffer
from game import constants
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
        self.goal_words = []
    
    def get_words(self):
        """Gets all the player's words.
        
        Args:
            self (Word): An instance of word.
        pass

    def check_guess(self, guess):
        pass
    
        Returns:
            list: The word's letters.
        """
        # Open the file in read mode
        with open("words.txt", "r") as file:
            allText = file.read()
            words = list(map(str, allText.split()))
  
            # print random string of 5 words in self.goal_words list
            for n in range(1,5):
                self.goal_words.append(random.choice(words)) 

            return self.goal_words  


    def check_guess(self, Buffer):
        """Prepares the word guess by adding letters.
        
        Args:
            self (Word): an instance of Word.
        """
        for word in self.goal_words:
            if word in Buffer:
                return True
            else:
                False

    def reset_goal_words(self):
        self.goal_words = []