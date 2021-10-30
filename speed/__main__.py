from game.director import Director
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen 
from game.timer import Timer

def main(screen):
    timer = Timer()
    input_service = InputService(screen, timer)
    output_service = OutputService(screen)
    director = Director(input_service, output_service)
    director.start_game(timer)

Screen.wrapper(main)