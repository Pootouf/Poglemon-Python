import sys, random, marshal, time, os
import pickle as pickle

sys.path.append('..\lib')
import pygame, numpy

pygame.init()

#Importation des autres fichiers

sys.path.append('.')
import chargement as chargement
import event as Event
import save as save
import menu as menu
import pc
import statsPog
import map
import poglemonCharge
import options

from pygame.locals import *

#Initalialisation des Textures

player1 = pygame.image.load("../textures/player1.png")
player2 = pygame.image.load("../textures/player2.png")
player3 = pygame.image.load("../textures/player3.png")
player4 = pygame.image.load("../textures/player4.png")
playercote1 = pygame.image.load("../textures/playercote1.png")
playercote2 = pygame.image.load("../textures/playercote2.png")
playercote3 = pygame.image.load("../textures/playercote3.png")
cadre = pygame.image.load("../textures/cadre.png")
cadreMenuPause = pygame.image.load("../textures/cadreMenuPause.png")
cadreMenuPauseSelection = pygame.image.load("../textures/cadreMenuPauseSelection.png")
cadreMenuDemarrage = pygame.image.load("../textures/cadreMenuDemarrage.png")
cadreCommandes = pygame.image.load("../textures/Commandes.png")


black = 0, 0, 0
grey = 120, 120, 120

def start():

    global cadre, cadreMenuPause, cadreMenuPauseSelection, cadreMenuDemarrage, cadreCommandes, police, police2, police3, resolutionx, resolutiony, screen

    cadre = pygame.image.load("../textures/cadre.png")
    cadreMenuPause = pygame.image.load("../textures/cadreMenuPause.png")
    cadreMenuPauseSelection = pygame.image.load("../textures/cadreMenuPauseSelection.png")
    cadreMenuDemarrage = pygame.image.load("../textures/cadreMenuDemarrage.png")
    cadreCommandes = pygame.image.load("../textures/Commandes.png")

    #Initialisation de l'écran
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

    pygame.display.set_caption("Poglemon")






    cadreMenuPause = pygame.transform.scale(cadreMenuPause, (int(resolutionx/2.4), int(resolutiony/1.96)))
    cadreMenuPauseSelection = pygame.transform.scale(cadreMenuPauseSelection, (int(resolutionx/2.61), int(resolutiony/10.8)))
    cadreCommandes = pygame.transform.scale(cadreCommandes, (int(resolutionx/3.84), int(resolutiony/1.5)))
    cadreMenuDemarrage = pygame.transform.scale(cadreMenuDemarrage, (int(resolutionx/2.74), int(resolutiony/8.64)))
    cadre = pygame.transform.scale(cadre, (resolutionx, int(resolutiony/3.6)))

    #Initialisation du F3

    police = pygame.font.Font(None,int(resolutionx/42.67))
    police2 = pygame.font.Font(None,int(resolutionx/9.6))
    police3 = pygame.font.Font(None,int(resolutionx/19.2))

    chargement.start()
    menu.start()
    pc.start()
    statsPog.start()
    Event.start()
    poglemonCharge.start()
    options.start()



start()



detail = 0
clock = pygame.time.Clock()
pygame.key.set_repeat(5, 5)


#Initialisation des variables

positionx = 10*96
positiony = 10*90
coordx = positionx/96
coordy = positiony/90

zone = 1
face = 1


evenement = 1
evenementposition = 0

pause = False
jeu_en_cours = True







#Initialisation menu



texteMenu = police2.render(("Poglemon"),True,pygame.Color("#000000"))


texteMenu2 = police3.render(("Nouvelle Partie"),True,pygame.Color("#000000"))

if os.path.isfile("../zone/zone1-2.npy") == True:

    texteMenu3 = police3.render(("Continuer la Partie"),True,pygame.Color("#000000"))
else:
    texteMenu3 = police3.render(("Continuer la Partie"),True,pygame.Color("#606060"))


texteMenu4 = police3.render(("Quitter le jeu"),True,pygame.Color("#000000"))


positionCadreX = int(resolutionx/3.2)
positionCadreY = int(resolutiony/2.92)


poglemonstats = {}
pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))

pygame.display.flip()

pause = True

while pause == True:

    screen.fill(grey)
    screen.blit(texteMenu, (int(resolutionx/3.2), int(resolutiony/36)))
    screen.blit(texteMenu2, (int(resolutionx/2.82), int(resolutiony/2.7)))
    screen.blit(texteMenu3, (int(resolutionx/3.05), int(resolutiony/1.96)))
    screen.blit(texteMenu4, (int(resolutionx/2.7), int(resolutiony/1.54)))
    screen.blit(cadreMenuDemarrage, (positionCadreX, positionCadreY))
    screen.blit(cadreCommandes, (int(resolutionx/1.37), int(resolutiony/5.4)))

    pygame.display.flip()

    time.sleep(0.07)


    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_s and positionCadreY != (int(resolutiony/2.92) +2*int(resolutiony/7.2)):

                positionCadreY += int(resolutiony/7.2)


            if event.key == pygame.K_w and positionCadreY != int(resolutiony/2.92):

                positionCadreY -= int(resolutiony/7.2)

            if event.key == pygame.K_SPACE and positionCadreY == int(resolutiony/2.92):

                if os.path.isfile("../zone/zone1.npy") == False:
                    map.InitialisationMap()

                poglemonstats = {}
                world = numpy.load("../zone/zone1.npy")

                if os.path.isfile("../zone/zone1-2.npy") == True:
                    os.remove("../zone/zone1-2.npy")

                if os.path.isfile("../save/save") == True:
                    os.remove("../save/save")

                if os.path.isfile("./save/poglemonstatsSAVE") == True:
                    os.remove("../save/poglemonstatsSAVE")

                data = {}
                pickle.dump(data, open( "../save/save", "wb" ))
                pickle.dump(poglemonstats, open( "../save/poglemonstatsSAVE", "wb" ))

                #Initialisation des poglemon

                pog1 = None
                pog1id = 0
                pog2 = None
                pog2id = 0
                pog3 = None
                pog3id = 0
                pog4 = None
                pog4id = 0
                pog5 = None
                pog5id = 0
                pog6 = None
                pog6id = 0

                pause = False

                time.sleep(0.2)

            if event.key == pygame.K_SPACE and positionCadreY == (int(resolutiony/2.92) + int(resolutiony/7.2)) and os.path.isfile("../zone/zone1-2.npy") == True:

                data = pickle.load( open( "../save/save", "rb" ))

                if os.path.isfile("../zone/zone1.npy") == True:
                    os.remove("../zone/zone1.npy")

                world = numpy.load("../zone/zone1-2.npy")
                poglemonstats = pickle.load( open( "../save/poglemonstatsSAVE", "rb" ))
                positionx = data.get("positionx")
                positiony = data.get("positiony")
                zone = data.get("zone")
                pog1 = data.get("pog1")
                pog2 = data.get("pog2")
                pog3 = data.get("pog3")
                pog4 = data.get("pog4")
                pog5 = data.get("pog5")
                pog6 = data.get("pog6")

                poglemonCharge.poglemonMenu(poglemonstats)
                pause = False

                time.sleep(0.2)

            if event.key == pygame.K_SPACE and positionCadreY == (int(resolutiony/2.92) +2*int(resolutiony/7.2)):
                jeu_en_cours = False
                pause = False
                break




#Chargement de l'écran

if jeu_en_cours == True:

    chargement.chargementMap(positionx - resolutionx/2, positiony - resolutiony/2, zone, world)
    pygame.display.update()

    poglemonCharge.poglemonMenu(poglemonstats)


def load_image(name):
    player = pygame.image.load(name)
    return player




class TestSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(TestSprite, self).__init__()
        self.images = []
        for x in range(0,5):
            self.images.append(load_image('../textures/player1.png'))
        for x in range(0,5):
            self.images.append(load_image('../textures/player2.png'))
        for x in range(0,5):
            self.images.append(load_image('../textures/player3.png'))
        for x in range(0,5):
            self.images.append(load_image('../textures/player4.png'))
        for x in range(0,5):
            self.images.append(load_image('../textures/player3.png'))
        for x in range(0,5):
            self.images.append(load_image('../textures/player2.png'))

        self.images2 = []
        self.images2.append(load_image('../textures/playercote1.png'))

        self.images3 = []
        self.images3.append(load_image('../textures/playercote2.png'))

        self.images4 = []
        for x in range (0,10):
            self.images4.append(load_image('../textures/playercote3.png'))
        for x in range (0,10):
            self.images4.append(load_image('../textures/playercote3-2.png'))
        for x in range (0,10):
            self.images4.append(load_image('../textures/playercote3-3.png'))



        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(resolutionx/2, resolutiony/2, 96, 90)
        print(resolutionx)

    def update(self):

        if face == 1:

            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]

        if face == 2:

            self.index += 1
            if self.index >= len(self.images2):
                self.index = 0
            self.image = self.images2[self.index]

        if face == 3:

            self.index += 1
            if self.index >= len(self.images3):
                self.index = 0
            self.image = self.images3[self.index]

        if face == 4:

            self.index += 1
            if self.index >= len(self.images4):
                self.index = 0
            self.image = self.images4[self.index]






#F3

def coords():

    if detail == 1:

        chargement.chargementPositionCoords(positionx - resolutionx/2, positiony - resolutiony/2, zone, world)



        fps = police.render(str(int(clock.get_fps())), True, pygame.Color('yellow'))
        FPS = police.render(("FPS:"),True,pygame.Color("#FFFF00"))
        screen.blit(FPS, (int(resolutionx/384), int(resolutiony/36)))
        screen.blit(fps, (int(resolutionx/25.6), int(resolutiony/36)))
        coordx = int(positionx/96)
        coordy = int(positiony/90)

        X = police.render(("X:"),True,pygame.Color("#FFFF00"))
        Y = police.render(("Y:"),True,pygame.Color("#FFFF00"))
        xx = police.render(str(coordx), True, pygame.Color('yellow'))
        yy = police.render(str(coordy), True, pygame.Color('yellow'))
        screen.blit(X, (int(resolutionx/384), int(resolutiony/18)))
        screen.blit(xx, (int(resolutionx/25.6), int(resolutiony/18)))
        screen.blit(Y, (int(resolutionx/384), int(resolutiony/12)))
        screen.blit(yy, (int(resolutionx/25.6), int(resolutiony/12)))


#Main


my_sprite = TestSprite()
my_group = pygame.sprite.Group(my_sprite)



while jeu_en_cours == True:


    chargement.chargementPosition(positionx, positiony, zone, world)
    coords()
    my_group.update()
    my_group.draw(screen)
    pygame.display.flip()
    clock.tick(200)



    if positionx/96  == 16 and positiony/90  == 35:
        print("zone2")
        zone = 2
        positionx = 4896
        positiony = 10*90
        chargement.chargementMap(positionx -resolutionx/2, positiony - resolutiony/2, zone, world)

    if positionx/96  == 17 and positiony/90 == 35:
        print("zone2")
        zone = 2
        positionx = 4896
        positiony = 10*90
        chargement.chargementMap(positionx -resolutionx/2, positiony - resolutiony/2, zone, world)

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:




            if event.key == pygame.K_w:

                face = 4

                if world[int(positionx/96), int(positiony/90 - 1)] == 2 or world[int(positionx/96), int(positiony/90 - 1)] == 3 or world[int(positionx/96), int(positiony/90 - 1)] == 15 or world[int(positionx/96), int(positiony/90 - 1)] == 16 or world[int(positionx/96), int(positiony/90 - 1)] == 17 or world[int(positionx/96), int(positiony/90 - 1)] == 18:
                    break

                if world[int(positionx/96), int(positiony/90 - 1)] == 4 :


                    p = random.randint(0,100)

                    if p<= (1.25/187.5)*100:
                        Event.poglemonSauvage(5, zone, poglemonstats, pause, positionx, positiony, world, False)
                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))
                        break
                    elif p<= (3.33/187.5)*100:
                        Event.poglemonSauvage(4, zone, poglemonstats, pause, positionx, positiony, world, False)
                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))
                        break
                    elif p<= (6.75/187.5)*100:
                        Event.poglemonSauvage(3, zone, poglemonstats, pause, positionx, positiony, world, False)
                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))
                        break
                    elif p<= (8.5/187.5)*100:
                        Event.poglemonSauvage(2, zone, poglemonstats, pause, positionx, positiony, world, False)
                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))
                        break
                    elif p<= (10/187.5)*100:
                        Event.poglemonSauvage(1, zone, poglemonstats, pause, positionx, positiony, world, False)
                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))
                        break

                if world[int(positionx/96), int(positiony/90 - 1)] == 69:

                    for x in range(1, 7):
                        if poglemonstats.get("pog" + str(x)) != None:
                            poglemonstats["pog" + str(x) + "hpActuel"] = poglemonstats["pog" + str(x) + "hp"]

                            for y in range (1, 5):
                                if poglemonstats.get("pog" + str(x) + "attaque" + str(y)) != None:
                                    poglemonstats["pog" + str(x) + "attaque" + str(y) + "pprestant"] = poglemonstats["pog" + str(x) + "attaque" + str(y) + "pp"]

                    pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))
                    break



                for x in range(0,10):
                    positiony -= 9


                    clock.tick(200)
                    chargement.chargementMap(positionx -resolutionx/2, positiony - resolutiony/2, zone, world)
                    coords()
                    my_group.update()
                    my_group.draw(screen)
                    pygame.display.update()





            if event.key == pygame.K_a:

                face = 2

                if world[int(positionx/96) - 1, int(positiony/90 )] == 2 or world[int(positionx/96) - 1, int(positiony/90 )] == 3 or world[int(positionx/96) - 1, int(positiony/90 )] == 15 or world[int(positionx/96) - 1, int(positiony/90 )] == 16 or world[int(positionx/96) - 1, int(positiony/90 )] == 17 or world[int(positionx/96) - 1, int(positiony/90 )] == 18:
                    break

                if world[int(positionx/96) - 1, int(positiony/90 )] == 4 :


                    p = random.randint(0,100)

                    if p<= (1.25/187.5)*100:
                        Event.poglemonSauvage(5, zone, poglemonstats, pause, positionx, positiony, world, False)
                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))
                        break
                    elif p<= (3.33/187.5)*100:
                        Event.poglemonSauvage(4, zone, poglemonstats, pause, positionx, positiony, world, False)
                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))
                        break
                    elif p<= (6.75/187.5)*100:
                        Event.poglemonSauvage(3, zone, poglemonstats, pause, positionx, positiony, world, False)
                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))
                        break
                    elif p<= (8.5/187.5)*100:
                        Event.poglemonSauvage(2, zone, poglemonstats, pause, positionx, positiony, world, False)
                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))
                        break
                    elif p<= (10/187.5)*100:
                        Event.poglemonSauvage(1, zone, poglemonstats, pause, positionx, positiony, world, False)
                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))
                        break

                if world[int(positionx/96) - 1, int(positiony/90 )] == 69:

                    for x in range(1, 7):
                        if poglemonstats.get("pog" + str(x)) != None:
                            poglemonstats["pog" + str(x) + "hpActuel"] = poglemonstats["pog" + str(x) + "hp"]

                            for y in range (1, 5):
                                if poglemonstats.get("pog" + str(x) + "attaque" + str(y)) != None:
                                    poglemonstats["pog" + str(x) + "attaque" + str(y) + "pprestant"] = poglemonstats["pog" + str(x) + "attaque" + str(y) + "pp"]

                    pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))
                    break



                for x in range(0,12):
                    positionx -= 8
                    clock.tick(200)
                    chargement.chargementMap(positionx -resolutionx/2, positiony - resolutiony/2, zone, world)
                    coords()
                    my_group.update()
                    my_group.draw(screen)
                    pygame.display.update()






            if event.key == pygame.K_d:

                face = 3

                if world[int(positionx/96) + 1, int(positiony/90)] == 2 or world[int(positionx/96) + 1, int(positiony/90)] == 3 or world[int(positionx/96) + 1, int(positiony/90)] == 15 or world[int(positionx/96) + 1, int(positiony/90)] == 16 or world[int(positionx/96) + 1, int(positiony/90)] == 17 or world[int(positionx/96) + 1, int(positiony/90)] == 18:
                    break

                if world[int(positionx/96) + 1, int(positiony/90)] == 4 :


                    p = random.randint(0,100)

                    if p<= (1.25/187.5)*100:
                        Event.poglemonSauvage(5, zone, poglemonstats, pause, positionx, positiony, world, False)
                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))
                        break
                    elif p<= (3.33/187.5)*100:
                        Event.poglemonSauvage(4, zone, poglemonstats, pause, positionx, positiony, world, False)
                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))
                        break
                    elif p<= (6.75/187.5)*100:
                        Event.poglemonSauvage(3, zone, poglemonstats, pause, positionx, positiony, world, False)
                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))
                        break
                    elif p<= (8.5/187.5)*100:
                        Event.poglemonSauvage(2, zone, poglemonstats, pause, positionx, positiony, world, False)
                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))
                        break
                    elif p<= (10/187.5)*100:
                        Event.poglemonSauvage(1, zone, poglemonstats, pause, positionx, positiony, world, False)
                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))
                        break

                if world[int(positionx/96) + 1, int(positiony/90)] == 69:

                    for x in range(1, 7):
                        if poglemonstats.get("pog" + str(x)) != None:
                            poglemonstats["pog" + str(x) + "hpActuel"] = poglemonstats["pog" + str(x) + "hp"]

                            for y in range (1, 5):
                                if poglemonstats.get("pog" + str(x) + "attaque" + str(y)) != None:
                                    poglemonstats["pog" + str(x) + "attaque" + str(y) + "pprestant"] = poglemonstats["pog" + str(x) + "attaque" + str(y) + "pp"]

                    pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))
                    break



                for x in range(0,12):
                    positionx += 8
                    clock.tick(200)
                    chargement.chargementMap(positionx -resolutionx/2, positiony - resolutiony/2, zone, world)
                    coords()
                    my_group.update()
                    my_group.draw(screen)
                    pygame.display.update()









            if event.key == pygame.K_s:

                face = 1

                if world[int(positionx/96), int(positiony/90 + 1)] == 2 or world[int(positionx/96), int(positiony/90 + 1)] == 3 or world[int(positionx/96), int(positiony/90 + 1)] == 15 or world[int(positionx/96), int(positiony/90 + 1)] == 16 or world[int(positionx/96), int(positiony/90 + 1)] == 17 or world[int(positionx/96), int(positiony/90 + 1)] == 18:
                    break

                if world[int(positionx/96), int(positiony/90 + 1)] == 4 :


                    p = random.randint(0,100)

                    if p<= (1.25/187.5)*100:
                        Event.poglemonSauvage(5, zone, poglemonstats, pause, positionx, positiony, world, False)
                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))
                        break
                    elif p<= (3.33/187.5)*100:
                        Event.poglemonSauvage(4, zone, poglemonstats, pause, positionx, positiony, world, False)
                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))
                        break
                    elif p<= (6.75/187.5)*100:
                        Event.poglemonSauvage(3, zone, poglemonstats, pause, positionx, positiony, world, False)
                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))
                        break
                    elif p<= (8.5/187.5)*100:
                        Event.poglemonSauvage(2, zone, poglemonstats, pause, positionx, positiony, world, False)
                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))
                        break
                    elif p<= (10/187.5)*100:
                        Event.poglemonSauvage(1, zone, poglemonstats, pause, positionx, positiony, world, False)
                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))
                        break

                if world[int(positionx/96), int(positiony/90 + 1)] == 69:

                    for x in range(1, 7):
                        if poglemonstats.get("pog" + str(x)) != None:
                            poglemonstats["pog" + str(x) + "hpActuel"] = poglemonstats["pog" + str(x) + "hp"]

                            for y in range (1, 5):
                                if poglemonstats.get("pog" + str(x) + "attaque" + str(y)) != None:
                                    poglemonstats["pog" + str(x) + "attaque" + str(y) + "pprestant"] = poglemonstats["pog" + str(x) + "attaque" + str(y) + "pp"]

                    pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))
                    break






                for x in range(0,10):
                    positiony += 9
                    clock.tick(200)
                    chargement.chargementMap(positionx -resolutionx/2, positiony - resolutiony/2, zone, world)
                    coords()
                    my_group.update()
                    my_group.draw(screen)
                    pygame.display.update()





            if event.key == pygame.K_F3:



                if detail == 1:
                    detail = 0
                    chargement.chargementPositionCoords(positionx - resolutionx/2, positiony - resolutiony/2, zone, world)

                elif detail == 0:
                    detail = 1

                pygame.display.update()
                time.sleep(0.2)






            if event.key == pygame.K_SPACE:
                pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))

                Event.event(positionx, positiony, face, world, cadre, police, pause, poglemonstats)

                poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))



                chargement.chargementMap(positionx -resolutionx/2, positiony - resolutiony/2, zone, world)





            if event.key == pygame.K_F4:
                print("charge")


                data = pickle.load( open( "../save/save", "rb" ))

                world = numpy.load("../zone/zone1-2.npy")
                poglemonstats = pickle.load( open( "../save/poglemonstatsSAVE", "rb" ))
                print(data)
                positionx = data.get("positionx")
                positiony = data.get("positiony")
                zone = data.get("zone")
                pog1 = data.get("pog1")
                pog2 = data.get("pog2")
                pog3 = data.get("pog3")
                pog4 = data.get("pog4")
                pog5 = data.get("pog5")
                pog6 = data.get("pog6")

                poglemonCharge.poglemonMenu(poglemonstats)

                time.sleep(0.2)

            if event.key == pygame.K_F5:
                poglemonstats = {}
                pickle.dump(poglemonstats, open( "../save/poglemonstatsSAVE", "wb" ))

            if event.key == pygame.K_u:

                id = random.randint(1, 9999999999999999999999999)
                Event.initialisationpogle(id, 11, poglemonstats, 27, True, "wow")
                pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))




            if event.key == pygame.K_i:


                menu.chargementMenu(positionx -resolutionx/2, positiony - resolutiony/2, zone, world, data, poglemonstats)
                poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))
                chargement.chargementMap(positionx -resolutionx/2, positiony - resolutiony/2, zone, world)


            if event.key == pygame.K_ESCAPE:

                texteRevenir = police3.render(("Revenir au jeu"),True,pygame.Color("#000000"))
                textePause = police3.render(("Pause"),True,pygame.Color("#000000"))
                texteOption = police3.render(("Options"),True,pygame.Color("#000000"))
                texteQuitter = police3.render(("Quitter le jeu"),True,pygame.Color("#000000"))

                positionCadreX2 = int(resolutionx/3.23)
                positionCadreY2 = int(resolutiony/2.23)

                screen.blit(cadreMenuPause, (int(resolutionx/3.43), int(resolutiony/3.6)))
                screen.blit(textePause, (int(resolutionx/2.26), int(resolutiony/3.09)))
                screen.blit(texteRevenir, (int(resolutionx/2.65), int(resolutiony/2.16)))
                screen.blit(texteOption, (int(resolutionx/2.34), int(resolutiony/1.8)))
                screen.blit(texteQuitter, (int(resolutionx/2.56), int(resolutiony/1.54)))
                screen.blit(cadreMenuPauseSelection, (positionCadreX2, positionCadreY2))
                screen.blit(cadreCommandes, (int(resolutionx/1.37), int(resolutiony/5.4)))



                pygame.display.flip()

                pause2 = True

                while pause2 == True:

                    screen.blit(cadreMenuPause, (int(resolutionx/3.43), int(resolutiony/3.6)))
                    screen.blit(textePause, (int(resolutionx/2.26), int(resolutiony/3.09)))
                    screen.blit(texteRevenir, (int(resolutionx/2.65), int(resolutiony/2.16)))
                    screen.blit(texteOption, (int(resolutionx/2.34), int(resolutiony/1.8)))
                    screen.blit(texteQuitter, (int(resolutionx/2.56), int(resolutiony/1.54)))
                    screen.blit(cadreMenuPauseSelection, (positionCadreX2, positionCadreY2))
                    screen.blit(cadreCommandes, (int(resolutionx/1.37), int(resolutiony/5.4)))

                    pygame.display.flip()

                    time.sleep(0.1)

                    for event in pygame.event.get():

                        if event.type == pygame.KEYDOWN:

                            if event.key == pygame.K_w and positionCadreY2 >= resolutionx/3.96:
                                positionCadreY2 -= int(resolutiony/10.8)

                            if event.key == pygame.K_s and positionCadreY2 <= resolutiony/1.59:
                                positionCadreY2 += int(resolutiony/10.8)

                            if event.key == pygame.K_SPACE and positionCadreY2 == int(resolutiony/2.23):
                                pause2 = False
                                time.sleep(0.2)
                                chargement.chargementMap(positionx -resolutionx/2, positiony - resolutiony/2, zone, world)
                                break

                            if event.key == pygame.K_SPACE and positionCadreY2 == (int(resolutiony/2.23) + 2*(int(resolutiony/10.8))):
                                pause2 = False
                                jeu_en_cours = False
                                break

                            if event.key == pygame.K_SPACE and positionCadreY2 == (int(resolutiony/2.23) + 1*(int(resolutiony/10.8))):
                                options.changementResolution()
                                start()
                                pause2 = False
                                my_sprite = TestSprite()
                                my_group = pygame.sprite.Group(my_sprite)
                                chargement.chargementMap(positionx -resolutionx/2, positiony - resolutiony/2, zone, world)
                                break

                            if event.key == pygame.K_ESCAPE:
                                pause2 = False
                                time.sleep(0.2)
                                chargement.chargementMap(positionx -resolutionx/2, positiony - resolutiony/2, zone, world)
                                break
