import tile, GameViewer,AIPlayer,HumanPlayer
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
        
        self.players=[AIPlayer.AIPlayer(WHITE,self),HumanPlayer.HumanPlayer(BLACK,self)]
        self.startNewGame()
        self.viewer.main()
        self.viewer.run()

    def setPlayers(self):
        self.players=[AIPlayer.AIPlayer("White",self),HumanPlayer.HumanPlayer("Black",self)]

    def createMatrix(self):
        tile_matrix = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(tile.tile())
            tile_matrix.append(row)
        return tile_matrix
    
    def updateViewer(self):
        self.viewer.draw(self.playingField)

    def newMove(self, tile):
        tile.activate()
        self.updateViewer()
        #lägg till i placeTile

    def getAvailableTiles(self, position, playerColor):
        availableLiles = []


    def startNewGame(self):
        for player in self.players:
            player.setupFirstTwoTiles()
                
    def moveIsValid(self, position, playerColor):
        if self.playingField[position[0]][position[1]].get_tile_color() == GREEN:
            print(self.playingField[position[0]][position[1]].get_tile_color() == GREEN)
            return True
        else:
            return False

    def placeTile(self,position,playerColor):
        if  self.moveIsValid(position, playerColor):
            self.playingField[position[0]][position[1]].set_tile_color(playerColor)
            return True
        else:
            return False

        

GameController()


