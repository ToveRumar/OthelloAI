from Player import Player
import random
class AIPlayer(Player):
    
    def __init__(self,color,controller):
       
        Player.__init__(self,color,controller)
        

    def setupFirstTwoTiles(self):
        
        self.controller.placeTile([1,1],self.color)
        self.controller.placeTile([2,2],self.color)

    def myMove(self, playingField):
        validMoves=Player.returnValidMoves(self, playingField)
       
        return validMoves
        


       




#minimax returns pos for move
#makemove takes matrix, runs minimax,returns posiion to gamecontroller
