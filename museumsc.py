import pygame
from pygame.locals import *

class museumscreen:


    def __init__(self,renown,fosNum):
        self.font = pygame.font.SysFont('Comic Sans MS', 40)
        self.smfont = pygame.font.SysFont('Comic Sans MS', 30)
        
        self.renown = str(renown)
        self.numFos = fosNum

        self.fosList = []
        self.fosRects = []
        self.Ret = pygame.Rect(350,620,300,70)
        self.back = pygame.image.load("menus/musback.png")

        #set up images & rects
        for i in range (fosNum):
            if i >= 50:
                break
            name = "fossil"+str(i)+".png"
            fosX = i%10
            foxY = i%5
            temp=pygame.image.load(name)
            temp = pygame.transform.scale(temp, (100, 100))
            self.fosList.append(temp) 
            rec = pygame.Rect((100*i)-(1000* int(i/10)),100+(int(i/10)*100),100,100)
            self.fosRects.append(rec)
        
            


        
 

    def draw(self,screen,keys,mX,mY,click):
        screen.blit(self.back,(0,0))

        tx = "Total Attention: "+self.renown
        text_width, text_height = self.smfont.size(tx)
        screen.blit(self.font.render(tx, True, (0, 0, 0)), (500-(text_width/2)-40, 0))
        
        for i in range(self.numFos):
            
            screen.blit(self.fosList[i],(self.fosRects[i].left,self.fosRects[i].top))
        


        pygame.draw.rect(screen, (249, 183, 17),self.Ret, border_radius=15)
        pygame.draw.rect(screen, (0, 0, 0), self.Ret, border_radius=15,width=3)
        text_width, text_height = self.smfont.size("Return to Campus")
        screen.blit(self.smfont.render("Return to Campus", True, (0, 0, 0)), (500-text_width/2, 630))

        if click:
            if(self.Ret.collidepoint(mX,mY)):
                return 2
       
