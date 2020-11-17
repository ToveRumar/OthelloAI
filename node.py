from enum import Enum
class node:
    def __init__(self):
        self.on=False
        self.state= 0 #Enum('State','OFF WHITE BLACK')

        #self.state=State.OFF
    def set_state(self,state):
        self.state=state
        
    def get_state(self):
        return self.state
    
    def is_on(self):
        return self.on

    def activate(self):
        self.on=True
        #self.state=State.WHITE
        return self.on

    
 