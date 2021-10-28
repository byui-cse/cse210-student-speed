import random
from game.actor import Actor
from game.point import Point

class Score(Actor):
    """Points earned. The responsibility of Score is to keep track of the player's points.

    Stereotype:
        Information Holder

    Attributes: 
        _points (integer): The number of points the food is worth.
    """

  
    def __init__(self):
        # Need to call superclass
        # call all attributes
        # set postion equal to 1,0 using the Point class
        # self.set_postion(position)
        # self.set_text(as shown in requirements)
        pass

  
    def add_points(self, points):

        """Adds the given points to the running total and updates the text.
        
        Args:
            self (Score): An instance of Score.
            points (integer): The points to add.
        """
        self._points += points
        self.set_text(f"Score: {self._points}")

        pass