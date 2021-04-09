from pynput.mouse import Button, Controller 
import random
#this  code is a simple virus it basically moves the mouse>
mouse = Controller()
def position():
        x = random.uniform(0, 1000)
        y = random.uniform(0, 1000)
        mouse.position = (x, y)
def mouse_position():
        while True:
                position()


mouse_position()






