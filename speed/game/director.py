from game import constants
from time import sleep
from game.word import Word
from game.score import Score
from game.buffer import Buffer


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        word (Word): The player's goal.
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
        self._word = Word()
        self.score = Score()
        self._buffer = Buffer()
        self._keep_playing = True
        self._output_service = output_service
        self._input_service = input_service


    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            sleep(constants.FRAME_LENGTH)


    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired word and capturing the player input by getting
        the letter.

        Args:
            self (Director): An instance of Director.
        """
        #grab words
        words = self._word.get_words()

        #capture player input get letter
        self._buffer.set_letter()
        self.letter = self._buffer.get_letter()
        

    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means adding a letter to the buffer, checking words against
        the dictionary for boolean, and updating points when passed.

        Args:
            self (Director): An instance of Director.
        """
        #add letter to buffer(list)
        self.buffer.set_buffer()
        #check words agenst dictionary for boolean
        if self._word.check_guess(self._buffer.get_buffer):
            #pass boolean to points
            #update points
            self.score.add_points(5)
        if self.letter == '*':
            self._word.reset_goal_words()


    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are words remaining and displaying
        the proper information (i.e. words and points).

        Args:
            self (Director): An instance of Director.
        """
        #clear screen
        self._output_service.clear_screen()
        #display words
        self._output_service.draw_actor(self._word)
        #display points
        self._output_service.draw_actor(self._score)
        #flush buffer
        self._output_service.flush_buffer()