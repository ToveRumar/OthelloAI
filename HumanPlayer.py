from Player import Player

class HumanPlayer:

    def __init__(self,color,controller):
        
        Player.__init__(self,color,controller)
    
    
    def setupFirstTwoTiles(self):
        self.controller.placeTile([1,2],self.color)
        self.controller.placeTile([2,1],self.color)