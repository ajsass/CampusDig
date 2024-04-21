import pygame
from pygame.locals import *

class Openscreen:


    def __init__(self):
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.scrn = 1
        self.s1 = (pygame.image.load("intro/1.png"))
        self.s2 = (pygame.image.load("intro/2.png"))
        self.s3 = (pygame.image.load("intro/3.png"))
        self.s4 = (pygame.image.load("intro/4.png"))
        self.s5 = (pygame.image.load("intro/5.png"))
        self.s6 = (pygame.image.load("intro/6.png"))
        self.s7 = (pygame.image.load("intro/7.png"))
        self.s8 = (pygame.image.load("intro/8.png"))
        self.on = False
 

    def draw(self,screen,keys,mX,mY,click):
            
            #screen.blit(self.font.render("Open Screen, press F to move to next", True, (0, 0, 0)), (450, 100))

            if keys[K_SPACE] and not self.on:
                 self.on = True
                 self.scrn +=1
                 if self.scrn == 9:
                      return 2
            if not keys[K_SPACE]:
                 self.on = False

            


            if(self.scrn==1):
                 screen.blit(self.s1,(0,0))
            elif(self.scrn==2):
                 screen.blit(self.s2,(0,0))
            elif(self.scrn==3):
                 screen.blit(self.s3,(0,0))
            elif(self.scrn==4):
                 screen.blit(self.s4,(0,0))
            elif(self.scrn==5):
                 screen.blit(self.s5,(0,0))
            elif(self.scrn==6):
                 screen.blit(self.s6,(0,0))
            elif(self.scrn==7):
                 screen.blit(self.s7,(0,0))
            elif(self.scrn==8):
                 screen.blit(self.s8,(0,0))


    def getRen(self):
         return 0
    