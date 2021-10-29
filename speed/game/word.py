from game.player import ImportService
import random

class Word(ImportService):
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
  
            # print random string
            print(random.choice(words))

    def reset_goal_words(self):
        pass