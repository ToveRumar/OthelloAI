import Move
class Player:
    def __init__(self,color,controller):
       
        self.color=color
        self.points=0

        self.controller=controller
       
    
    def makeMove(self, position):
        
        self.controller.placeTile( position, self.color)

    def getPoints(self):
        return self.points

    def setPoints(self,points):
        self.points=points
        
    def getColor():
        return self.color

    
    def returnValidMoves(self, color, playingField):
        allValidMoves = []
        
        #allValidMoves = [[0 for i in range(len(playingField))] for j in range(len(playingField))]
        for i in range(len(playingField)):
            for j in range(len(playingField)):
                tilesToFlip=[]
                if playingField[i][j] == 0:
                    
                    nw = self.isValid(color, -1, -1, i, j, playingField)
                    if nw:
                        for count in range(nw+ 1):
                            tilesToFlip.append([i-count, j-count])

                    nn = self.isValid(color, -1, 0, i, j, playingField)
                    if nn:
                        for count in range(nn+ 1):
                            tilesToFlip.append([i-count, j])

                    ne = self.isValid(color, -1, 1, i, j, playingField)
                    if ne:
                        for count in range(ne+ 1):
                            tilesToFlip.append([i-count,j+count])

                    ee = self.isValid(color, 0, 1, i, j, playingField)
                    if ee:
                        for count in range(ee+ 1):
                            tilesToFlip.append([i,j+count])

                    se = self.isValid(color, 1, 1, i, j, playingField)
                    if se:    
                        for count in range(se+ 1):
                            tilesToFlip.append([i+count,j+count])

                    ss = self.isValid(color, 1, 0, i, j, playingField)
                    if ss:
                        for count in range(ss + 1):
                            tilesToFlip.append([i+count,j])

                    sw = self.isValid(color, 1, -1, i, j, playingField)
                    if sw:
                        for count in range(sw+ 1):
                            tilesToFlip.append([i+count,j-count])

                    ww = self.isValid(color, 0, -1, i, j, playingField)
                    if ww:
                        for count in range(ww+ 1):
                            tilesToFlip.append([i,j-count])

                    points = nw + nn + ne + ee + se + ss + sw + ww
                    
                    if (points > 0):
                        move = Move.Move([i,j], points, color,tilesToFlip)
                        allValidMoves.append(move)          
                      
        return allValidMoves


    def isValid(self, playerColor, offseti, offsetj, i, j, playingField):
        other = ""
        if(playerColor == "B"):
            other = "W"
        elif (playerColor == "W"):
            other = "B"
        else:
            print("problemo with colorino")

        if (((offseti + i) < 0) or ((offseti + i) > (len(playingField)-1)) or ((offsetj + j) < 0) or ((offsetj + j) >(len(playingField)-1))):
            return 0
        if (playingField [offseti + i][offsetj + j] != other):
            return 0
        elif (playingField [offseti + i][offsetj + j] == other):
            # kolla samma linje check line function
            return self.findSelfInLine(playerColor, offseti, offsetj, offseti + i, offsetj + j, playingField, other, 1)

    def findSelfInLine(self, playerColor, offseti, offsetj, i, j, playingField, other, counter):        
        if (((offseti + i) < 0) or ((offseti + i )>(len(playingField)-1)) or ((offsetj + j) < 0) or ((offsetj + j) >(len(playingField)-1))):
           
            return 0
        else:
            if (playingField [offseti + i][offsetj + j] == other):
                counter += 1
                
                counter=self.findSelfInLine(playerColor, offseti, offsetj, offseti + i, offsetj + j, playingField, other, counter)
                return counter
            elif (playingField [offseti + i][offsetj + j] == playerColor):
                return counter
            else:
                return 0
        
        

