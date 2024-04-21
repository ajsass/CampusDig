import pygame
from pygame.locals import *
from dirt import dirt
from enum import Enum
from rock import rock
from crack import crack
import random
from PIL import Image
from genFossil import genFossil

class TOOL(Enum):
    Brush = 1
    Shovel = 2
    Pick = 3

class Digscreen:


    def __init__(self, num, renown, tier):
        self.layer = []
        for x in range(70):
            row  = []
            for y in range(70):
                rockper = random.randint(0, tier)
                if rockper == 5:
                    row.append((rock(x,y)))
                else:
                    row.append(dirt(x,y))
            self.layer.append(row)
        self.dbase = pygame.image.load("terrain/dirtbase.png")
        self.d1= pygame.image.load("terrain/dirt1.png")
        self.d2 = pygame.image.load("terrain/dirt2.png")
        self.d3 = pygame.image.load("terrain/dirt3.png")
        self.d4 = pygame.image.load("terrain/dirt4.png")
        self.d5 = pygame.image.load("terrain/dirt5.png")

        self.rbase = pygame.image.load("terrain/rock.png")
        self.r1= pygame.image.load("terrain/rock1.png")
        self.r2 = pygame.image.load("terrain/rock2.png")
        self.r3 = pygame.image.load("terrain/rock3.png")
        self.r4 = pygame.image.load("terrain/rock4.png")
        self.r5 = pygame.image.load("terrain/rock5.png")

        self.c0= pygame.image.load("cracks/c0.png").convert_alpha()
        self.c1= pygame.image.load("cracks/c1.png").convert_alpha()
        self.c2= pygame.image.load("cracks/c2.png").convert_alpha()
        self.c3= pygame.image.load("cracks/c3.png").convert_alpha()
        self.c4= pygame.image.load("cracks/c4.png").convert_alpha()

        #large versions for side
        br = pygame.image.load("tools/brush.png").convert_alpha()
        sh = pygame.image.load("tools/shovel.png").convert_alpha()
        pk = pygame.image.load("tools/pickaxe.png").convert_alpha()

        

        #mini for mouse
        self.Mousebr = pygame.transform.scale(br, (30, 30))
        self.Mousesh = pygame.transform.scale(sh, (30, 30))
        self.Mousepk = pygame.transform.scale(pk, (30, 30))

        self.menu = pygame.image.load("menus/Digmenu.png")

        im , name = genFossil()
        
        im.save("fos.png")
        self.fosName = name

        self.fossil=pygame.image.load("fos.png")
        self.fossil = pygame.transform.scale(self.fossil, (700, 700))
        self.fossilLoc = pygame.Rect(0,0,700,700)
        self.tool = TOOL.Brush
        self.cracks = []

        self.bkgnd = pygame.image.load("terrain/backg.png")
        self.start_time = pygame.time.get_ticks()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

        self.fossilnum = num


        self.score = 0
        self.renown = renown


    def tick(self,screen,keys,mX,mY,click):
        seconds = (pygame.time.get_ticks()-self.start_time)/1000
        remain = round(30-seconds,0)
        if remain <=0:
            self.export()
            return (1)

        if keys[K_a]:
            self.tool = TOOL.Brush
        if keys[K_s]:
            self.tool = TOOL.Shovel
        if keys[K_d]:
            self.tool = TOOL.Pick

        if keys[K_l]:
            self.export()

        #digging logic

        if(click):
            if mX <= 700:
                if mY <= 700:
                    
                    if(self.tool == TOOL.Brush):
                        self.brush(int(mX/10),int(mY/10))
                    if(self.tool == TOOL.Shovel):
                        self.shovel(int(mX/10),int(mY/10))
                    if(self.tool == TOOL.Pick):
                        self.pick(int(mX/10),int(mY/10))
    




        # draw
        
        screen.blit(self.bkgnd, (0, 0))

        screen.blit(self.fossil, (0, 0))

        for row in self.layer:
            for spot in row:
                if (spot.getOP()!=0):
                    if(not spot.isRock()):
                        num = spot.getOP()
                        if num == 6:
                            spot.draw(screen,self.dbase)
                        elif num == 5:
                            spot.draw(screen,self.d1)
                        elif num == 4:
                            spot.draw(screen,self.d2)
                        elif num == 3:
                            spot.draw(screen,self.d3)
                        elif num == 2:
                            spot.draw(screen,self.d4)
                        elif num == 1:
                            spot.draw(screen,self.d5)

                    

        for row in self.layer:
            for spot in row:
                if (spot.getOP()!=0):
                    if(spot.isRock()):
                        num = spot.getOP()
                        if num == 6:
                            spot.draw(screen,self.rbase)
                        elif num == 5:
                            spot.draw(screen,self.r1)
                        elif num == 4:
                            spot.draw(screen,self.r2)
                        elif num == 3:
                            spot.draw(screen,self.r3)
                        elif num == 2:
                            spot.draw(screen,self.r4)
                        elif num == 1:
                            spot.draw(screen,self.r5)


        
        for c in self.cracks:
            num = c.whatcrack()
            if num == 0:
                c.draw(screen,self.c0)
            elif num == 1:
                c.draw(screen,self.c1)
            elif num == 2:
                c.draw(screen,self.c2)
            elif num == 3:
                c.draw(screen,self.c3)
            elif num == 4:
                c.draw(screen,self.c4)

        screen.blit(self.menu,(700,0))

        if(self.tool == TOOL.Brush):
            screen.blit(self.Mousebr, (mX, mY-30))
            pygame.draw.rect(screen, (255, 0, 0), (760, 5, 180, 180), 3)  # width = 3
        elif(self.tool == TOOL.Shovel):
            screen.blit(self.Mousesh, (mX, mY-30))
            pygame.draw.rect(screen, (255, 0, 0), (760, 182, 180, 180), 3)  # width = 3
        elif(self.tool == TOOL.Pick):
            screen.blit(self.Mousepk, (mX, mY-30))
            pygame.draw.rect(screen, (255, 0, 0), (760, 355, 180, 180), 3)  # width = 3

        text = str(int(remain))
        screen.blit(self.font.render("Time Remaining", True, (0, 0, 0)), (750, 600))
        screen.blit(self.font.render(text, True, (255, 0, 0)), (750, 630))


        
            


            
            


    def brush(self,x,y):
        for remX in range(x-2,x+2):
            for remY in range(y-2,y+2):
                if(remX >=0 and remX<=69):
                    if (remY >=0 and remY<=69):
                        if(not self.layer[int(remX)][int(remY)].isRock()):
                            self.layer[int(remX)][int(remY)].remove()

    def shovel(self,x,y):
        if(self.layer[x][y].isDug()):
            self.cracks.append(crack(x,y))

        for remX in range(x-6,x+6):
            for remY in range(y-6,y+6):
                if(remX >=0 and remX<=69):
                    if (remY >=0 and remY<=69):
                        if(not self.layer[int(remX)][int(remY)].isRock()):
                            self.layer[int(remX)][int(remY)].remove()


    def pick(self,x,y):
        if(self.layer[x][y].isDug()):
            self.cracks.append(crack(x,y))
        for remX in range(x-4,x+4):
            for remY in range(y-4,y+4):
                if(remX >=0 and remX<=69):
                    if (remY >=0 and remY<=69):
                        self.layer[int(remX)][int(remY)].remove()



    def export(self):
        base_image = Image.open("terrain/backg.png")
        nw_image= Image.open("terrain/backg.png")
        fs_image = Image.open("fos.png")
        c0 = Image.open("cracks/c0.png")
        c1 = Image.open("cracks/c1.png")
        c2 = Image.open("cracks/c2.png")
        c3 = Image.open("cracks/c3.png")
        c4 = Image.open("cracks/c4.png")
        rock_img = Image.open("terrain/rock.png")
        dirt_img = Image.open("terrain/dirtbase.png")

        base_image.paste(fs_image,(0,0),fs_image)
        nw_image.paste(fs_image,(0,0),fs_image)

        for row in self.layer:
            for spot in row:
                if (spot.getOP()!=0):
                    if not spot.isRock():
                        base_image.paste(dirt_img,spot.loc(),dirt_img)

        for row in self.layer:
            for spot in row:
                if (spot.getOP()!=0):
                    if spot.isRock():
                        base_image.paste(rock_img,spot.loc(),rock_img)

        for c in self.cracks:
            num = c.whatcrack()
            if num == 0:
                base_image.paste(c0,c.loc(),c0)
            elif num == 1:
                base_image.paste(c1,c.loc(),c1)
            elif num == 2:
                base_image.paste(c2,c.loc(),c2)
            elif num == 3:
                base_image.paste(c3,c.loc(),c3)
            elif num == 4:
                base_image.paste(c4,c.loc(),c4)




            

        
                

        name = "fossil"+str(self.fossilnum)+".png"
        base_image.save(name)

        # Get the pixel data
        pixels1 = base_image.load()
        pixels2 = nw_image.load()

    # Count different pixels
        different_pixels = 0
        width, height = base_image.size
        for x in range(width):
            for y in range(height):
                if pixels1[x, y] != pixels2[x, y]:
                    different_pixels += 1

       

        self.score = (round(different_pixels/(width*height),2)*100)

        

    def getScore(self):
        if self.fosName == "Clawdius":
            self.renown *= 2
        return self.renown, 100 - self.score, self.fosName
    
    def resetTime(self):
        self.start_time = pygame.time.get_ticks()

    def getImg(self):
        return "fossil"+str(self.fossilnum)+".png"