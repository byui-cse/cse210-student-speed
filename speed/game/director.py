from time import sleep
from game import constants
from game.word import Word
from game.score import Score
from game.buffer import Buffer
import random

from speed.game import buffer


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        word (Food): random words or an instance of Word
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        Buffer (Snake): The player or snake.
    """

    def __init__(self, input_service, output_service):
        """The class constructor. 
        
        Args:
            self (Director): an instance of Director.
        """
        self._word = Word()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._buffer = Buffer()
        self._letter = ""

        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._do_outputs()
            self._keep_playing
            self._get_inputs()
            self._do_updates()
            
            sleep(constants.FRAME_LENGTH)

    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if correct words, 

        Args:
            self (Director): An instance of Director.
        """
        
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._word) #word list???) 
        self._output_service.draw_actors(self._buffer)
        self._output_service.draw_actors(self.points)
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()


    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the letter input from user. 

        Args:
            self (Director): An instance of Director.
        """
        self._letter = self._input_service.get_letters() 


    def _do_updates(self):

        """Updates the game information for each round of play. In 
        this case, that means checking for correcct words / letter and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        self.buffer.display_letter(self._letter) # sends letter to buffer 
        self.list = self.buffer.make_list(self.letter)# create list in buffer to send to word
        self.word.check_word(self.list) # sends to word
  
        if self._input_service.get_result() == self._word.get_text():
            points = self._word.get_points()
            self._score.add_points(points)
            self._word.reset()
            self._input_service.reset()



     # pass key to add_letter to buffer
        # self._buffer.move_word(wordLocation)
        # create a word
        # save a wrd 





    





