import pygame
from pygame.locals import *
from enum import Enum
from Dig import Digscreen

class DigState(Enum):
    Select = 1
    Count = 2
    Indig = 3
    postDig = 4

    

class Yatesscreen:


    def __init__(self,num):
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.xlfont = pygame.font.SysFont('Comic Sans MS', 70)
        self.state = DigState.Select
        self.buton = pygame.Rect(250,350,500,300)
        self.timerbase = 0
        self.dig = Digscreen(num,300,5)
        self.score = 0
        self.renown = 0
        self.fosName = ""
        self.fosImg = None
        self.star = pygame.image.load("menus/star.png").convert_alpha()
        self.bfont = pygame.font.SysFont('Comic Sans MS', 40)
        self.back = pygame.image.load("menus/yates.png")
 

    def draw(self,screen,keys,mX,mY,click):
            
            if self.state == DigState.Select:
                 screen.blit(self.back,(0,0))

                 pygame.draw.rect(screen, (220, 0, 0), self.buton, border_radius=15)
                 pygame.draw.rect(screen, (190, 0, 0), self.buton, border_radius=15,width=3)
                 
                 text_width, text_height = self.xlfont.size("Press To Dig")

                 screen.blit(self.xlfont.render("Press To Dig", True, (0, 0, 0)), (500-text_width/2, 505-text_height/2))
                 
                 if click:
                      if(self.buton.collidepoint(mX,mY)):
                           self.state = DigState.Count
                           self.timerbase = pygame.time.get_ticks()


            elif self.state == DigState.Count:
                 screen.blit(self.back,(0,0))
                 seconds = (pygame.time.get_ticks()-self.timerbase)/1500

                 pygame.draw.rect(screen, (220, 0, 0), self.buton, border_radius=15)
                 pygame.draw.rect(screen, (190, 0, 0), self.buton, border_radius=15,width=3)
                 
                 text_width, text_height = self.xlfont.size("Digging in")

                 screen.blit(self.xlfont.render("Digging in", True, (0, 0, 0)), (500-text_width/2, 460-text_height/2))

                 

                 if int(3-round(seconds,0)) == 0:
                      self.state = DigState.Indig
                      self.dig.resetTime()

                 text_width, text_height = self.xlfont.size(str(int(3-round(seconds,0))))

                 screen.blit(self.xlfont.render(str(int(3-round(seconds,0))), True, (0, 0, 0)), (500-text_width/2, 550-text_height/2))
            
            elif self.state == DigState.Indig:
                 out = self.dig.tick(screen,keys,mX,mY,click)

                 if out == 1:
                      
                      
                      self.state = DigState.postDig
                      self.renown, self.score, self.fosName = self.dig.getScore()
                      self.renown = int((self.score/100)*self.renown)
                      self.fosImg = pygame.image.load(self.dig.getImg())
                      self.fosImg = pygame.transform.scale(self.fosImg, (300, 300))


            elif self.state == DigState.postDig:
                 # background here
                 screen.blit(self.back,(0,0))
                 pygame.draw.rect(screen, (135, 225, 218), (150, 25, 700, 150), border_radius=15)
                 screen.blit(self.bfont.render("You Found A", True, (0, 0, 0)), (180, 40))
                 screen.blit(self.bfont.render(self.fosName+"!", True, (0, 0, 0)), (180, 100))

                 
                 screen.blit(self.fosImg, (350,200))
                 
                 if self.score>0:
                      screen.blit(self.star,(360,500))
                      if self.score>50:
                         screen.blit(self.star,(460,480))
                         if self.score>90:
                              screen.blit(self.star,(560,500))
                 

                 #screen.blit(self.font.render("Your Score: "+str(int(self.score)), True, (0, 0, 0)), (200, 500))

               
                 words = "You gain " + str(self.renown)+" Attention!"

                 pygame.draw.rect(screen, (135, 225, 218), (150, 580, 700, 150), border_radius=15)

                 text_width, text_height = self.font.size(words)

                 screen.blit(self.font.render(words, True, (0, 0, 0)), (500-(text_width/2), 600))

                 text_width, text_height = self.font.size("Press E to exit back to campus")
                 
                 screen.blit(self.font.render("Press E to exit back to campus", True, (0, 0, 0)), (500-(text_width/2), 650))

                 

                 if keys[K_e]:
                      return 2
                 

    def getRen(self):
         return self.renown