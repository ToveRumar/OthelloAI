from Player import Player

class HumanPlayer:

    def __init__(self,color,controller):
        
        Player.__init__(self,color,controller)
    
    
    def setupFirstTwoTiles(self):
        if self.color=="White":
            self.controller.placeTile([2,2],1)
        elif self.color=="Black":
            self.controller.placeTile([2,3],2)