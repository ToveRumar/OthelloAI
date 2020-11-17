from Player import Player
WHITE=(255,255,255)
BLACK=(0,0,0)
class AIPlayer(Player):
    
    def __init__(self,color,controller):
       
        Player.__init__(self,color,controller)
        

    def setupFirstTwoTiles(self):
        
        self.controller.placeTile([2,2],self.color)
       




#minimax returns pos for move
#makemove takes matrix, runs minimax,returns posiion to gamecontroller
