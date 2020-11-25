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

    def incPoints(self,points):
        self.points=self.points+points
        
    def getColor():
        return self.color

    
    def returnValidMoves(self, playingField):
        allValidMoves = []
        
        #allValidMoves = [[0 for i in range(len(playingField))] for j in range(len(playingField))]
        for i in range(len(playingField)):
            for j in range(len(playingField)):
                tilesToFlip=[]
                if playingField[i][j] == 0:
                    
                    nw = self.isValid(self.color, -1, -1, i, j, playingField)
                    if nw:
                        for count in range(nw+ 1):
                            tilesToFlip.append([i-count, j-count])

                    nn = self.isValid(self.color, -1, 0, i, j, playingField)
                    if nn:
                        for count in range(nn+ 1):
                            tilesToFlip.append([i-count, j])

                    ne = self.isValid(self.color, -1, 1, i, j, playingField)
                    if ne:
                        for count in range(ne+ 1):
                            tilesToFlip.append([i-count,j+count])

                    ee = self.isValid(self.color, 0, 1, i, j, playingField)
                    if ee:
                        for count in range(ee+ 1):
                            tilesToFlip.append([i,j+count])

                    se = self.isValid(self.color, 1, 1, i, j, playingField)
                    if se:    
                        for count in range(se+ 1):
                            tilesToFlip.append([i+count,j+count])

                    ss = self.isValid(self.color, 1, 0, i, j, playingField)
                    if ss:
                        for count in range(ss + 1):
                            tilesToFlip.append([i+count,j])

                    sw = self.isValid(self.color, 1, -1, i, j, playingField)
                    if sw:
                        for count in range(sw+ 1):
                            tilesToFlip.append([i+count,j-count])

                    ww = self.isValid(self.color, 0, -1, i, j, playingField)
                    if ww:
                        for count in range(ww+ 1):
                            tilesToFlip.append([i,j-count])

                    points = nw + nn + ne + ee + se + ss + sw + ww
                    
                    if (points > 0):
                        move = Move.Move([i,j], points, self.color,tilesToFlip)
                        allValidMoves.append(move)
                        print("move to make: "+str(move.getPos())+"tiles to flip for this move is"+ str(move.getTilesToFlip()))
                       # print(str(nw) + "<< nw "+ str(nn) + "<< nn " + str(ne) + "<< ne " + str(ee) + "<< ee " + str(se) + "<< se " + str(ss) + "<< ss " + str(sw) + "<< sw " + str(ww) +"<< ww ")
        return allValidMoves


    def isValid(self, playerColor, offseti, offsetj, i, j, playingField):
        other = ""
        if(playerColor == "B"):
            other = "W"
        elif (playerColor == "W"):
            other = "B"
        else:
            print("problemo in colorino")

        if (((offseti + i) < 0) or ((offseti + i) > (len(playingField)-1)) or ((offsetj + j) < 0) or ((offsetj + j) >(len(playingField)-1))):
            return 0
        if (playingField [offseti + i][offsetj + j] != other):
            return 0
        elif (playingField [offseti + i][offsetj + j] == other):
            # kolla samma linje check line function
            return self.findSelfInLine(playerColor, offseti, offsetj, offseti + i, offsetj + j, playingField, other, 1)

    def findSelfInLine(self, playerColor, offseti, offsetj, i, j, playingField, other, counter):        
        if (((offseti + i) < 0) or ((offseti + i )>(len(playingField)-1)) or ((offsetj + j) < 0) or ((offsetj + j) >(len(playingField)-1))):
            print("index out of bounds")
            return 0
        else:
            if (playingField [offseti + i][offsetj + j] == other):
                counter += 1
                print(str(counter) + "added one to counter")
                counter=self.findSelfInLine(playerColor, offseti, offsetj, offseti + i, offsetj + j, playingField, other, counter)
                return counter
            elif (playingField [offseti + i][offsetj + j] == playerColor):
                return counter
            else:
                return 0
        
        

