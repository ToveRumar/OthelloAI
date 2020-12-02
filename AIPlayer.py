from Player import Player
import random
import sys
import copy
import time
class AIPlayer(Player):
    
    def __init__(self,color,controller):
       
        Player.__init__(self,color,controller)
        self.name="AI"
        self.maximizing=True
    
    def getName(self):
        return self.name
    def isMaximizing(self):
        return self.maximizing
    def setupFirstTwoTiles(self,boardSize):
        
        self.controller.placeTile([((boardSize//2)-1),((boardSize//2)-1)],self.color)
        self.controller.placeTile([(boardSize//2),(boardSize//2)],self.color)

    def myMove(self, playingField):
        validMoves=Player.returnValidMoves(self,self.color, playingField)
       
        return validMoves
        

    def calcBestMove(self,board,validMoves):
        points=-1000
        moveToMake=None
        print(str(validMoves))
        for move in validMoves:
            board=self.updateBoard(board, move, self.color)
            res=self.minimax(board,3,not self.maximizing,self.color)
            print("res"+str(res))
            if res>=points:
                
                moveToMake=move
                points=res
        return moveToMake
        

    def minimax(self, boardState, depth,maximizing, playerColor):
        if playerColor=="W":
            other="B"
        else:
            other="W"
        validMoves=Player.returnValidMoves(self,playerColor, boardState)
        if depth == 0 or not validMoves:
            points=self.calcPoints(boardState, playerColor)
            if not maximizing:
                points=-points
            #print("Calculating points for" + str(maximizing) + str(playerColor))
            return points
        else:
            childBoards = []
            for move in validMoves:
                childBoards.append(self.updateBoard(boardState, move, playerColor)) 
        if maximizing:
            maxEval = - 1000
            for board in childBoards:
                evaluation = self.minimax(board, depth - 1,False, other)
                maxEval = max(maxEval, evaluation)
                print("maxeval" + str(maxEval))
            return maxEval
        else:
            minEval = 1000
            for board in childBoards:
                evaluation = self.minimax(board, depth - 1, True, other)
                minEval = min(minEval, evaluation)
                print("minval" + str(minEval))
            return minEval
            
    def calcPoints(self, board, playerColor):
        points = 0
        for row in board:
            for tile in row:
                if tile == playerColor:
                    points = points + 1
      

        
        return points
        


    def updateBoard(self, board , move, color):
        newBoard = copy.deepcopy(board)
        tilesToFlip= move.getTilesToFlip()
        tilesToFlip.append(move.getPos())
        for tiles in tilesToFlip:
            newBoard[tiles[0]][tiles[1]]=color
        return newBoard
    
    


#minimax returns pos for move
#makemove takes matrix, runs minimax,returns posiion to gamecontroller
