from time import sleep
from game import constants
from game.score import Score

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
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        
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
        that means getting the ...

        Args:
            self (Director): An instance of Director.
        """
        pass

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking ... and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        pass
        
    def _do_outputs(self):
        """

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actor(self.)
        self._output_service.draw_actors(self.)
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()

    def _(self):
        """

        Args:
            self (Director): An instance of Director.
        """
        pass

    def _(self):
        """

        Args:
            self (Director): An instance of Director.
        """
        pass