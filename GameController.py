import node, GameViewer,AIPlayer,HumanPlayer
# get color from each player
# start game
# bool move is valid

class GameController:

    def __init__ (self):
        self.rows = 4
        self.cols = 4
        
        self.playingField = self.createMatrix()
        self.viewer = GameViewer.GameViewer(self.rows, self.cols, 600, self, self.playingField)
        
        self.players=[AIPlayer.AIPlayer("White",self),HumanPlayer.HumanPlayer("Black",self)]
        self.startNewGame()
        self.viewer.main()
        self.viewer.run()

    def setPlayers(self):
        self.players=[AIPlayer.AIPlayer("White",self),HumanPlayer.HumanPlayer("Black",self)]

    def createMatrix(self):
        node_matrix = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(node.node())
            node_matrix.append(row)
        return node_matrix
    
    def updateViewer(self):
        self.viewer.draw(self.playingField)

    def newMove(self, node):
        node.activate()
        self.updateViewer()

    def startNewGame(self):
        for player in self.players:
            player.setupFirstTwoTiles()

    def placeTile(self,position,playerNbr):
        self.playingField[position[0]][position[1]].set_state(playerNbr)

GameController()