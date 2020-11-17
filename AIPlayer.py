from Player import Player

class AIPlayer(Player):
    
    def __init__(self,color,controller):
       
        Player.__init__(self,color,controller)
        

    def setupFirstTwoTiles(self):
        if self.color=="White":
            self.controller.placeTile([2,2],1)
        elif self.color=="Black":
            self.controller.placeTile([2,3],2)




#minimax returns pos for move
#makemove takes matrix, runs minimax,returns posiion to gamecontroller
