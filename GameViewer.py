import pygame, sys, node

WHITE=(255,255,255)
BLACK=(0,0,0)
YELLOW=(255,255,0)
RED=(255,0,0)
GREEN=(0,255,0)
class GameViewer:
    
    def __init__(self,rows,cols,size, controller, nodeMatrix):
        self.rows=rows
        self.cols=cols
        self.size=size
        self.screen = None
        self.controller = controller
        self.nodeMatrix = nodeMatrix
        self.main()

    def main(self):           
        pygame.init()
        self.screen = pygame.display.set_mode((self.size,self.size))
        running = True
        self.draw(self.nodeMatrix)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
                    pygame.quit
                    sys.exit()
                if pygame.mouse.get_pressed()[0]:
                    pos=pygame.mouse.get_pos()
                    new_node=self.get_clicked_node(pos)
                    #new_node.activate()
                    self.controller.newMove(new_node)

                    


    def draw_grid(self):
        height=self.size//self.rows
        width=self.size//self.cols
        for i in range(self.rows):
            pygame.draw.line(self.screen,(BLACK),(0,i*height),(self.size,i*height))
            for j in range(self.cols):
                pygame.draw.line(self.screen,(BLACK),(j*width,0),(j*width,self.size))

    def draw_nodes(self):
        height=self.size//self.rows
        width=self.size//self.cols
        for i in range(self.rows):
            for j in range(self.cols):
                if (self.nodeMatrix[i][j].is_on()):
                    pygame.draw.rect(self.screen,RED,((j*width),(i*height),width,height))
                else:
                   pygame.draw.rect(self.screen,GREEN,((j*width),(i*height),width,height)) 

    def get_clicked_node(self,pos):
        height= height=self.size//self.rows
        width=self.size//self.cols
        x,y= pos
        row=y//height
        col=x//width
        return self.nodeMatrix[row][col]

    def draw(self, nodeMatrix):
        self.nodeMatrix = nodeMatrix
        self.draw_nodes()
        self.draw_grid()
        pygame.display.update()


#simulation(4,4,600)



    
       