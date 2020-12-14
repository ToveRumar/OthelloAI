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
        self.searchDepth=3
    
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
        self.counter=0
        points=-1000
        moveToMake=None
        startTime=time.perf_counter()
        for move in validMoves:
            newboard=self.updateBoard(board, move, self.color)
          
            res=self.minimax(newboard,self.searchDepth,self.maximizing,self.color,-1000,1000,)
           
            if res>=points:
                moveToMake=move
                points=res
        totalTime=time.perf_counter()-startTime
       # print(totalTime)
        print("Number of nodes evaluated; "+str(self.counter)+ " search depth is: " + str(self.searchDepth))
        
        return moveToMake
        

    def minimax(self, boardState, depth,maximizing, playerColor,alpha,beta):

        if playerColor=="W":
            other="B"
        else:
            other="W"
        validMoves=Player.returnValidMoves(self,playerColor, boardState)
        if (depth == 0) or (not validMoves):
            points=self.calcPoints(boardState, playerColor)
            
           
            if not maximizing:
                points=-points
           
            return points
            
        else:
            childBoards = []
            for move in validMoves:
               
                childBoards.append(self.updateBoard(boardState, move, playerColor)) 
            if maximizing:
                maxEval = - 1000
                for board in childBoards:
                    evaluation = self.minimax(board, depth - 1,False, other,alpha,beta)
                    
                    maxEval = max(maxEval, evaluation)
                    alpha=max(alpha,evaluation)
                    if beta<=alpha:
                        #print("Pruning")
                        break
                return maxEval
            else:
                minEval = 1000
                for board in childBoards:
                    evaluation = self.minimax(board, depth - 1, True, other,alpha,beta)   
                    minEval = min(minEval, evaluation)
                    beta=min(beta,evaluation)
                    if beta<=alpha:
                        #print("Pruning")
                        break
                return minEval
            
    def calcPoints(self, board, playerColor):
        points = 0
        for row in board:
            for tile in row:
                if tile == playerColor:
                    points += 1
                    
        return points
        


    def updateBoard(self, board , move, color):
        newBoard = copy.deepcopy(board)
        tilesToFlip= move.getTilesToFlip()
        self.counter+=1
        for tiles in tilesToFlip:
            newBoard[tiles[0]][tiles[1]]=color

        
        return newBoard
    
    


#minimax returns pos for move
#makemove takes matrix, runs minimax,returns posiion to gamecontroller
