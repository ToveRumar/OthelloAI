class Move:
    def __init__ (self, pos, points, color,tilesToFlip):
        self.pos = pos
        self.points = points
        self.color = color
        self.tilesToFlip=tilesToFlip
        
    def getPos(self):
        return self.pos

    def getPoints(self):
        return self.points
    
    def getColor(self):
        return self.color
    
    def getTilesToFlip(self):
        return self.tilesToFlip