import random
from PIL import Image


def genFossil():
    bodies = ["-Rex","Squirrel","itops","Griffin"]
    heads = ["tyrannosaurus","Squirrel-Headed","Tricer-","Griffin-headed"]
    hats= ["colonial","fancy",""]

    body = random.choice(bodies)
    head = random.choice(heads)
    hat = random.choice(hats)

    

    claw = random.randint(0, 10)
    
    if claw == 5:
        return Image.open("parts/clawdius.png"),"Clawdius"
    bod_url = "parts/"+body+".png"
    base_img = Image.open(bod_url)

    head_url = "parts/"+head+".png"
    head_img = Image.open(head_url)

    

    loc = head_offset(head,body)
    base_img.paste(head_img,loc,head_img)

    if hat!="":
        hat_url = "parts/"+hat+".png"
        hat_img = Image.open(hat_url)
        hatloc = hat_offset(head,body,hat)
        base_img.paste(hat_img,hatloc,hat_img)


    name = hat +" "+head +" "+body
    
    return base_img, name
    #base_image.paste(rock_img,spot.loc(),rock_img)

def head_offset(head,body):
    headDict = {"tyrannosaurus":[48,187],"Squirrel-Headed":[40,110],"Tricer-":[30,110],"Griffin-headed":[135,175]}
    bodDict = {"-Rex":[500,165],"Squirrel":[515,220],"itops":[490,270],"Griffin":[530,315]}
    
    offx = bodDict[body][0]-headDict[head][0]
    offy = bodDict[body][1]-headDict[head][1]
    return (offx,offy)

def hat_offset(head,body,hat):
    headDict = {"tyrannosaurus":[48,187],"Squirrel-Headed":[40,110],"Tricer-":[30,110],"Griffin-headed":[135,175]}

    hatPlace = {"tyrannosaurus":[78,98],"Squirrel-Headed":[70,50],"Tricer-":[115,50],"Griffin-headed":[90,30]}
    bodDict = {"-Rex":[500,165],"Squirrel":[515,220],"itops":[490,270],"Griffin":[530,315]}
    hatDict = {"colonial":[45,80],"fancy":[45,65]}
    
    headrealx = bodDict[body][0]-headDict[head][0] # head base
    headrealy = bodDict[body][1]-headDict[head][1] # head base

    hatoffx = hatPlace[head][0]- hatDict[hat][0]
    hatoffy = hatPlace[head][1]- hatDict[hat][1]

    return(headrealx+hatoffx,headrealy+hatoffy)

    
  



if __name__ == "__main__":
    for i in range(50):
        im,name = genFossil()
        im.save("Fossil"+str(i)+".png")