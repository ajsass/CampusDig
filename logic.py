import pygame
from pygame.locals import *
from enum import Enum
from opensc import Openscreen
from campussc import Campusscreen
from barkssc import barksscreen
from iscscreen import ISCscreen
from yatessc import Yatesscreen
from museumsc import museumscreen
from endsc import endscreen

class Screen(Enum):
    Open = 1
    Campus = 2
    Yates = 3
    ISC = 4
    Barksdale = 5
    Museum = 6
    end = 7
    

class logic:


    def __init__(self):
        self.state = Screen.Open
        
        self.current = Openscreen()
        self.renown = 0
        self.numFos = 0 # number of fossils (for saving numbers)

    def draw(self,screen,keys,mX,mY,click):
            
            if keys[K_t]:
                 self.numFos = 50 # FOR DEBUG
            
            exit = self.current.draw(screen,keys,mX,mY,click)

            if exit != None:
                 self.swap(exit)
        
    def swap(self,num):
        
        if num == 1:
             self.state = Screen.Open
             self.current = Openscreen()
        elif num == 2:
             if self.state == Screen.Barksdale or self.state == Screen.ISC or self.state == Screen.Yates:
                  self.numFos +=1
                  self.renown += self.current.getRen()
             self.state = Screen.Campus
             
             self.current = Campusscreen(self.renown)
             
        elif num == 3:
             self.state = Screen.Yates
             self.current = Yatesscreen(self.numFos)
        elif num == 4:
             self.state = Screen.ISC
             self.current = ISCscreen(self.numFos)
        elif num == 5:
             self.state = Screen.Barksdale
             self.current = barksscreen(self.numFos)
        elif num == 6:
             self.state = Screen.Museum
             self.current = museumscreen(self.renown,self.numFos)
        elif num == 7:
             self.state = Screen.end
             self.current = endscreen()
             
             
             
