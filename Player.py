import Move
class Player:
    def __init__(self,color,controller):
       
        self.color=color

        self.controller=controller
       
    
    def makeMove(self, position):
        print("placing tile")
        self.controller.placeTile( position, self.color)


    def getColor():
        return self.color

    
    def returnValidMoves(self, playingField):
        allValidMoves = []
        #allValidMoves = [[0 for i in range(len(playingField))] for j in range(len(playingField))]
        for i in range(len(playingField)):
            for j in range(len(playingField)):
                if playingField[i][j] == 0:
                    nw = self.isValid(self.color, -1, -1, i, j, playingField)
                    
                    nn = self.isValid(self.color, 0, -1, i, j, playingField)
                    
                    ne = self.isValid(self.color, 1, -1, i, j, playingField)
                    
                    ee = self.isValid(self.color, 1, 0, i, j, playingField)
                    
                    se = self.isValid(self.color, 1, 1, i, j, playingField)
                    
                    ss = self.isValid(self.color, 0, 1, i, j, playingField)
                    
                    sw = self.isValid(self.color, -1, 1, i, j, playingField)
                    
                    ww = self.isValid(self.color, -1, 0, i, j, playingField)
                    
                    points = nw + nn + ne + ee + se + ss + sw + ww
                    print(points)
                    if (points > 0):
                        allValidMoves.append(Move.Move([i,j], points, self.color))
                        #allValidMoves[i][j] = self.color
                        for val in allValidMoves:
                            print(val.points) 
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
        print("in function")
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
        
        

