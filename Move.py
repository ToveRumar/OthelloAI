class Move:
    def __init__ (self, pos, points, color):
        self.pos = pos
        self.points = points
        self.color = color

    def getPos(self):
        return self.pos

    def getPoints(self):
        return self.points
    
    def getColor(self):
        return self.color