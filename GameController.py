import GameViewer,AIPlayer,HumanPlayer, time
# get color from each player
# start game
# bool move is valid
GREEN=(0,255,0)
WHITE=(255,255,255)
BLACK=(0,0,0)
class GameController:

    def __init__ (self):
        self.rows = 4
        self.cols = 4
        
        self.playingField = self.createMatrix()
        self.viewer = GameViewer.GameViewer(self.rows, self.cols, 600, self, self.playingField)
        self.player1=AIPlayer.AIPlayer("W",self)
        self.player2=HumanPlayer.HumanPlayer("B",self)
        self.turn = self.player2
        self.players={}
        self.players["AIPlayer"]=self.player1
        self.players["HumanPlayer"]=self.player2
        self.startNewGame()
        

    def startNewGame(self):
        GameNotOver=True
        for player in self.players:
            self.players[player].setupFirstTwoTiles()
        self.viewer.main()
        while(GameNotOver):
            validMoves=self.turn.myMove(self.playingField)
            self.viewer.showPossibleMoves(validMoves)
            self.viewer.run()
            self.turn = self.player1
            self.turn.myMove(self.playingField)
            self.viewer.draw(self.playingField)
            self.turn=self.player2
       

    def createMatrix(self):
        tile_matrix = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(0)
                #row.append(tile.tile())
            tile_matrix.append(row)
        return tile_matrix
    
    def updateViewer(self):
        self.viewer.draw(self.playingField)

    def handleClick(self, position):
        print("handling cklick")
        self.players["HumanPlayer"].handleIncomingMove(position)
        self.updateViewer()
        #lägg till i placeTile

    def getAvailableTiles(self, position, playerColor):
        availableLiles = []

                
    def moveIsValid(self, position, playerColor):
        if self.playingField[position[0]][position[1]] == 0:
            return True
        else:
            return False

    def placeTile(self,position,playerColor):
        if  self.moveIsValid(position, playerColor):
            self.playingField[position[0]][position[1]] = playerColor
            
            return True
        else:
            return False

        

GameController()


