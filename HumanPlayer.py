from Player import Player

class HumanPlayer(Player):

    def __init__(self,color,controller):
        
        Player.__init__(self,color,controller)
    
    
    def setupFirstTwoTiles(self):
        self.controller.placeTile([1,2],self.color)
        self.controller.placeTile([2,1],self.color)

    def handleIncomingMove(self, position):
        print("player hanling move")
        Player.makeMove(self,position)

    def myMove(self, playingField):

        return Player.returnValidMoves(self, playingField)

