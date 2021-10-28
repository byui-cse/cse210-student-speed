from game import constants
from time import sleep
from game.word import Word
from game.score import Score
from game.player import Player
from game.buffer import Buffer


class Director:
    
    def __init__(self, input_service, output_service):
        self._word = Word()
        self.score = Score()
        self.player = Player()
        self._buffer = Buffer()
        self._keep_playing = True
        self._output_service = output_service
        self._input_service = input_service

    def start_game(self):
        while self._keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            sleep(constants.FRAME_LENGTH)

    def get_inputs(self):
        #grab words
        words = self._word.get_words()

        #capture player input get letter
        self._input_service.get_letter()
        

    def do_updates(self):
        #add letter to buffer(list)
        self.buffer.set_buffer()
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