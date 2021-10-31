from time import sleep
from game.score import Score
from game.word import Word
from game.buffer import Buffer
from game import constants
class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._words = []
        self.input_service = input_service
        self._keep_playing = True
        self.output_service = output_service
        self._score = Score()
        self._buffer = Buffer()

        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        for i in range(8):
            self._words.append(Word())
            
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the adding the letter to the buffer and moving the word to the next spot.

        Args:
            self (Director): An instance of Director.
        """
        #self._buffer.add_letters(self._input_service.get_letter())
        #for word in self._words:
           # word.move_next()
        self._buffer.add_char(self.input_service.get_letter())

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking ... and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        for word in self._words:
            word.move_next()
            if(not word.check()):
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
        """

        Args:
            self (Director): An instance of Director.
        """
        
        self.output_service.clear_screen()
        self.output_service.draw_actor(self._score)
        for word in self._words:
            self.output_service.draw_actor(word)
        self.output_service.draw_actor(self._buffer)
        self.output_service.flush_buffer()

    def _check_word(self):
        """
        see if the typed word is on the list of words

        Args:
            self (Director): An instance of Director.
        """
        attempt = self._buffer.convert_to_string()

        for word in self._words:
            actual_word = word.get_text()

            if attempt == actual_word: 
                self._score.add_points(word.get_points())
                word.reset()

   