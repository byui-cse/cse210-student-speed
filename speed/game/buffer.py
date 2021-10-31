from game import constants
from game.actor import Actor

class Buffer(Actor):
    """A buffer to type words for the speed. The responsibility of Buffer is to type the words as they appear to the screen. Words move fast, and the user must type them fast to gain piont. 
    
    Stereotype:
        Information Holder

    Attributes: 
        _points (integer): The number of points the speed is worth.
    """
    def __init__(self):
        super().__init__()
        self.chars = ''
        self._position._y = constants.MAX_Y - 1

    def add_char(self, char):
        self.chars += char
        self.set_text(f'Buffer: {self.chars}')

    def get_chars(self):
        return self.chars

    def compare(self, string):
        if (string in self.chars):
            return True
        else:
            return False
    

    def reset_buffer(self):
        """Resets the buffer by moving it to a random position within the boundaries of the screen and reassigning the points to a random number.
        
        Args:
            self (Buffer): an instance of Buffer.
        """
        self.chars = ''
        self.set_text(f'Buffer:{self.chars}')