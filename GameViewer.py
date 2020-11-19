import pygame, sys, tile

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
        

    def main(self):           
        pygame.init()
        self.screen = pygame.display.set_mode((740,self.size))
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.draw(self.tileMatrix)
      

                    
    def run(self):
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
                        new_tile=self.get_clicked_tile(pos)
                        self.controller.newMove(new_tile)



    def draw_grid(self):
        height=self.size//self.rows
        width=self.size//self.cols
        for i in range(self.rows):
            pygame.draw.line(self.screen,(BLACK),(0,i*height),(self.size,i*height))
            for j in range(self.cols):
                pygame.draw.line(self.screen,(BLACK),(j*width,0),(j*width,self.size))

    def draw_tiles(self):
        height=self.size//self.rows
        width=self.size//self.cols
        for i in range(self.rows):
            for j in range(self.cols):
                pygame.draw.rect(self.screen,self.tileMatrix[i][j].get_tile_color(),((j*width),(i*height),width,height))
            pygame.draw.rect(self.screen,GREY,((4*width),(i*height),width,height))

    def draw_text(self):
        
        text = self.font.render('Human', True, BLACK) 
        textRect = text.get_rect()  
        textRect.center = (680, 20)
        self.screen.blit(text, textRect) 

    def get_clicked_tile(self,pos):
        height= height=self.size//self.rows
        width=self.size//self.cols
        x,y= pos
        row=y//height
        col=x//width
        return self.tileMatrix[row][col]

    def draw(self, tileMatrix):
        self.tileMatrix = tileMatrix
        self.draw_tiles()
        self.draw_grid()
        self.draw_text()
        pygame.display.update()



    
       