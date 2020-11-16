import node, GameViewer
# get color from each player
# start game
# bool move is valid

class GameController:

    def __init__ (self):
        self.rows = 4
        self.cols = 4
        self.playingField = self.createMatrix()
        self.Viewer = GameViewer.GameViewer(self.rows, self.cols, 600, self, self.playingField)

    def createMatrix(self):
        node_matrix = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(node.node())
            node_matrix.append(row)
        return node_matrix
    
    def updateViewer(self):
        self.Viewer.draw(self.playingField)

    def newMove(self, node):
        node.activate()
        self.updateViewer()



GameController()