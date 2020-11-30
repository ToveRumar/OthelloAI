from Player import Player
import random
class AIPlayer(Player):
    
    def __init__(self,color,controller):
       
        Player.__init__(self,color,controller)
        self.name="AI"
    
    def getName(self):
        return self.name
    def setupFirstTwoTiles(self,boardSize):
        
        self.controller.placeTile([((boardSize//2)-1),((boardSize//2)-1)],self.color)
        self.controller.placeTile([(boardSize//2),(boardSize//2)],self.color)

    def myMove(self, playingField):
        validMoves=Player.returnValidMoves(self, playingField)
       
        return validMoves
        

    def calcBestMove(self,validMoves):
        moveToMake=validMoves[0]
        for move in validMoves:
            if moveToMake.getPoints()<move.getPoints():
                moveToMake=move   
       
        return moveToMake



#minimax returns pos for move
#makemove takes matrix, runs minimax,returns posiion to gamecontroller
