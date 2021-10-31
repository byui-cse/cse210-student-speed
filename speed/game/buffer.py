from game import constants
from game.actor import Actor
from game.point import Point

class Buffer(Actor):
    def __init__(self):
        super().__init__()
        self.chars = ''
        self._position._y = constants.MAX_Y - 1


    def add_char(self, char):
        self.chars += char
        self.set_text(f'Buffer:{self.chars}')

    def get_chars(self):
        return self.chars

        """
        Returns:
            list: The buffers's segments.
        """
        return self._segments
    
    def add_letters(self, letter):
        """
            If enter key is hit clear and reset buffer if not retreve the letters form the input 
            service and returns the value to the buffer.
        """


    def compare(self, string):
        if (string in self.chars):
            return True
        else:

            return False

    def reset_buffer(self):
        self.chars = ''
        self.set_text(f'Buffer:{self.chars}')

        #self._add_segment(letter,Point(len(letter),constants.MAX_Y), Point(0,0))

    def _add_segment(self, text, position, velocity):
        """Adds a new segment to the buffer using the given text, position and velocity.

        Args:
            self (Snake): An instance of snake.
            text (string): The segment's text.
            position (Point): The segment's position.
            velocity (Point): The segment's velocity.
        """
        segment = Actor()
        segment.set_text(text)
        segment.set_position(position)
        segment.set_velocity(velocity)
        self._segments.append(segment)

    def _prepare_buffer(self):
        """Clears out the buffer and sets new values for starting positions.
        
        Args:
            self (Buffer): an instance of Buffer.
        """
        self._segments.clear()
        message ="- Buffer: "
        position = Point(1,constants.MAX_Y)
        velocity = Point(0,0)
        self._add_segment(message,velocity, position)

    def convert_to_string(self):
        """
        Converts current list item to a text string 
        """
        string = ""
        for i in self._segments[1:]:
            string += i.get_text()
        
        return string


