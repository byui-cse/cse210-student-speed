from game import constants
from time import sleep
from game.word import Word
from game.score import Score
from game.player import Player
from game.buffer import Buffer


class Director:
    
    def __init__(self):
        self._word = Word()
        self.score = Score()
        self.player = Player()
        self._buffer = Buffer()
        self._keep_playing = True

    def start_game(self):
        while self._keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            sleep(constants.FRAME_LENGTH)

    def get_inputs(self):
        #grab words
        #capture player input get letter
        
        pass

    def do_updates(self):
        #add letter to buffer(list)
        #check words agenst dictionary for boolian
        #pass boolian to points
        #update points
        
        pass

    def do_outputs(self):
        #clear screen
        #display words
        #display points
        #flush buffer
        pass