# this needs to pick random words from the words.txt file 
#these words are those that will cross the screen and the player
#will have to copy/type them  as they pass, in order to play.
import random

class Words:
    """ This creats a list of words from the words.txt file. It then chooses 5 random words from 
    that file. 
    
    """
    def __init__(self):
        """ this is the class constructor
        
        args:  self (Words)  and instance of words
        
        """
        super().__init__()
        self.letters()
        self.trial_words = []
        self._prepare_body() #using this from snake. this will put the letters on the screen
        

    def get_words(self):
        """ this gets the words from the txt file and splits them in to a list. 
        
        Args: self (Words) and instance of words
         Returns: list of words
        """

        with open('words.txt','r') as w:
            w.strip().split(',')
            words = random.sample(w, 5)
        return words  

    def get_letters(self,get_words):
        """ I want this to take the list of random words created in get_words
        and take each word string and seperate it in to letters. """

        self.get_words = get_words

        return list(get_words) # I want to take eachstring and seperate it in to individual 
                                #letters, i'm not sure this will do it. 