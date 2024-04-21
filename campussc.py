import pygame
from pygame.locals import *

class Campusscreen:


    def __init__(self,renown):
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.smlfont = pygame.font.SysFont('Comic Sans MS', 15)
        self.renown = renown
        self.ISC = pygame.Rect(320,345,80,120)
        self.Bark = pygame.Rect(395,440,100,100)
        self.Yates = pygame.Rect(140,135,200,200)
        self.Mus = pygame.Rect(385,205,100,70)
        self.count = 120
        self.show = False # show err mesage for low renown
        self.map = pygame.image.load("menus/map.png")
        self.sad = pygame.image.load("menus/sadMark.png")
        self.sad = pygame.transform.scale(self.sad, (250, 230))
        self.End = pygame.Rect(750, 330, 250, 100)
        
 

    def draw(self,screen,keys,mX,mY,click):
            
            screen.blit(self.map,(0,0))
            
            if keys[K_b]:
                 self.renown = 1000 # FOR DEBUG
                 
            
            #screen.blit(self.font.render("Campus Screen move to next by clicking one", True, (0, 0, 0)), (200, 100))

            if self.show:
                 pygame.draw.rect(screen, (255, 225, 255), (20, 470, 180, 220), border_radius=15)
                 pygame.draw.rect(screen, (255, 0, 0), (20, 470, 180, 220), border_radius=15,width=3)
                 text_width, text_height = self.font.size("You need")
                 screen.blit(self.font.render("You need", True, (0, 0, 0)), (90-(text_width/2)+20, 480))
                 text_width, text_height = self.font.size("more")
                 screen.blit(self.font.render("more", True, (0, 0, 0)), (90-(text_width/2)+20, 515))
                 text_width, text_height = self.font.size("Attention")
                 screen.blit(self.font.render("Attention", True, (0, 0, 0)), (90-(text_width/2)+20, 550))
                 text_width, text_height = self.font.size("to dig")
                 screen.blit(self.font.render("to dig", True, (0, 0, 0)), (90-(text_width/2)+20, 585))
                 text_width, text_height = self.font.size("there")
                 screen.blit(self.font.render("there", True, (0, 0, 0)), (90-(text_width/2)+20, 620))

                 self.count -=1
            if self.count == 0:
                 self.show = False
                 self.count = 120

            pygame.draw.rect(screen, (135, 225, 218), (634, 30, 350, 100), border_radius=15)
            pygame.draw.rect(screen, (0, 0, 0), (634, 30, 350, 100), border_radius=15,width=3)

            pygame.draw.rect(screen, (135, 225, 218), (520, 510, 460, 180), border_radius=15)
            pygame.draw.rect(screen, (0, 0, 0), (520, 510, 460, 180), border_radius=15,width=3)

            text_width, text_height = self.font.size("Attention Progress")

            screen.blit(self.font.render("Attention Progress", True, (0, 0, 0)), (809-(text_width/2), 35))

            text_width, text_height = self.font.size(str(self.renown)+"/1000")

            screen.blit(self.font.render(str(self.renown)+"/1000", True, (0, 0, 0)), (809-(text_width/2), 75))

            text_width, text_height = self.font.size("Dig Sites")
            screen.blit(self.font.render("Dig Sites", True, (0, 0, 0)), (750-(text_width/2), 515))

            screen.blit(self.font.render("Barksdale Field", True, (0, 100, 0)), (750-(text_width/2)-140, 550))
            screen.blit(self.font.render("Isc 4", True, (200, 200, 0)), (750-(text_width/2)-140, 590))
            screen.blit(self.font.render("Yates", True, (255, 0, 0)), (750-(text_width/2)-140, 630))

            screen.blit(self.font.render("Attention Needed: 200", True, (0, 0, 0)), (750-(text_width/2)-40, 590))
            screen.blit(self.font.render("Attention Needed: 500", True, (0, 0, 0)), (750-(text_width/2)-40, 630))

            tx = "click to dig"
            screen.blit(self.smlfont.render(tx, True, (0, 0, 0)), (200, 200))
            screen.blit(self.smlfont.render(tx, True, (0, 0, 0)), (325, 397))
            screen.blit(self.smlfont.render(tx, True, (0, 0, 0)), (400, 470))

            if(self.renown >= 1000):
               pygame.draw.rect(screen, (135, 225, 218), self.End, border_radius=15)
               pygame.draw.rect(screen, (0, 0, 0), self.End, border_radius=15,width=3)
              
               screen.blit(self.font.render("Speak to", True, (0, 0, 0)), (795, 340))
               screen.blit(self.font.render("President Rowe", True, (0, 0, 0)), (765, 375))
            

            screen.blit(self.sad,(308,-25))





            #pygame.draw.rect(screen, (255, 0, 0), self.ISC,5)
            #pygame.draw.rect(screen, (0, 255, 0), self.Bark,5)
            #pygame.draw.rect(screen, (0, 0, 255), self.Yates,5)
            #pygame.draw.rect(screen, (255, 0, 255), self.Mus,5)



            if click:
                if(self.Mus.collidepoint(mX,mY)):
                    return 6
                
                elif(self.Bark.collidepoint(mX,mY)):
                    return 5
                    
                elif(self.ISC.collidepoint(mX,mY)):
                    if self.renown < 200:
                         self.show = True
                    else:
                         return 4
                    

                elif(self.Yates.collidepoint(mX,mY)):
                    if self.renown < 500:
                         self.show = True
                    else:
                         return 3
                elif(self.renown>=1000):
                     if (self.End.collidepoint(mX,mY)):
                          return 7
                    
                


            
    