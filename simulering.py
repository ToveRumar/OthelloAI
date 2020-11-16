import pygame, sys, numpy as np, node

WHITE=(255,255,255)
BLACK=(0,0,0)
YELLOW=(255,255,0)
RED=(255,0,0)
GREEN=(0,255,0)
class simulation:
    
    def __init__(self,rows,cols,size):
        self.rows=rows
        self.cols=cols
        self.size=size
        self.main()

    def main(self):

        node_matrix = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(node.node())
            node_matrix.append(row)
            
        pygame.init()
        screen = pygame.display.set_mode((self.size,self.size))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
                    pygame.quit
                    sys.exit()
                screen.fill(YELLOW)
                self.draw_nodes(screen,node_matrix)
                self.draw_grid(screen)
                pygame.display.update()
                if pygame.mouse.get_pressed()[0]:
                    pos=pygame.mouse.get_pos()
                    new_node=self.get_clicked_node(pos,node_matrix)
                    new_node.activate()
                    


    def draw_grid(self,screen):
        height=self.size//self.rows
        width=self.size//self.cols
        for i in range(self.rows):
            pygame.draw.line(screen,(BLACK),(0,i*height),(self.size,i*height))
            for j in range(self.cols):
                pygame.draw.line(screen,(BLACK),(j*width,0),(j*width,self.size))

    def draw_nodes(self,screen,node_matrix):
        height=self.size//self.rows
        width=self.size//self.cols
        for i in range(self.rows):
            for j in range(self.cols):
                if (node_matrix[i][j].is_on()):
                    pygame.draw.rect(screen,GREEN,((j*width),(i*height),width,height))
                else:
                   pygame.draw.rect(screen,RED,((j*width),(i*height),width,height)) 

    def get_clicked_node(self,pos,node_matrix):
        height= height=self.size//self.rows
        width=self.size//self.cols
        x,y= pos
        row=y//height
        col=x//width
        return node_matrix[row][col]

simulation(4,4,600)



    
       