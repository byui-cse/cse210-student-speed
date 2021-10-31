# Implement Director code to run game
from time import sleep
from game.word import Word
from game.buffer import Buffer
from game.score import Score
from game import constants



class Director:
    def __init__(self, input_service, output_service):
        self._buffer = Buffer()
        self._keep_playing = True
        self.input_service = input_service
        self.output_service = output_service
        self._words = []
        self._score = Score()


    def start_game(self):
        # Initial bank of 5 words
        for i in range(5):
            self._words.append(Word())

        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)
        

    def _get_inputs(self):
        self._buffer.add_char(self.input_service.get_letter())

    def _do_updates(self):
        for word in self._words:
            word.move_next()
            if(not word.check_position()):
                # Checking if word has moved off of the screen and needs to be replaced
                self._words.remove(word)
                self._words.append(Word())
        if not len(self._buffer.get_chars()) == 0: 
            recent_char = self._buffer.get_chars()[len(self._buffer.get_chars()) - 1]
            if (recent_char == '*'):
                self._buffer.reset_buffer()
            else:
                for word in self._words:
                    if (self._buffer.compare(word.get_text())):
                        self._score.add_points(1)
                        self._words.remove(word)
                        self._words.append(Word())
                        continue
                    

    def _do_outputs(self):
        self.output_service.clear_screen()
        self.output_service.draw_actor(self._score)
        for word in self._words:
            self.output_service.draw_actor(word)
        self.output_service.draw_actor(self._buffer)
        self.output_service.flush_buffer()
            
