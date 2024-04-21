import pygame
from pygame.locals import *

class endscreen:


    def __init__(self):
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.scrn = 1
        self.s1 = (pygame.image.load("outro/1.png"))
        self.s2 = (pygame.image.load("outro/2.png"))
        self.s3 = (pygame.image.load("outro/3.png"))
        self.s4 = (pygame.image.load("outro/4.png"))
      
        self.on = False
 

    def draw(self,screen,keys,mX,mY,click):
            
            #screen.blit(self.font.render("Open Screen, press F to move to next", True, (0, 0, 0)), (450, 100))

            if keys[K_SPACE] and not self.on:
                 self.on = True
                 if self.scrn != 4:
                    self.scrn +=1
                 
            if not keys[K_SPACE]:
                 self.on = False

            if keys[K_q]:
                 if self.scrn == 4:
                      pygame.quit()
                      exit()



            if(self.scrn==1):
                 screen.blit(self.s1,(0,0))
            elif(self.scrn==2):
                 screen.blit(self.s2,(0,0))
            elif(self.scrn==3):
                 screen.blit(self.s3,(0,0))
            elif(self.scrn==4):
                 screen.blit(self.s4,(0,0))
          

    def getRen(self):
         return 0
    