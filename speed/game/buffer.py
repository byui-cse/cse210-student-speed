from game import constants
from game.actor import Actor
from game.point import Point
# Buffer-lyfe--zach

class Buffer:

    def __init__(self):
        self.guess_list = []
        self.x = 50
        self.dashes = "-"*self.x
  

    def make_list(self,user_input):#adds user input to list of guesses
        self.guess_list.add(user_input)
        self.x -= 1
        return self.guess_list

    def display_buffer(self):#prints buffer "Buffer: (guess_list in string form) (correct amount of dashes)"
        print(f"-Buffer: {''.join(str(i) for i in self.guess_list)}{self.dashes}")


    def clear_buffer(self):#clears list to restart buffer if player hits enter
        self.x = 50
        self.guess_list.clear()
       
