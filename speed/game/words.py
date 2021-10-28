# this needs to pick random words from the words.txt file 
#these words are those that will cross the screen and the player
#will have to copy/type them  as they pass, in order to play.
import random

class Words:
    """ This creats a list of words from the words.txt file. It then chooses 5 random words from 
    that file. """

    def game_words(self):
        

        with open('words.txt','r') as w:
            w.strip().split(',')
            words = random.sample(w, 5)
        return words     