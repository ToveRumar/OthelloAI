import Move
class Player:
    def __init__(self,color,controller):
       
        self.color=color

        self.controller=controller
       
    
    def makeMove(self, position):
        
        self.controller.placeTile( position, self.color)


    def getColor():
        return self.color

    
    def returnValidMoves(self, playingField):
        allValidMoves = []
        tilesToFlip=[]
        #allValidMoves = [[0 for i in range(len(playingField))] for j in range(len(playingField))]
        for i in range(len(playingField)):
            for j in range(len(playingField)):
                if playingField[i][j] == 0:
                    nw = self.isValid(self.color, -1, -1, i, j, playingField)
                    for count in range(nw):
                        tilesToFlip.append([i-count, j-count])
                    nn = self.isValid(self.color, 0, -1, i, j, playingField)
                    for count in range(nn):
                        tilesToFlip.append([i, j-count])
                    ne = self.isValid(self.color, 1, -1, i, j, playingField)
                    for count in range(ne):
                        tilesToFlip.append([i+count,j-count])
                    ee = self.isValid(self.color, 1, 0, i, j, playingField)
                    for count in range(ee):
                        tilesToFlip.append([i+count,j])
                    se = self.isValid(self.color, 1, 1, i, j, playingField)
                    for count in range(se):
                        tilesToFlip.append([i+count,j+count])
                    ss = self.isValid(self.color, 0, 1, i, j, playingField)
                    if ss:
                        for count in range(ss):
                            tilesToFlip.append([i+count,j])
                        
                    sw = self.isValid(self.color, -1, 1, i, j, playingField)
                    for count in range(nw):
                        tilesToFlip.append([i-count,j+count])
                    ww = self.isValid(self.color, -1, 0, i, j, playingField)
                    for count in range(nn):
                        tilesToFlip.append([i-count,j])
                    points = nw + nn + ne + ee + se + ss + sw + ww
                    
                    if (points > 0):
                        allValidMoves.append(Move.Move([i,j], points, self.color,tilesToFlip))
                       
        return allValidMoves


    def isValid(self, playerColor, offseti, offsetj, i, j, playingField):
        other = ""
        if(playerColor == "B"):
            other = "W"
        elif (playerColor == "W"):
            other = "B"
        else:
            print("problemo in colorino")

        if ((offseti + i < 0) or (offseti + i > len(playingField)-1) or (offsetj + j < 0) or (offsetj + j > len(playingField)-1)):
            return 0
        if (playingField [offseti + i][offsetj + j] != other):
            return 0
        elif (playingField [offseti + i][offsetj + j] == other):
            # kolla samma linje check line function
            return self.findSelfInLine(playerColor, offseti, offsetj, offseti + i, offsetj + j, playingField, other)

    def findSelfInLine(self, playerColor, offseti, offsetj, i, j, playingField, other, counter = 1):
        
        if ((offseti + i < 0) or (offseti + i > len(playingField)-1) or (offsetj + j < 0) or (offsetj + j > len(playingField)-1)):
            print("index out of bounds")
            return 0
        else:
            if (playingField [offseti + i][offsetj + j] == other):
                counter += 1
                self.findSelfInLine(playerColor, offseti, offsetj, offseti + i, offsetj + j, playingField, other, counter)
            elif (playingField [offseti + i][offsetj + j] == playerColor):
                return counter
            else:
                return 0
            return 0
        
        

