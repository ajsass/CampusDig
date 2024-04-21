import pygame
from pygame.locals import *

class rock:


    def __init__(self, X,Y):
        self.x = X*10
        self.y = Y*10
        self.dug = False
        self.opac = 6
        self.pos = pygame.Rect(X*10,Y*10,10,10)
        

    def draw(self,screen, img):

        screen.blit(img, (self.pos.left, self.pos.top))
        if self.dug:
            if self.opac !=0:
                
                
                
                self.opac = self.opac-1
            
    def isDug(self):
        return self.dug
    def getOP(self):
        return self.opac

    def remove(self):
        self.dug = True

    def isRock(self):
        return True
    
    def loc(self):
        return(self.pos.left, self.pos.top)
