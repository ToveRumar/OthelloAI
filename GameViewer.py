import pygame, sys, tile,time,os
from threading import Thread

WHITE=(255,255,255)
BLACK=(0,0,0)
YELLOW=(255,255,0)
RED=(255,0,0)
GREEN=(0,255,0)
GREY=(128,128,128)
class GameViewer:
    
    def __init__(self,rows,cols,size, controller, tileMatrix):
        self.rows=rows
        self.cols=cols
        self.size=size
        self.screen = None
        self.controller = controller
        self.tileMatrix = tileMatrix
        workingDir = os.path.dirname(__file__)
        self.fontFile = os.path.join(workingDir, 'INVASION2000.ttf')

    def setup(self):           
        pygame.init()
        #print(pygame.font.get_fonts())
        
        self.screen = pygame.display.set_mode((740,self.size))

        self.font = pygame.font.Font(self.fontFile, 32)
        #self.draw(self.tileMatrix,0,0)
        
                    
    def run(self):
        pos=[]
        done = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
                    pygame.quit
                    sys.exit()
                if pygame.mouse.get_pressed()[0]:
                    pos=pygame.mouse.get_pos()
                    if pos[0]>self.size:
                        pass
                    else:
                        done = True
                        break
            if done:
                break                
        return self.get_clicked_tile(pos)



    def draw_grid(self):
        height=self.size//self.rows
        width=self.size//self.cols
        for i in range(self.rows):
            pygame.draw.line(self.screen,(BLACK),(0,i*height),(self.size,i*height))
            for j in range(self.cols):
                pygame.draw.line(self.screen,(BLACK),(j*width,0),(j*width,self.size))

    def draw_tiles(self):
        self.screen.fill(GREY)
        height=self.size//self.rows
        width=self.size//self.cols
        for i in range(self.rows):
            for j in range(self.cols):
                if self.tileMatrix[i][j] == "W":
                    pygame.draw.rect(self.screen,WHITE,((j*width),(i*height),width,height))
                elif self.tileMatrix[i][j] == "B":
                    pygame.draw.rect(self.screen,BLACK,((j*width),(i*height),width,height))
                else:
                    pygame.draw.rect(self.screen,GREEN,((j*width),(i*height),width,height))
            #pygame.draw.rect(self.screen,GREY,((8*width),(i*height),width,height))
            

    def draw_text(self,whitePlayerName, blackPlayerName,whitePlayerPoints,blackPlayerPoints):
        
        text = self.font.render(blackPlayerName, True, BLACK) 
        textRect = text.get_rect()  
        textRect.center = (675, 20)
        self.screen.blit(text, textRect) 
        text = self.font.render(str(blackPlayerPoints), True, BLACK) 
        textRect = text.get_rect()  
        textRect.center = (675,60)
        self.screen.blit(text, textRect) 
        text = self.font.render(whitePlayerName, True, WHITE) 
        textRect = text.get_rect()  
        textRect.center = (675,200)
        self.screen.blit(text, textRect) 
        text = self.font.render(str(whitePlayerPoints), True, WHITE) 
        textRect = text.get_rect()  
        textRect.center = (675,260)
        self.screen.blit(text, textRect) 

    def get_clicked_tile(self,pos):
        height= height=self.size//self.rows
        width=self.size//self.cols
        x,y= pos
        row=y//height
        col=x//width
        return [row,col]

    def draw(self, tileMatrix,whitePlayerName,blackPlayerName, whitePlayerPoints,blackPlayerPoints):
        self.tileMatrix = tileMatrix
        self.draw_tiles()
        self.draw_grid()
        self.draw_text(whitePlayerName,blackPlayerName,whitePlayerPoints,blackPlayerPoints)
        pygame.display.update()

    def showPossibleMoves(self, posMoves):
        height=self.size//self.rows
        width=self.size//self.cols
        for move in posMoves:
            points=str(move.getPoints())
            
            text = self.font.render(points, True, BLACK) 
            textRect = text.get_rect()  
            textRect.center = ((width*move.getPos()[1])+(width/2), (height*move.getPos()[0])+(height/2))
            self.screen.blit(text, textRect)
        pygame.display.update()


    def drawGameOver(self):
        font = pygame.font.Font(self.fontFile,80)
        text =font.render("Game Over!", True, RED) 
        textRect = text.get_rect()  
        textRect.center = (300, 250)
        self.screen.blit(text, textRect)
        font = pygame.font.Font(self.fontFile,30)
        text =font.render("(click anywhere to start over)", True, RED) 
        textRect = text.get_rect()  
        textRect.center = (300, 320)
        self.screen.blit(text, textRect)
        pygame.display.update()
        self.waitForInput()
        self.controller.NewGame()
        
    
    def startScreen(self):
        pygame.draw.rect(self.screen,BLACK, (0,0, 380,600))
        pygame.draw.rect(self.screen,WHITE, (380,0, 380,600))
        font = pygame.font.Font(self.fontFile,60)
        text = font.render("WELCOME TO", True, RED) 
        textRect = text.get_rect()  
        textRect.center = (380, 250)
        self.screen.blit(text, textRect)
        text = font.render("OTHELLO", True, RED) 
        textRect = text.get_rect()  
        textRect.center = (380, 320)
        self.screen.blit(text, textRect)
        pygame.display.update()
        pos=self.waitForInput()
        pygame.draw.rect(self.screen,BLACK, (0,0, 380,600))
        pygame.draw.rect(self.screen,WHITE, (380,0, 380,600))
        font = pygame.font.Font(self.fontFile,60)
        text = font.render("Pick a Color", True, RED) 
        textRect = text.get_rect()  
        textRect.center = (380, 250)
        self.screen.blit(text, textRect) 
        font = pygame.font.Font(self.fontFile, 30)
        text = font.render("(Black begins)", True, RED) 
        textRect = text.get_rect()  
        textRect.center = (380, 320)
        self.screen.blit(text, textRect) 
        pygame.display.update()
        pos=self.waitForInput()
        if pos[0]<380:
            return "B"
        else:
            return "W"

    def waitForInput(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
                    pygame.quit
                    sys.exit()
                if pygame.mouse.get_pressed()[0]:
                    pos=pygame.mouse.get_pos()
                    if pos[0]>self.size:
                        pass
                    else:
                        return pos