from game.actor import Actor

class Buffer(Actor):
    
    def __init__(self):
        self._word = ''
        self._letter = ''

    def get_buffer(self):
        return self._word

    def set_buffer(self):
        self._word = self._word + self._letter
    
    def get_letter(self):
        return self._letter
    
    def set_letter(self):
        self._letter = self._input_service.get_letter()
        
        