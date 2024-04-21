import pygame
from pygame.locals import *
import random

class crack:


    def __init__(self, X,Y):
        self.num = random.randint(0,4)
        xoffDict = {0:5,1:10,2:10,3:0,4:3}
        yoffDict ={0:5,1:3,2:10,3:0,4:0}
        self.x = (X*10)-xoffDict[self.num]
        self.y = (Y*10)-yoffDict[self.num]
        


        self.pos = pygame.Rect(self.x,self.y,20,20)
 

    def draw(self,screen, img):

        screen.blit(img, (self.pos.left, self.pos.top))
        
    def loc(self):
        return(self.pos.left,self.pos.top)
    
    def whatcrack(self): #hehe
        return self.num
    


    

