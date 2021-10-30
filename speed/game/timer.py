import time
from game.actor import Actor
from game.point import Point
import asyncio
from game import constants


# define the countdown func.
class Timer(Actor):

    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.

        Args:
            self (Score): an instance of Score.
        """
        super().__init__()
        # self._points = 0
        position = Point(1, 1)
        self.set_position(position)
        # self.set_text(f"Timer: {self.timer}") #broken
        self.set_position(Point(0, constants.MAX_Y))
        self.set_velocity(Point(0, 0))

    def get_input(self):
        # input time in seconds
        self.t = input("Please enter the amount of time you would like to play in seconds: ")
        self.mins, self.secs = divmod(self.t, 60)
        self.timer = '{:02d}:{:02d}'.format(self.mins, self.secs)
        self.set_text(f"Timer: {self.timer}")

    async def countdown(self):
    
        while self.t:
            self.mins, self.secs = divmod(self.t, 60)
            self.timer = '{:02d}:{:02d}'.format(self.mins, self.secs)
            # print(self.timer, end="\r")
            self.set_text(f"Timer: {self.timer}")
            time.sleep(1)
            self.t -= 1
        
        print('Fire in the hole!!')


    # input time in seconds
    # t = input("Please enter the amount of time you would like to play in seconds: ")

    # function call
    # countdown(int(t))

