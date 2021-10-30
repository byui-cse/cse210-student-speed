from game import constants
from game.actor import Actor
from game.point import Point

class Buffer:
    """A limbless reptile. The responsibility of Snake is keep track of its segments. It contains methods for moving and growing among others.

    Stereotype:
        Structurer, Information Holder

    Attributes:
        _body (List): The snake's body (a list of Actor instances)
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Buffer): An instance of Buffer.
        """
        super().__init__()
        self._segments = []
        self._prepare_buffer()
    
    def get_all(self):
        """Gets all the stored segments.
        
        Args:
            self (Buffer): An instance of buffer.

        Returns:
            list: The buffers's segments.
        """
        return self._segments

    def convert_to_string(self):
        string = ""
        for i in self._segments[1:]:
            string += i.get_text()
        
        return string
    
    def add_letters(self, letter):
        """
            If enter key is hit clear and reset buffer if not retreve the letters form the input 
            service and returns the value to the buffer.

        Args:
            self (Buffer): An instance of buffer.
            direction (Point): The direction to move.
        """
        if letter == "*":
            self._prepare_buffer()
        else:
            self._add_segment(letter,Point(len(letter.get_text()),constants.MAX_Y), Point(0.0))

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