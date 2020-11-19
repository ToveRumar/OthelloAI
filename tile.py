from enum import Enum
WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)
class tile:
    def __init__(self):
        self.on=False
        self.state= GREEN #Enum('State','OFF WHITE BLACK')

        #self.state=State.OFF
    def set_tile_color(self,state):
        self.state=state

    def get_tile_color(self):
        return self.state
    
    def is_on(self):
        return self.on

    def activate(self):
        self.on=True
        self.state= RED
        return self.on

    
 