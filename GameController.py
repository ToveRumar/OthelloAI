import GameViewer,AIPlayer,HumanPlayer, time,random
# get color from each player
# start game
# bool move is valid
GREEN=(0,255,0)
WHITE=(255,255,255)
BLACK=(0,0,0)
class GameController:

    def __init__ (self,size):
        self.rows = size
        self.cols = size
        
        self.playingField = self.createMatrix()
        self.viewer = GameViewer.GameViewer(self.rows, self.cols, 600, self, self.playingField)
        self.whitePlayer=AIPlayer.AIPlayer("W",self)
        self.blackPlayer=HumanPlayer.HumanPlayer("B",self)
        self.turn = self.blackPlayer  ##Make this a local variable in startnewgame
       
        self.startNewGame()
        

    def startNewGame(self):
        GameOver=False
        self.blackPlayer.setupFirstTwoTiles(self.rows)
        self.whitePlayer.setupFirstTwoTiles(self.cols)
        self.viewer.main()
        self.updateViewer()
        while(not GameOver):
            validMoves=self.turn.myMove(self.playingField)
            if validMoves:
                moveToMake=None
                self.viewer.showPossibleMoves(validMoves)
                if isinstance(self.turn,HumanPlayer.HumanPlayer):
                    while(moveToMake==None):
                        clickedTilePos=self.viewer.run()  
                        for move in validMoves:
                            if clickedTilePos==move.getPos():
                                moveToMake=move
                                break
                    
                elif isinstance(self.turn,AIPlayer.AIPlayer) :
                    time.sleep(2)
                    moveToMake=self.turn.calcBestMove(validMoves)
                         
                self.turn.makeMove(moveToMake.getPos())
                self.flipTiles(moveToMake.getTilesToFlip(),moveToMake.getColor())
                #self.calculatePoints()
                self.updateViewer()
                if self.turn==self.whitePlayer:
                    self.turn=self.blackPlayer
                else:
                    self.turn=self.whitePlayer
            else:
                GameOver=True
        self.viewer.drawGameOver()
        

                
            
       

    def createMatrix(self):
        tile_matrix = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(0)
               
            tile_matrix.append(row)
        return tile_matrix
    
    def updateViewer(self):
        self.calculatePoints()
        self.viewer.draw(self.playingField,self. whitePlayer.getPoints(), self.blackPlayer.getPoints())

  #  def handleClick(self, position):
       
        #self.players["HumanPlayer"].handleIncomingMove(position)
        
        #lägg till i placeTile

    def getAvailableTiles(self, position, playerColor):
        availableLiles = []

    def flipTiles(self,tilesToFlip,color):
        
        for position in tilesToFlip:
            self.playingField[position[0]][position[1]]=color
    def calculatePoints(self):
        whitepoints=0
        blackpoints=0
        for row in self.playingField:
            for tile in row:
                if tile=="W":
                    whitepoints+=1
                if tile=="B":
                    blackpoints+=1
        self.whitePlayer.setPoints(whitepoints)
        self.blackPlayer.setPoints(blackpoints)

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

        

GameController(4)


