import pygame, os, pickle

from pygame.locals import *

nuageon = pygame.image.load("../textures/nuageon.png")
poupinus = pygame.image.load("../textures/poupinus.png")
pingouinou = pygame.image.load("../textures/pingouinou.png")
dieuGlete = pygame.image.load("../textures/dieuGlete.png")
doof = pygame.image.load("../textures/Doof.png")
multiDoof = pygame.image.load("../textures/Multidoof.png")



def start():

    global nuageon, poupinus, pingouinou, dieuGlete, doof, multiDoof, resolutionx, resolutiony, screen

    if os.path.isfile("../save/resolution") == False:


        resolution = pygame.display.Info()
        resolutionx = resolution.current_w
        resolutiony = resolution.current_h

        resolution = {}
        resolution["resolutionx"] = resolutionx
        resolution["resolutiony"] = resolutiony

        pickle.dump(resolution, open( "../save/resolution", "wb" ))
    else:
        resolution = pickle.load( open( "../save/resolution", "rb" ))
        resolutionx = resolution["resolutionx"]
        resolutiony = resolution["resolutiony"]



    size = width, height = resolutionx, resolutiony

    flags = DOUBLEBUF
    screen = pygame.display.set_mode(size, flags)
    screen.set_alpha(None)




    nuageon = pygame.transform.scale(nuageon, (int(resolutionx/20), int(resolutiony/12)))
    poupinus = pygame.transform.scale(poupinus, (int(resolutionx/20), int(resolutiony/12)))
    pingouinou = pygame.transform.scale(pingouinou, (int(resolutionx/20), int(resolutiony/12)))
    dieuGlete = pygame.transform.scale(dieuGlete, (int(resolutionx/20), int(resolutiony/12)))
    doof = pygame.transform.scale(doof, (int(resolutionx/20), int(resolutiony/12)))
    multiDoof = pygame.transform.scale(multiDoof, (int(resolutionx/20), int(resolutiony/12)))

#Liste a agrandir pour plus de poglemon
listeSprite = {}
listeSprite["1"] = nuageon
listeSprite["4"] = poupinus
listeSprite["7"] = pingouinou
listeSprite["10"] = doof
listeSprite["11"] = multiDoof
listeSprite["999"] = dieuGlete



def poglemonMenu(poglemonstats):

    chargepog = {}

    for x in range (1, 7):

        if poglemonstats.get("pog" + str(x)) != None:
            chargepog[x] = listeSprite[str(poglemonstats.get("pog" + str(x)))]
        else:
            chargepog[x] = pygame.image.load("../textures/rien.png")



    try:

        pygame.image.save(chargepog[1], "../textures/chargePog1.png")
        pygame.image.save(chargepog[2], "../textures/chargePog2.png")
        pygame.image.save(chargepog[3], "../textures/chargePog3.png")
        pygame.image.save(chargepog[4], "../textures/chargePog4.png")
        pygame.image.save(chargepog[5], "../textures/chargePog5.png")
        pygame.image.save(chargepog[6], "../textures/chargePog6.png")
    except:

        print("Impossible de trouver les images OOF")

def poglemonPC(pog):
    print(pog)

    chargepog7 = listeSprite[str(pog)]
    pygame.image.save(chargepog7, "../textures/chargePog7.png")

def poglemonCombat(pog, pog1):

    print(pog1)

    chargepog8 = listeSprite[str(pog)]
    chargepog8 = pygame.transform.scale(chargepog8, (int(resolutionx/9.6), int(resolutiony/5.74)))

    chargepog9 = listeSprite[str(pog1)]
    chargepog9 = pygame.transform.scale(chargepog9, (int(resolutionx/9.6), int(resolutiony/5.74)))

    pygame.image.save(chargepog8, "../textures/chargePog8.png")
    pygame.image.save(chargepog9, "../textures/chargePog9.png")

def poglemonPcMenu(numeroBoite, poglemonstats):


    positionx = int(resolutionx/9.6)
    positiony = int(resolutiony/4.8)

    for x in range(1 + (numeroBoite-1)*30, 31 + (numeroBoite-1)*30):

            if poglemonstats.get("pc"+str(x)) != None:

                pog = poglemonstats.get("pc"+str(x))

                chargepog = listeSprite[str(pog)]
                chargepog = pygame.transform.scale(chargepog, (int(resolutionx/12.8), int(resolutiony/7.71)))

                screen.blit(chargepog, (positionx, positiony))
                positionx += int(resolutionx/7.11)



            if poglemonstats.get("pc"+str(x)) == None:
                positionx += int(resolutionx/7.11)

            if positionx == int(resolutionx/9.6) + 6*int(resolutionx/7.11):
                positionx = int(resolutionx/9.6)
                positiony += int(resolutiony/6.35)
