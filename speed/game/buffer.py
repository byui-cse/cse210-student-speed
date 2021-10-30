from game import constants
from game.actor import Actor
from game.point import Point

class Buffer(Actor):
    
    def __init__(self):
        super().__init__()
        self._buffer = ''
        self.set_position(Point(0, constants.MAX_X))
        self.set_velocity(Point(0, 0))
        self.set_text(f"Buffer: {self._buffer}")

    def get_buffer(self):
        return self._buffer

    
    def add_letter(self, letter):
        self._buffer += letter
        self.set_text(f"Buffer: {self._buffer}")
        
        
        
    def clear_buffer(self):
        self.set_position(Point(constants.MAX_X, 0))
        self.set_velocity(Point(0, 0))
        self._buffer = ''