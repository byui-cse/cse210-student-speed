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
        self.letter = self._input_service.get_letter()
        

    def do_updates(self):
        #add letter to buffer(list)
        self.buffer.set_buffer(self.letter)
        #check words agenst dictionary for boolian
        if self._word.check_guess(self._buffer.get_buffer):
            #pass boolian to points
            #update points
            self.points.update_points()


    def do_outputs(self):
        #clear screen
        self._output_service.clear_screen()
        #display words
        self._output_service.draw_actor(self._word)
        #display points
        self._output_service.draw_actor(self._score)
        #flush buffer
        self._output_service.flush_buffer()