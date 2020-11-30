from Player import Player

class HumanPlayer(Player):

    def __init__(self,color,controller):
        
        Player.__init__(self,color,controller)
        self.name="Human"
        
    def getName(self):
        return self.name
        
    def setupFirstTwoTiles(self, boardSize):
        self.controller.placeTile([((boardSize//2)-1),(boardSize//2)],self.color)
        self.controller.placeTile([(boardSize//2),((boardSize//2)-1)],self.color)

    def handleIncomingMove(self, position):
        
        Player.makeMove(self,position)

    def myMove(self, playingField):
        validMoves=Player.returnValidMoves(self, playingField)
        
        
        return validMoves
       

