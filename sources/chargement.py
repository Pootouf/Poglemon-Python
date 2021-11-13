import pygame, numpy, random, os, pickle

herbe = pygame.image.load("../textures/herbe.png")
hautesHerbes = pygame.image.load("../textures/hautesHerbes.png")
fleur = pygame.image.load("../textures/fleur.png")
arbre = pygame.image.load("../textures/arbre.png")
arbuste = pygame.image.load("../textures/arbuste.png")
dieuGlete = pygame.image.load("../textures/dieuGlete.png")
nuageon = pygame.image.load("../textures/nuageon.png")
poupinus = pygame.image.load("../textures/poupinus.png")
pingouinou = pygame.image.load("../textures/pingouinou.png")
centreSoin = pygame.image.load("../textures/centreSoin.png")



from pygame.locals import *

def start():

    global resolutionx, resolutiony, chargex, chargey, screen


    if os.path.isfile("../save/resolution") == False:


        resolution = pygame.display.Info()
        resolutionx = resolution.current_w
        resolutiony = resolution.current_h
        chargex = int(resolution.current_w/91) + 2
        chargey = int(resolution.current_h/82) + 1

        resolution = {}
        resolution["resolutionx"] = resolutionx
        resolution["resolutiony"] = resolutiony

        pickle.dump(resolution, open( "../save/resolution", "wb" ))
    else:
        resolution = pickle.load( open( "../save/resolution", "rb" ))
        resolutionx = resolution["resolutionx"]
        resolutiony = resolution["resolutiony"]
        chargex = int(resolutionx/91) + 2
        chargey = int(resolutiony/82) + 1



    size = width, height = resolutionx, resolutiony

    flags = DOUBLEBUF
    screen = pygame.display.set_mode(size, flags)
    screen.set_alpha(None)



def chargementMap(positionx, positiony, zone, world):



    coordx = int(positionx/96)
    coordy = int(positiony/90)


    # Zone de départ




    for x in range(coordx -1, coordx + chargex):
        for y in range(coordy -1,coordy + chargey):



            if world[int( x ), int( y )] == 1:
                screen.blit(herbe, ( x *96 - positionx, y *90 - positiony))

            if world[int( x ), int( y )] == 3:
                screen.blit(arbre, (x *96 - positionx,  y*90 - positiony))

            if world[int( x ), int( y )] == 0:
                screen.blit(fleur, (x *96 - positionx,  y*90 - positiony))



            if zone ==1:

                if world[int( x ), int( y )] == 15:
                    screen.blit(herbe, ( x *96 - positionx, y *90 - positiony))
                    screen.blit(dieuGlete, (x *96 - positionx,  y*90 - positiony))



            if zone == 2:

                if world[int( x ), int( y )] == 16:
                    screen.blit(herbe, ( x *96 - positionx, y *90 - positiony))
                    screen.blit(nuageon, (x *96 - positionx,  y*90 - positiony))

                if world[int( x ), int( y )] == 17:
                    screen.blit(herbe, ( x *96 - positionx, y *90 - positiony))
                    screen.blit(poupinus, (x *96 - positionx,  y*90 - positiony))

                if world[int( x ), int( y )] == 18:
                    screen.blit(herbe, ( x *96 - positionx, y *90 - positiony))
                    screen.blit(pingouinou, (x *96 - positionx,  y*90 - positiony))

                if world[int( x ), int( y )] == 4:
                    screen.blit(hautesHerbes, (x *96 - positionx,  y*90 - positiony))

                if world[int( x ), int( y )] == 69:
                    screen.blit(herbe, ( x *96 - positionx, y *90 - positiony))
                    screen.blit(centreSoin, (x *96 - positionx,  y*90 - positiony))


def chargementPosition(positionx, positiony, zone, world):

    x = int(positionx/96)
    y = int(positiony/90)




    if world[int( x ), int( y )] == 1:
        screen.blit(herbe, ( resolutionx/2,  resolutiony/2))



    if world[int( x ), int( y )] == 0:
        screen.blit(fleur, ( resolutionx/2,  resolutiony/2))


    if zone == 2:

        if world[int( x ), int( y )] == 4:
            screen.blit(hautesHerbes, ( resolutionx/2,  resolutiony/2))

def chargementPositionCoords(positionx, positiony, zone, world):

    coordx = int(positionx/96)
    coordy = int(positiony/90)



    # Zone de départ

    for x in range(coordx -3, coordx +4):
        for y in range(coordy -2,coordy + 2):



            if world[int( x ), int( y )] == 1:
                screen.blit(herbe, ( x *96 - positionx, y *90 - positiony))

            if world[int( x ), int( y )] == 3:
                screen.blit(arbre, (x *96 - positionx,  y*90 - positiony))

            if world[int( x ), int( y )] == 0:
                screen.blit(fleur, (x *96 - positionx,  y*90 - positiony))

            if zone ==1:

                if world[int( x ), int( y )] == 15:
                    screen.blit(herbe, ( x *96 - positionx, y *90 - positiony))
                    screen.blit(dieuGlete, (x *96 - positionx,  y*90 - positiony))

            if zone == 2:

                if world[int( x ), int( y )] == 16:
                    screen.blit(herbe, ( x *96 - positionx, y *90 - positiony))
                    screen.blit(nuageon, (x *96 - positionx,  y*90 - positiony))

                if world[int( x ), int( y )] == 17:
                    screen.blit(herbe, ( x *96 - positionx, y *90 - positiony))
                    screen.blit(poupinus, (x *96 - positionx,  y*90 - positiony))

                if world[int( x ), int( y )] == 18:
                    screen.blit(herbe, ( x *96 - positionx, y *90 - positiony))
                    screen.blit(pingouinou, (x *96 - positionx,  y*90 - positiony))

                if world[int( x ), int( y )] == 4:
                    screen.blit(hautesHerbes, (x *96 - positionx,  y*90 - positiony))

                if world[int( x ), int( y )] == 69:
                    screen.blit(herbe, ( x *96 - positionx, y *90 - positiony))
                    screen.blit(centreSoin, (x *96 - positionx,  y*90 - positiony))
