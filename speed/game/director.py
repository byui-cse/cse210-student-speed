from time import sleep
from game import constants
from game.score import Score
from game.word import Word
from game.buffer import Buffer

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
        for i in range (constants.STARTING_WORDS):
            word = Word()
            self._words.append(word)
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._buffer = Buffer()

        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
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
        self._buffer.add_letters(self._input_service.get_letter())
        for word in self._words:
            word.move_next()

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking ... and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        self._check_word()
        
    def _do_outputs(self):
        """

        Args:
            self (Director): An instance of Director.
        """
        
        self._output_service.clear_screen()
        for word in self._words:
            self._output_service.draw_actor(word)
        self._output_service.draw_actors(self._buffer.get_all())
        self._output_service.draw_actor(self._score)
        self._output_service.print_text(self._buffer.convert_to_string())
        self._output_service.flush_buffer()

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

   