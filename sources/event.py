import pygame, time, pickle, random, os

import poglemonCharge
import chargement

from pygame.locals import *

cadreCombat = pygame.image.load("../textures/cadreCombat.png")
cadreCombat2 = pygame.image.load("../textures/cadreCombat2.png")




def start():

    global cadreCombat, cadreCombat2, resolutionx, resolutiony, screen, police1 ,police2 ,police3, police4, police5

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

    cadreCombat = pygame.image.load("../textures/cadreCombat.png")
    cadreCombat2 = pygame.image.load("../textures/cadreCombat2.png")



    cadreCombat = pygame.transform.scale(cadreCombat, (resolutionx, resolutiony))
    cadreCombat2 = pygame.transform.scale(cadreCombat2, (resolutionx, resolutiony))



    police2 = pygame.font.Font(None,int(resolutionx/9.6))
    police1 = pygame.font.Font(None,int(resolutionx/19.2))
    police3 = pygame.font.Font(None,int(resolutionx/42.7))
    police4 = pygame.font.Font(None,int(resolutionx/42.67))
    police5 = pygame.font.Font(None,int(resolutionx/35))


attaqueID = {}

#Liste des attaques

attaqueID["nom" + str(1)] = "Charge"
attaqueID["degat" + str(1)] = 40
attaqueID["pp" + str(1)] = 35
attaqueID["precision" + str(1)] = 100
attaqueID["categorie" + str(1)] = "physique"

attaqueID["nom" + str(2)] = "Cochon"
attaqueID["degat" + str(2)] = 90
attaqueID["pp" + str(2)] = 25
attaqueID["precision" + str(2)] = 90
attaqueID["categorie" + str(2)] = "special"

attaqueID["nom" + str(3)] = "Dinde"
attaqueID["degat" + str(3)] = 250
attaqueID["pp" + str(3)] = 5
attaqueID["precision" + str(3)] = 45
attaqueID["categorie" + str(3)] = "special"

attaqueID["nom" + str(4)] = "Glete"
attaqueID["degat" + str(4)] = 999
attaqueID["pp" + str(4)] = 1
attaqueID["precision" + str(4)] = 1
attaqueID["categorie" + str(4)] = "special"

attaqueID["nom" + str(5)] = "Pelote"
attaqueID["degat" + str(5)] = 1
attaqueID["pp" + str(5)] = 50
attaqueID["precision" + str(5)] = 100
attaqueID["categorie" + str(5)] = "physique"

attaqueID["nom" + str(6)] = "Bourguignon"
attaqueID["degat" + str(6)] = 60
attaqueID["pp" + str(6)] = 15
attaqueID["precision" + str(6)] = 95
attaqueID["categorie" + str(6)] = "physique"

statsPog = {}

#Liste a agrandir pour plus de poglemon

#Stats de nuageon

statsPog["pog" + "hp" + str(1)] = 40
statsPog["pog" + "atk" + str(1)] = 45
statsPog["pog" + "spatk" + str(1)] = 70
statsPog["pog" + "def" + str(1)] = 45
statsPog["pog" + "spdef" + str(1)] = 65
statsPog["pog" + "vit" + str(1)] = 45
statsPog["type1" + str(1)] = "Eau"
statsPog["type2" + str(1)] = "Vol"
statsPog["pog" + "name" + str(1)] = "Nuageon"
statsPog["pog" + "progressionxp" + str(1)] = 3
statsPog["pog" + "basexp" + str(1)] = 65

for x in range(1, 3):
    statsPog["pog" + str(1) + "attaque" + str(x)] = True

statsPog["pog" + str(1) + "attaqueniv" + str(1)] = 1
statsPog["pog" + str(1) + "attaqueniv" + str(2)] = 4

#Stats de poupinus

statsPog["pog" + "hp" + str(4)] = 55
statsPog["pog" + "atk" + str(4)] = 70
statsPog["pog" + "spatk" + str(4)] = 45
statsPog["pog" + "def" + str(4)] = 65
statsPog["pog" + "spdef" + str(4)] = 50
statsPog["pog" + "vit" + str(4)] = 40
statsPog["type1" + str(4)] = "Plante"
statsPog["pog" + "name" + str(4)] = "Poupinus"
statsPog["pog" + "progressionxp" + str(4)] = 3
statsPog["pog" + "basexp" + str(4)] = 65

for x in range(1, 3):
    statsPog["pog" + str(4) + "attaque" + str(x)] = True

statsPog["pog" + str(4) + "attaqueniv" + str(1)] = 1
statsPog["pog" + str(4) + "attaqueniv" + str(2)] = 4

#Stats de pingouinou

statsPog["pog" + "hp" + str(7)] = 55
statsPog["pog" + "atk" + str(7)] = 50
statsPog["pog" + "spatk" + str(7)] = 55
statsPog["pog" + "def" + str(7)] = 50
statsPog["pog" + "spdef" + str(7)] = 60
statsPog["pog" + "vit" + str(7)] = 40
statsPog["type1" + str(7)] = "Feu"
statsPog["pog" + "name" + str(7)] = "Pingouinou"
statsPog["pog" + "progressionxp" + str(7)] = 3
statsPog["pog" + "basexp" + str(7)] = 65

for x in range(1, 3):
    statsPog["pog" + str(7) + "attaque" + str(x)] = True

statsPog["pog" + str(7) + "attaqueniv" + str(1)] = 1
statsPog["pog" + str(7) + "attaqueniv" + str(2)] = 4


#Stats de Doof

statsPog["pog" + "hp" + str(10)] = 60
statsPog["pog" + "atk" + str(10)] = 55
statsPog["pog" + "spatk" + str(10)] = 25
statsPog["pog" + "def" + str(10)] = 45
statsPog["pog" + "spdef" + str(10)] = 35
statsPog["pog" + "vit" + str(10)] = 35
statsPog["type1" + str(10)] = "Normal"
statsPog["pog" + "name" + str(10)] = "Doof"
statsPog["pog" + "progressionxp" + str(10)] = 1
statsPog["pog" + "basexp" + str(10)] = 58

for x in range(1, 4):
    statsPog["pog" + str(10) + "attaque" + str(x)] = True

statsPog["pog" + str(10) + "attaqueniv" + str(1)] = 1
statsPog["pog" + str(10) + "attaqueniv" + str(2)] = 4
statsPog["pog" + str(10) + "attaqueniv" + str(3)] = 4



#Stats de MultiDoof

statsPog["pog" + "hp" + str(11)] = 90
statsPog["pog" + "atk" + str(11)] = 85
statsPog["pog" + "spatk" + str(11)] = 55
statsPog["pog" + "def" + str(11)] = 65
statsPog["pog" + "spdef" + str(11)] = 45
statsPog["pog" + "vit" + str(11)] = 75
statsPog["type1" + str(11)] = "Normal"
statsPog["pog" + "name" + str(11)] = "MultiDoof"
statsPog["pog" + "progressionxp" + str(11)] = 1
statsPog["pog" + "basexp" + str(11)] = 116

for x in range(1, 4):
    statsPog["pog" + str(11) + "attaque" + str(x)] = True

statsPog["pog" + str(11) + "attaqueniv" + str(1)] = 1
statsPog["pog" + str(11) + "attaqueniv" + str(2)] = 4
statsPog["pog" + str(11) + "attaqueniv" + str(3)] = 4



#Stats de dieuGlete

statsPog["pog" + "hp" + str(999)] = 90
statsPog["pog" + "atk" + str(999)] = 130
statsPog["pog" + "spatk" + str(999)] = 175
statsPog["pog" + "def" + str(999)] = 90
statsPog["pog" + "spdef" + str(999)] = 120
statsPog["pog" + "vit" + str(999)] = 135
statsPog["type1" + str(999)] = "Normal"
statsPog["type2" + str(999)] = "Vol"
statsPog["pog" + "name" + str(999)] = "Dieu Glete"
statsPog["pog" + "progressionxp" + str(999)] = 4
statsPog["pog" + "basexp" + str(999)] = 300

for x in range(1, 7):
    statsPog["pog" + str(999) + "attaque" + str(x)] = True

statsPog["pog" + str(999) + "attaqueniv" + str(1)] = 1
statsPog["pog" + str(999) + "attaqueniv" + str(2)] = 2
statsPog["pog" + str(999) + "attaqueniv" + str(3)] = 2
statsPog["pog" + str(999) + "attaqueniv" + str(4)] = 3
statsPog["pog" + str(999) + "attaqueniv" + str(5)] = 4
statsPog["pog" + str(999) + "attaqueniv" + str(6)] = 7



def event(positionx, positiony, face, world, cadre, police, pause, poglemonstats):




    if face ==1:
        if world[int(positionx/96), int(positiony/90 + 1)] == 15:
            screen.blit(cadre, (0,  int(resolutiony/1.38)))
            pygame.display.flip()
            pause = True
            evenement = 2

        if world[int(positionx/96), int(positiony/90 + 1)] == 16:
            screen.blit(cadre, (0,  int(resolutiony/1.38)))
            pygame.display.flip()
            pause = True
            evenement = 3

        if world[int(positionx/96), int(positiony/90 + 1)] == 17:
            screen.blit(cadre, (0,  int(resolutiony/1.38)))
            pygame.display.flip()
            pause = True
            evenement = 4

        if world[int(positionx/96), int(positiony/90 + 1)] == 18:
            screen.blit(cadre, (0,  int(resolutiony/1.38)))
            pygame.display.flip()
            pause = True
            evenement = 5

    if face ==2:
        if world[int(positionx/96) - 1, int(positiony/90 )] == 15:
            screen.blit(cadre, (0,  int(resolutiony/1.38)))
            pygame.display.flip()
            pause = True
            evenement = 2

        if world[int(positionx/96) - 1, int(positiony/90 )] == 16:
            screen.blit(cadre, (0,  int(resolutiony/1.38)))
            pygame.display.flip()
            pause = True
            evenement = 3

        if world[int(positionx/96) - 1, int(positiony/90 )] == 17:
            screen.blit(cadre, (0,  int(resolutiony/1.38)))
            pygame.display.flip()
            pause = True
            evenement = 4

        if world[int(positionx/96) - 1, int(positiony/90 )] == 18:
            screen.blit(cadre, (0,  int(resolutiony/1.38)))
            pygame.display.flip()
            pause = True
            evenement = 5

    if face ==3:
        if world[int(positionx/96) + 1, int(positiony/90)] == 15:
            screen.blit(cadre, (0,  int(resolutiony/1.38)))
            pygame.display.flip()
            pause = True
            evenement = 2

        if world[int(positionx/96) + 1, int(positiony/90)] == 16:
            screen.blit(cadre, (0,  int(resolutiony/1.38)))
            pygame.display.flip()
            pause = True
            evenement = 3

        if world[int(positionx/96) + 1, int(positiony/90)] == 17:
            screen.blit(cadre, (0,  int(resolutiony/1.38)))
            pygame.display.flip()
            pause = True
            evenement = 4

        if world[int(positionx/96) + 1, int(positiony/90)] == 18:
            screen.blit(cadre, (0,  int(resolutiony/1.38)))
            pygame.display.flip()
            pause = True
            evenement = 5

    if face ==4:
        if world[int(positionx/96), int(positiony/90 - 1)] == 15:
            screen.blit(cadre, (0,  int(resolutiony/1.38)))
            pygame.display.flip()
            pause = True
            evenement = 2

        if world[int(positionx/96), int(positiony/90 - 1)] == 16:
            screen.blit(cadre, (0,  int(resolutiony/1.38)))
            pygame.display.flip()
            pause = True
            evenement = 3

        if world[int(positionx/96), int(positiony/90 - 1)] == 17:
            screen.blit(cadre, (0,  int(resolutiony/1.38)))
            pygame.display.flip()
            pause = True
            evenement = 4

        if world[int(positionx/96), int(positiony/90 - 1)] == 18:
            screen.blit(cadre, (0,  int(resolutiony/1.38)))
            pygame.display.flip()
            pause = True
            evenement = 5



    if pause == True:

        time.sleep(0.2)

        if evenement == 2:
            evenementtexte = police.render(("Je suis le dieu Glete noob."),True,pygame.Color("#000000"))
            screen.blit(evenementtexte, (int(resolutionx/64),  int(resolutiony/1.33)))
            pygame.display.flip()
            evenementposition = 1

        if evenement == 3:
            evenementtexte = police.render(("Voulez vous prendre Nuageon"),True,pygame.Color("#000000"))
            evenementtexte2 = police.render(("Echap pour quitter, espace pour confirmer"),True,pygame.Color("#000000"))
            screen.blit(evenementtexte, (int(resolutionx/64),  int(resolutiony/1.33)))
            screen.blit(evenementtexte2, (int(resolutionx/64),  int(resolutiony/1.08)))
            pygame.display.flip()
            evenementposition = 1

        if evenement == 4:
            evenementtexte = police.render(("Voulez vous prendre Poupinus"),True,pygame.Color("#000000"))
            evenementtexte2 = police.render(("Echap pour quitter, espace pour confirmer"),True,pygame.Color("#000000"))
            screen.blit(evenementtexte, (int(resolutionx/64),  int(resolutiony/1.33)))
            screen.blit(evenementtexte2, (int(resolutionx/64),  int(resolutiony/1.08)))
            pygame.display.flip()
            evenementposition = 1

        if evenement == 5:
            evenementtexte = police.render(("Voulez vous prendre Pingouinou"),True,pygame.Color("#000000"))
            evenementtexte2 = police.render(("Echap pour quitter, espace pour confirmer"),True,pygame.Color("#000000"))
            screen.blit(evenementtexte, (int(resolutionx/64),  int(resolutiony/1.33)))
            screen.blit(evenementtexte2, (int(resolutionx/64),  int(resolutiony/1.08)))
            pygame.display.flip()
            evenementposition = 1



        while pause == True:

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:

                        if evenementposition == 99:

                            pause = False
                            print(pause)
                            break

                        if evenementposition == 1 and evenement == 2:
                            evenementtexte = police.render(("Va voir ailleurs noob"),True,pygame.Color("#000000"))
                            screen.blit(evenementtexte, (int(resolutionx/64),  int(resolutiony/1.29)))

                            id = random.randint(1, 9999999999999999999999999)
                            initialisationpogle(id, 999, poglemonstats, 6, True, "wow")

                            evenementposition = 99



                            world[17, 17] = 0

                            for x in range(26,36):
                                world[17, x] = 1
                                world[16, x] = 1

                            pygame.display.flip()
                            time.sleep(0.2)

                        if evenementposition == 1 and evenement == 3:
                            evenementtexte = police.render(("Vous prenez Nuageon!"),True,pygame.Color("#000000"))
                            screen.blit(cadre, (0,  int(resolutiony/1.38)))
                            screen.blit(evenementtexte, (int(resolutionx/64),  int(resolutiony/1.33)))

                            evenementposition = 99



                            id = random.randint(1, 9999999999999999999999999)
                            initialisationpogle(id, 1, poglemonstats, 5, True, "wow")

                            poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))




                            poglemonCharge.poglemonMenu( poglemonstats)



                            pygame.display.flip()
                            time.sleep(0.2)



                        if evenementposition == 1 and evenement == 4:
                            evenementtexte = police.render(("Vous prenez Poupinus!"),True,pygame.Color("#000000"))
                            screen.blit(cadre, (0,  int(resolutiony/1.38)))
                            screen.blit(evenementtexte, (int(resolutionx/64),  int(resolutiony/1.33)))

                            evenementposition = 99

                            world[51, 11] = 0
                            world[49, 11] = 0
                            world[53, 11] = 0

                            id = random.randint(1, 9999999999999999999999999)
                            initialisationpogle(id, 4, poglemonstats, 5, True, "wow")

                            poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))


                            poglemonCharge.poglemonMenu( poglemonstats)



                            pygame.display.flip()
                            time.sleep(0.2)



                        if evenementposition == 1 and evenement == 5:
                            evenementtexte = police.render(("Vous prenez Pingouinou!"),True,pygame.Color("#000000"))
                            screen.blit(cadre, (0,  int(resolutiony/1.38)))
                            screen.blit(evenementtexte, (int(resolutionx/64),  int(resolutiony/1.33)))

                            evenementposition = 99

                            world[51, 11] = 0
                            world[49, 11] = 0
                            world[53, 11] = 0

                            id = random.randint(1, 9999999999999999999999999)
                            initialisationpogle(id, 7, poglemonstats, 5, True, "wow")

                            poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))


                            poglemonCharge.poglemonMenu( poglemonstats)



                            pygame.display.flip()
                            time.sleep(0.2)



                    if event.key == pygame.K_ESCAPE and evenement == 3:
                        pause = False
                        print(pause)
                        time.sleep(0.2)
                        break

                    if event.key == pygame.K_ESCAPE and evenement == 4:
                        pause = False
                        print(pause)
                        time.sleep(0.2)
                        break

                    if event.key == pygame.K_ESCAPE and evenement == 5:
                        pause = False
                        print(pause)
                        time.sleep(0.2)
                        break












def initialisationpogle(id, pog, poglemonstats, niveau, nouveau, position):


    hp = int((((statsPog["pog" + "hp" + str(pog)]*2)*niveau)/100) + niveau + 10)
    attaque = int((((statsPog["pog" + "atk" + str(pog)]*2)*niveau)/100) + 5)
    attaquespe = int((((statsPog["pog" + "spatk" + str(pog)]*2)*niveau)/100) + 5)
    defense = int((((statsPog["pog" + "def" + str(pog)]*2)*niveau)/100) + 5)
    defensespe = int((((statsPog["pog" + "spdef" + str(pog)]*2)*niveau)/100) + 5)
    vitesse = int((((statsPog["pog" + "vit" + str(pog)]*2)*niveau)/100) + 5)

    progressionxp = statsPog["pog" + "progressionxp" + str(pog)]

    type1 = statsPog.get("type1" + str(pog))
    type2 = statsPog.get("type2" + str(pog))

    name = statsPog.get("pog" + "name" + str(pog))

    if nouveau == False:
        for x in range(1, 7):
            if statsPog.get("pog" + str(pog) + "attaqueniv" + str(x)) == niveau:
                nouvelleattaque = x
                print("COCHON")
            else:
                nouvelleattaque = None


    if nouveau == True:

        attaqueliste = {}
        num = 1
        for x in range (1,7):

            if statsPog.get("pog" + str(pog) + "attaque" + str(x)) == True:
                if statsPog.get("pog" + str(pog) + "attaqueniv" + str(x)) <= niveau:
                    if num <= 4:
                        attaqueliste[num] = x
                        num +=1
                    elif num == 5:
                        rand = random.randint(1,5)
                        print("rand")
                        print(rand)
                        if rand != 5:
                            attaqueliste[rand] = x


    if progressionxp == 1:
        xpniveau = 0.8*(niveau + 1)*(niveau+1)*(niveau+1) - 0.8*(niveau)*(niveau)*(niveau)

    if progressionxp == 2:
        xpniveau = (niveau + 1)*(niveau+1)*(niveau+1) - (niveau)*(niveau)*(niveau)

    if progressionxp == 3:
        xpniveau = (1.2*(niveau + 1)*(niveau+1)*(niveau+1) - 15*(niveau + 1)*(niveau + 1) + 100*(niveau+1) -140) - (1.2*(niveau)*(niveau)*(niveau) - 15*(niveau)*(niveau) + 100*(niveau) -140)

    if progressionxp == 4:
        xpniveau = 1.25*(niveau + 1)*(niveau+1)*(niveau+1) - 1.25*(niveau)*(niveau)*(niveau)

    if nouveau == True:

        x = 1

        while poglemonstats.get("pog"+str(x)) != None:
            x += 1


            if x>=7:


                x=1

                while poglemonstats.get("pc"+str(x)) != None:
                    x += 1




                poglemonstats["pc" + str(x)] = pog
                poglemonstats["pc" + str(x) + "id"] = id
                poglemonstats["pc" + str(x) + "hp"] = hp
                poglemonstats["pc" + str(x) + "hpActuel"] = hp
                poglemonstats["pc" + str(x) + "xp"] = xpniveau
                poglemonstats["pc" + str(x) + "xpActuel"] = 0
                poglemonstats["pc" + str(x) + "atk"] = attaque
                poglemonstats["pc" + str(x) + "spatk"] = attaquespe
                poglemonstats["pc" + str(x) + "def"] = defense
                poglemonstats["pc" + str(x) + "spdef"] = defensespe
                poglemonstats["pc" + str(x) + "vit"] = vitesse
                poglemonstats["pc" + str(x) + "niv"] = niveau
                poglemonstats["pc" + str(x) + "type1"] = type1
                poglemonstats["pc" + str(x) + "type2"] = type2
                poglemonstats["pc" + str(x) + "name"] = name

                for y in range (1,5):
                    poglemonstats["pc" + str(x) + "attaque" + str(y)] = attaqueliste.get(y)
                    if attaqueliste.get(y) != None:
                        poglemonstats["pc" + str(x) + "attaque" + str(y) ] = str(attaqueliste[y])
                        poglemonstats["pc" + str(x) + "attaque" + str(y) + "nom"] = attaqueID["nom" + str(attaqueliste[y])]
                        poglemonstats["pc" + str(x) + "attaque" + str(y) + "deg"] = attaqueID["degat" + str(attaqueliste[y])]
                        poglemonstats["pc" + str(x) + "attaque" + str(y) + "pp"] = attaqueID["pp" + str(attaqueliste[y])]
                        poglemonstats["pc" + str(x) + "attaque" + str(y) + "pprestant"] = poglemonstats["pc" + str(x) + "attaque" + str(y) + "pp"]
                        poglemonstats["pc" + str(x) + "attaque" + str(y) + "pre"] = attaqueID["precision" + str(attaqueliste[y])]
                        poglemonstats["pc" + str(x) + "attaque" + str(y) + "categorie"] = attaqueID["categorie" + str(attaqueliste[y])]

                break


        if poglemonstats.get("pog"+str(x)) == None:
            poglemonstats["pog" +str(x)] = pog
            poglemonstats["pog" + str(x) + "id"] = id
            poglemonstats["pog"+ str(x) + "hp"] = hp
            poglemonstats["pog"+ str(x) + "hpActuel"] = hp
            poglemonstats["pog"+ str(x) + "xp"] = xpniveau
            poglemonstats["pog"+ str(x) + "xpActuel"] = 0
            poglemonstats["pog"+ str(x) + "atk"] = attaque
            poglemonstats["pog"+ str(x) + "spatk"] = attaquespe
            poglemonstats["pog"+ str(x) + "def"] = defense
            poglemonstats["pog"+ str(x) + "spdef"] = defensespe
            poglemonstats["pog"+ str(x) + "vit"] = vitesse
            poglemonstats["pog"+ str(x) + "niv"] = niveau
            poglemonstats["pog"+ str(x) + "type1"] = type1
            poglemonstats["pog"+ str(x) + "type2"] = type2
            poglemonstats["pog"+ str(x) + "name"] = name

            for y in range (1,5):
                poglemonstats["pog" + str(x) + "attaque" + str(y)] = attaqueliste.get(y)
                if attaqueliste.get(y) != None:
                    poglemonstats["pog" + str(x) + "attaque" + str(y) ] = str(attaqueliste[y])
                    poglemonstats["pog" + str(x) + "attaque" + str(y) + "nom"] = attaqueID["nom" + str(attaqueliste[y])]
                    poglemonstats["pog" + str(x) + "attaque" + str(y) + "deg"] = attaqueID["degat" + str(attaqueliste[y])]
                    poglemonstats["pog" + str(x) + "attaque" + str(y) + "pp"] = attaqueID["pp" + str(attaqueliste[y])]
                    poglemonstats["pog" + str(x) + "attaque" + str(y) + "pprestant"] = poglemonstats["pog" + str(x) + "attaque" + str(y) + "pp"]
                    poglemonstats["pog" + str(x) + "attaque" + str(y) + "pre"] = attaqueID["precision" + str(attaqueliste[y])]
                    poglemonstats["pog" + str(x) + "attaque" + str(y) + "categorie"] = attaqueID["categorie" + str(attaqueliste[y])]
    else:
        poglemonstats[str(position)] = pog
        poglemonstats[str(position) + "id"] = id
        poglemonstats[str(position) + "hp"] = hp
        poglemonstats[str(position) + "xp"] = xpniveau
        poglemonstats[str(position) + "xpActuel"] = 0
        poglemonstats[str(position) + "atk"] = attaque
        poglemonstats[str(position) + "spatk"] = attaquespe
        poglemonstats[str(position) + "def"] = defense
        poglemonstats[str(position) + "spdef"] = defensespe
        poglemonstats[str(position) + "vit"] = vitesse
        poglemonstats[str(position) + "niv"] = niveau
        poglemonstats[str(position) + "type1"] = type1
        poglemonstats[str(position) + "type2"] = type2
        poglemonstats[str(position) + "name"] = name

        if nouvelleattaque != None:
            poglemonstats[str(position) + "attaque" + str(2) ] = str(nouvelleattaque)
            poglemonstats[str(position) + "attaque" + str(2) + "nom"] = attaqueID["nom" + str(nouvelleattaque)]
            poglemonstats[str(position) + "attaque" + str(2) + "deg"] = attaqueID["degat" + str(nouvelleattaque)]
            poglemonstats[str(position) + "attaque" + str(2) + "pp"] = attaqueID["pp" + str(nouvelleattaque)]
            poglemonstats[str(position) + "attaque" + str(2) + "pprestant"] = poglemonstats[str(position) + "attaque" + str(2) + "pp"]
            poglemonstats[str(position) + "attaque" + str(2) + "pre"] = attaqueID["precision" + str(nouvelleattaque)]
            poglemonstats[str(position) + "attaque" + str(2) + "categorie"] = attaqueID["categorie" + str(nouvelleattaque)]







    pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))














def poglemonSauvage(rareté, zone, poglemonstats, pause, positionx, positiony, world, dresseur):

    for x in range(1, 7):

        if poglemonstats.get("pog" + str(x)) != None:
            if poglemonstats.get("pog" + str(x) + "hpActuel") > 0:
                pogCombat = x
                break
            else:
                pogCombat = None
        else:
            pogCombat = None



    pause = True
    print(rareté)

    if pogCombat == None:
        pause = False

    if pogCombat != None:

        épaisseurBarre1 = int(resolutionx/5.19)

        BarreDeVie = pygame.image.load("../textures/BarreDeVie.png")
        BarreDeVie2 = pygame.image.load("../textures/BarreDeVie.png")
        BarreDeXP = pygame.image.load("../textures/BarreDeXP.png")
        BarreVide = pygame.image.load("../textures/BarreDeVieVide.png")
        cadreattaque = pygame.image.load("../textures/cadreattaque.png")

        BarreDeVie = pygame.transform.scale(BarreDeVie, (int(resolutionx/4.8), int(resolutiony/108)))
        BarreDeVie2 = pygame.transform.scale(BarreDeVie2, (int(resolutionx/4.8), int(resolutiony/108)))
        BarreDeXP = pygame.transform.scale(BarreDeXP, (int(resolutionx/4.8), int(resolutiony/108)))
        BarreVide = pygame.transform.scale(BarreVide, (int(resolutionx/4.36), int(resolutiony/36)))
        cadreattaque = pygame.transform.scale(cadreattaque, (int(resolutionx/3.84), int(resolutiony/7.71)))

        screen.blit(cadreCombat, (0,0))
        pygame.display.flip()

        if zone ==2:
            if rareté == 5:
                initialisationpogleSauvage(1, 2, poglemonstats.get("pog" + str(pogCombat)))

            if rareté == 4:
                initialisationpogleSauvage(1, 3, poglemonstats.get("pog" + str(pogCombat)))

            if rareté == 3:
                initialisationpogleSauvage(4, 3, poglemonstats.get("pog" + str(pogCombat)))

            if rareté == 2:
                initialisationpogleSauvage(4, 1, poglemonstats.get("pog" + str(pogCombat)))

            if rareté == 1:
                initialisationpogleSauvage(7, 4, poglemonstats.get("pog" + str(pogCombat)))

        dataCombat = pickle.load( open( "../save/dataCombat", "rb" ))


        hpE = dataCombat.get("hpE")
        hpActuelE = hpE
        attaqueE = dataCombat.get("attaqueE")
        attaquespeE = dataCombat.get("attaquespeE")
        defenseE = dataCombat.get("defenseE")
        defensespeE = dataCombat.get("defensespeE")
        vitesseE = dataCombat.get("vitesseE")
        type1E = dataCombat.get("type1E")
        type2E = dataCombat.get("type2E")
        nameE = dataCombat.get("nameE")
        niveauE = dataCombat.get("niveauE")

        hp = int(poglemonstats.get("pog" + str(pogCombat) + "hp"))
        hpactuel = int(poglemonstats.get("pog" + str(pogCombat) + "hpActuel"))
        xp = int(poglemonstats.get("pog" + str(pogCombat) + "xp"))
        xpactuel = int(poglemonstats.get("pog" + str(pogCombat) + "xpActuel"))
        niveau = int(poglemonstats.get("pog" + str(pogCombat) + "niv"))
        attaque = poglemonstats.get("pog" + str(pogCombat) + "atk")
        attaquespe = poglemonstats.get("pog" + str(pogCombat) + "spatk")
        defense = poglemonstats.get("pog" + str(pogCombat) + "def")
        defensespe = poglemonstats.get("pog" + str(pogCombat) + "spdef")
        vitesse = poglemonstats.get("pog" + str(pogCombat) + "vit")
        niveau = poglemonstats.get("pog" + str(pogCombat) + "niv")




        chargepog8 = pygame.image.load("../textures/chargePog8.png")
        chargepog9 = pygame.image.load("../textures/chargePog9.png")

        BarreDeVie = pygame.transform.scale(BarreDeVie, (int(épaisseurBarre1 * (hpactuel/hp)), int(resolutiony/108)))
        BarreDeVie2 = pygame.transform.scale(BarreDeVie2, (int(épaisseurBarre1 * (hpActuelE/hpE)), int(resolutiony/108)))
        BarreDeXP = pygame.transform.scale(BarreDeXP, (int(épaisseurBarre1 * (xpactuel/xp)), int(resolutiony/108)))
        BarreVide = pygame.transform.scale(BarreVide, (épaisseurBarre1 + int(resolutionx/76.8), int(resolutiony/108)))

        screen.blit(BarreVide, (int(resolutionx/14.77), int(resolutiony/4.91)))
        screen.blit(BarreVide, (int(resolutionx/14.77), int(resolutiony/4.5)))
        screen.blit(BarreVide, (int(resolutionx/1.41), int(resolutiony/2.27)))
        screen.blit(BarreDeVie, (int(resolutionx/13.24), int(resolutiony/4.91)))
        screen.blit(BarreDeXP, (int(resolutionx/13.24), int(resolutiony/4.5)))
        screen.blit(BarreDeVie2, (int(resolutionx/1.4), int(resolutiony/2.27)))
        screen.blit(chargepog8, (int(resolutionx/1.34), int(resolutiony/6.75)))
        screen.blit(chargepog9, (int(resolutionx/8.35), int(resolutiony/3.86)))

        nompog1 = poglemonstats["pog" + str(pogCombat) + "name"]
        textenompog1 =  police3.render(str(nompog1),True,pygame.Color("#000000"))
        textenameE = police3.render(str(nameE),True,pygame.Color("#000000"))
        textenivpog = police3.render("Niv:" + str(niveau),True,pygame.Color("#000000"))
        textenivE = police3.render("Niv:" + str(niveauE),True,pygame.Color("#000000"))
        screen.blit(textenameE, (int(resolutionx/1.39), int(resolutiony/2.57)))
        screen.blit(textenompog1, (int(resolutionx/12.8), int(resolutiony/6.35)))
        screen.blit(textenivpog, (int(resolutionx/4.36), int(resolutiony/6.35)))
        screen.blit(textenivE, (int(resolutionx/1.15), int(resolutiony/2.57)))

        pygame.display.flip()


    pauseattaque = False

    while pause == True:

        screen.blit(cadreCombat, (0,0))

        BarreDeVie = pygame.transform.scale(BarreDeVie, (int(épaisseurBarre1 * (hpactuel/hp)), int(resolutiony/108)))
        BarreDeVie2 = pygame.transform.scale(BarreDeVie2, (int(épaisseurBarre1 * (hpActuelE/hpE)), int(resolutiony/108)))
        BarreDeXP = pygame.image.load("../textures/BarreDeXP.png")
        BarreDeXP = pygame.transform.scale(BarreDeXP, (int(épaisseurBarre1 * (xpactuel/xp)), int(resolutiony/108)))

        screen.blit(BarreVide, (int(resolutionx/14.77), int(resolutiony/4.91)))
        screen.blit(BarreVide, (int(resolutionx/14.77), int(resolutiony/4.5)))
        screen.blit(BarreVide, (int(resolutionx/1.41), int(resolutiony/2.27)))
        screen.blit(BarreDeVie, (int(resolutionx/13.24), int(resolutiony/4.91)))
        screen.blit(BarreDeXP, (int(resolutionx/13.24), int(resolutiony/4.5)))
        screen.blit(BarreDeVie2, (int(resolutionx/1.4), int(resolutiony/2.27)))
        screen.blit(chargepog8, (int(resolutionx/1.34), int(resolutiony/6.75)))
        screen.blit(chargepog9, (int(resolutionx/8.35), int(resolutiony/3.86)))
        screen.blit(textenameE, (int(resolutionx/1.39), int(resolutiony/2.57)))
        screen.blit(textenompog1, (int(resolutionx/12.8), int(resolutiony/6.35)))
        screen.blit(textenivpog, (int(resolutionx/4.36), int(resolutiony/6.35)))
        screen.blit(textenivE, (int(resolutionx/1.15), int(resolutiony/2.57)))


        pygame.display.flip()

        time.sleep(0.1)




        if hpActuelE <= 0:
            pause = False
            print("victoire gg mdr")

            basexp = statsPog.get("pog" + "basexp" + str(dataCombat.get("pogE")))

            xpgagne =(basexp)*(niveauE/7)

            xpactuel = xpactuel + xpgagne

            if xpactuel >= poglemonstats.get("pog" + str(pogCombat) + "xp"):
                xpniv = xpactuel - poglemonstats.get("pog" + str(pogCombat) + "xp")
                xpactuel = poglemonstats.get("pog" + str(pogCombat) + "xp")



            texteVictoire = police3.render("Victoire! " + str(nameE) + " est vaincu!",True,pygame.Color("#000000"))
            screen.blit(texteVictoire, (int(resolutionx/2.82), int(resolutiony/2.04)))

            BarreDeXP = pygame.image.load("../textures/BarreDeXP.png")
            BarreDeXP = pygame.transform.scale(BarreDeXP, (int(épaisseurBarre1 * (xpactuel/xp)), int(resolutiony/108)))
            screen.blit(BarreDeXP, (int(resolutionx/13.24), int(resolutiony/4.5)))

            if xpactuel == poglemonstats.get("pog" + str(pogCombat) + "xp"):
                xpactuel = 0
                niveau += 1
                BarreDeXP = pygame.image.load("../textures/BarreDeXP.png")
                BarreDeXP = pygame.transform.scale(BarreDeXP, (int(épaisseurBarre1 * (xpactuel/xp)), int(resolutiony/108)))
                textenivpog = police3.render("Niv:" + str(niveau),True,pygame.Color("#000000"))



                screen.blit(cadreCombat, (0,0))
                screen.blit(BarreVide, (int(resolutionx/14.77), int(resolutiony/4.91)))
                screen.blit(BarreVide, (int(resolutionx/14.77), int(resolutiony/4.5)))
                screen.blit(BarreVide, (int(resolutionx/1.41), int(resolutiony/2.27)))
                screen.blit(BarreDeVie, (int(resolutionx/13.24), int(resolutiony/4.91)))
                screen.blit(BarreDeXP, (int(resolutionx/13.24), int(resolutiony/4.5)))
                screen.blit(BarreDeVie2, (int(resolutionx/1.4), int(resolutiony/2.27)))
                screen.blit(chargepog8, (int(resolutionx/1.34), int(resolutiony/6.75)))
                screen.blit(chargepog9, (int(resolutionx/8.35), int(resolutiony/3.86)))
                screen.blit(textenameE, (int(resolutionx/1.39), int(resolutiony/2.57)))
                screen.blit(textenompog1, (int(resolutionx/12.8), int(resolutiony/6.35)))
                screen.blit(textenivpog, (int(resolutionx/4.36), int(resolutiony/6.35)))
                screen.blit(textenivE, (int(resolutionx/1.15), int(resolutiony/2.57)))
                screen.blit(texteVictoire, (int(resolutionx/2.82), int(resolutiony/2.04)))

                initialisationpogle(poglemonstats.get("pog" + str(pogCombat) + "id"), poglemonstats.get("pog" + str(pogCombat)), poglemonstats, niveau, False, "pog" + str(pogCombat))

            pygame.display.flip()
            time.sleep(0.1)

            if dresseur == False:

                victoire = True

                while victoire == True:
                    for event in pygame.event.get():

                        if event.type == pygame.KEYDOWN:

                            if event.key == pygame.K_SPACE:

                                poglemonstats["pog" + str(pogCombat) + "hpActuel"] = hpactuel
                                poglemonstats["pog" + str(pogCombat) + "xpActuel"] = xpactuel
                                poglemonstats["pog" + str(pogCombat) + "niv"] = niveau
                                pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))
                                chargement.chargementMap(positionx -resolutionx/2, positiony - resolutiony/2, zone, world)
                                victoire = False
                                break





        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pause = False
                    poglemonstats["pog" + str(pogCombat) + "hpActuel"] = hpactuel
                    poglemonstats["pog" + str(pogCombat) + "niv"] = niveau
                    poglemonstats["pog" + str(pogCombat) + "xpActuel"] = xpactuel
                    chargement.chargementMap(positionx - resolutionx/2, positiony - resolutiony/2, zone, world)
                    time.sleep(0.1)
                    break



                if event.key == pygame.K_SPACE:

                    pauseattaque = True

                    posxcadre = int(resolutionx/25.26)
                    posycadre = int(resolutiony/1.61)

                    positionCadre = 1

                    texteattaquelistenom = {}
                    texteattaquelistedeg = {}
                    texteattaquelistepp = {}
                    texteattaquelistepprestant = {}
                    texteattaquelistepre = {}
                    texteattaquelistecategorie = {}

                    for x in range(1,5):
                        if poglemonstats.get("pog" + str(pogCombat) + "attaque" + str(x)) != None:
                            attaquelistenom = poglemonstats.get("pog" + str(pogCombat) + "attaque" + str(x) + "nom")
                            attaquelistedeg = poglemonstats.get("pog" + str(pogCombat) + "attaque" + str(x) + "deg")
                            attaquelistepp = poglemonstats.get("pog" + str(pogCombat) + "attaque" + str(x) + "pp")
                            attaquelistepprestant = poglemonstats.get("pog" + str(pogCombat) + "attaque" + str(x) + "pprestant")
                            attaquelistepre = poglemonstats.get("pog" + str(pogCombat) + "attaque" + str(x) + "pre")
                            attaquelistecategorie = poglemonstats.get("pog" + str(pogCombat) + "attaque" + str(x) + "categorie")

                            texteattaquelistenom[x] = police5.render((str(attaquelistenom)),True,pygame.Color("#000000"))
                            texteattaquelistedeg[x] = police4.render(("Deg: " + str(attaquelistedeg)),True,pygame.Color("#000000"))
                            texteattaquelistepprestant[x] = police4.render((str(attaquelistepprestant) + "/" + str(attaquelistepp)),True,pygame.Color("#000000"))
                            texteattaquelistepre[x] = police4.render(("Pre: " + str(attaquelistepre)),True,pygame.Color("#000000"))

                            if attaquelistecategorie == "physique":
                                texteattaquelistecategorie[x] = police4.render(("PHY"),True,pygame.Color("#000000"))
                            else:
                                texteattaquelistecategorie[x] = police4.render(("SPE"),True,pygame.Color("#000000"))



                    while pauseattaque == True:

                        if hpActuelE == 0:
                            break

                        screen.blit(cadreCombat2, (0,0))
                        screen.blit(cadreattaque, (posxcadre, posycadre))

                        BarreDeVie = pygame.transform.scale(BarreDeVie, (int(épaisseurBarre1 * (hpactuel/hp)), int(resolutiony/108)))
                        BarreDeVie2 = pygame.transform.scale(BarreDeVie2, (int(épaisseurBarre1 * (hpActuelE/hpE)), int(resolutiony/108)))
                        BarreDeXP = pygame.image.load("../textures/BarreDeXP.png")
                        BarreDeXP = pygame.transform.scale(BarreDeXP, (int(épaisseurBarre1 * (xpactuel/xp)), int(resolutiony/108)))

                        screen.blit(BarreVide, (int(resolutionx/14.77), int(resolutiony/4.91)))
                        screen.blit(BarreVide, (int(resolutionx/14.77), int(resolutiony/4.5)))
                        screen.blit(BarreVide, (int(resolutionx/1.41), int(resolutiony/2.27)))
                        screen.blit(BarreDeVie, (int(resolutionx/13.24), int(resolutiony/4.91)))
                        screen.blit(BarreDeXP, (int(resolutionx/13.24), int(resolutiony/4.5)))
                        screen.blit(BarreDeVie2, (int(resolutionx/1.4), int(resolutiony/2.27)))
                        screen.blit(chargepog8, (int(resolutionx/1.34), int(resolutiony/6.75)))
                        screen.blit(chargepog9, (int(resolutionx/8.35), int(resolutiony/3.86)))
                        screen.blit(textenameE, (int(resolutionx/1.39), int(resolutiony/2.57)))
                        screen.blit(textenompog1, (int(resolutionx/12.8), int(resolutiony/6.35)))
                        screen.blit(textenivpog, (int(resolutionx/4.36), int(resolutiony/6.35)))
                        screen.blit(textenivE, (int(resolutionx/1.15), int(resolutiony/2.57)))

                        if poglemonstats.get("pog" + str(pogCombat) + "attaque" + "1") != None:
                            screen.blit(texteattaquelistenom[1], (int(resolutionx/18.29), int(resolutiony/1.55)))
                            screen.blit(texteattaquelistedeg[1], (int(resolutionx/4.46), int(resolutiony/1.55)))
                            screen.blit(texteattaquelistepre[1], (int(resolutionx/4.46), int(resolutiony/1.42)))
                            screen.blit(texteattaquelistepprestant[1], (int(resolutionx/18.29), int(resolutiony/1.42)))
                            screen.blit(texteattaquelistecategorie[1], (int(resolutionx/7), int(resolutiony/1.42)))

                        if poglemonstats.get("pog" + str(pogCombat) + "attaque" + "2") != None:
                            screen.blit(texteattaquelistenom[2], (int(resolutionx/1.44), int(resolutiony/1.55)))
                            screen.blit(texteattaquelistedeg[2], (int(resolutionx/1.17), int(resolutiony/1.55)))
                            screen.blit(texteattaquelistepre[2], (int(resolutionx/1.17), int(resolutiony/1.42)))
                            screen.blit(texteattaquelistepprestant[2], (int(resolutionx/1.44), int(resolutiony/1.42)))
                            screen.blit(texteattaquelistecategorie[2], (int(resolutionx/1.28), int(resolutiony/1.42)))

                        if poglemonstats.get("pog" + str(pogCombat) + "attaque" + "3") != None:
                            screen.blit(texteattaquelistenom[3], (int(resolutionx/18.29), int(resolutiony/1.27)))
                            screen.blit(texteattaquelistedeg[3], (int(resolutionx/4.46), int(resolutiony/1.27)))
                            screen.blit(texteattaquelistepre[3], (int(resolutionx/4.46), int(resolutiony/1.18)))
                            screen.blit(texteattaquelistepprestant[3], (int(resolutionx/18.29), int(resolutiony/1.18)))
                            screen.blit(texteattaquelistecategorie[3], (int(resolutionx/7), int(resolutiony/1.18)))

                        if poglemonstats.get("pog" + str(pogCombat) + "attaque" + "4") != None:
                            screen.blit(texteattaquelistenom[4], (int(resolutionx/1.44), int(resolutiony/1.27)))
                            screen.blit(texteattaquelistedeg[4], (int(resolutionx/1.17), int(resolutiony/1.27)))
                            screen.blit(texteattaquelistepre[4], (int(resolutionx/1.17), int(resolutiony/1.18)))
                            screen.blit(texteattaquelistepprestant[4], (int(resolutionx/1.44), int(resolutiony/1.18)))
                            screen.blit(texteattaquelistecategorie[4], (int(resolutionx/1.28), int(resolutiony/1.18)))

                        pygame.display.flip()

                        time.sleep(0.2)

                        for event in pygame.event.get():

                            if event.type == pygame.KEYDOWN:
                                print("porg")

                                if event.key == pygame.K_s and posycadre >= (int(resolutiony/1.61) + int(resolutiony/6.97)):
                                    posxcadre = int(resolutionx/2.74)
                                    posycadre = int(resolutiony/1.17)

                                if event.key == pygame.K_d and posxcadre != (int(resolutionx/1.56) + int(resolutionx/25.26))  and posxcadre != int(resolutionx/2.74):
                                    posxcadre += int(resolutionx/1.56)
                                    positionCadre += 1

                                if event.key == pygame.K_a and posxcadre != int(resolutionx/25.26) and posxcadre != int(resolutionx/2.74):
                                    posxcadre -= int(resolutionx/1.56)
                                    positionCadre -= 1

                                if event.key == pygame.K_w and posycadre != int(resolutiony/1.61) and posycadre != int(resolutiony/1.17):
                                    posycadre -= int(resolutiony/6.97)
                                    positionCadre -= 2

                                if event.key == pygame.K_s and posycadre != (int(resolutiony/1.61) + int(resolutiony/6.97)) and posycadre != int(resolutiony/1.17):
                                    posycadre += int(resolutiony/6.97)
                                    positionCadre += 2

                                if event.key == pygame.K_w and posycadre == int(resolutiony/1.17):
                                    posxcadre = int(resolutionx/25.26)
                                    posycadre = (int(resolutiony/1.61) + int(resolutiony/6.97))
                                    positionCadre = 3

                                if event.key == pygame.K_SPACE and posxcadre == int(resolutionx/2.74) or event.key == pygame.K_ESCAPE:
                                    pauseattaque = False
                                    break

                                if event.key == pygame.K_SPACE and posxcadre != int(resolutionx/2.74) and poglemonstats.get("pog" + str(pogCombat) + "attaque" + str(positionCadre)) != None and poglemonstats.get("pog" + str(pogCombat) + "attaque" + str(positionCadre) + "pprestant") > 0:

                                    attaqueUtilise = poglemonstats.get("pog" + str(pogCombat) + "attaque" + str(positionCadre))
                                    attaqueUtiliseNom = poglemonstats.get("pog" + str(pogCombat) + "attaque" + str(positionCadre) + "nom")
                                    attaqueUtiliseDeg = poglemonstats.get("pog" + str(pogCombat) + "attaque" + str(positionCadre) + "deg")
                                    attaqueUtilisePPrestant = poglemonstats.get("pog" + str(pogCombat) + "attaque" + str(positionCadre) + "pprestant")
                                    attaqueUtilisePre = poglemonstats.get("pog" + str(pogCombat) + "attaque" + str(positionCadre) + "pre")

                                    poglemonstats["pog" + str(pogCombat) + "attaque" + str(positionCadre) + "pprestant"] -= 1

                                    if attaqueID.get("categorie" + str(positionCadre)) == "physique":
                                        attaquecat = attaque
                                    else:
                                        attaquecat = attaquespe


                                    if vitesse >= vitesseE:
                                        rand = random.randint(0,100)
                                        print(rand)

                                        if rand <= attaqueUtilisePre:
                                            print("reussiteAttaque")

                                            texteAttaque = police3.render((str(nompog1) + " utilise " + str(attaqueUtiliseNom)),True,pygame.Color("#000000"))
                                            screen.blit(texteAttaque, (int(resolutionx/2.82), int(resolutiony/2.04)))
                                            pygame.display.flip()
                                            time.sleep(0.2)

                                            degat = int((((niveau*0.4+2)*attaquecat*attaqueUtiliseDeg)/(defenseE*50))+2)
                                            print("degat"+str(degat))
                                            hpActuelE = hpActuelE - degat

                                            if hpActuelE <= 0:
                                                hpActuelE = 0

                                        else:
                                            print("attaqueRaté(cheh)")
                                            texteAttaque = police3.render((str(nompog1) + " rate l'attaque!"),True,pygame.Color("#000000"))
                                            screen.blit(texteAttaque, (int(resolutionx/2.82), int(resolutiony/2.04)))
                                            pygame.display.flip()
                                            time.sleep(0.2)


                                    screen.blit(cadreCombat, (0,0))
                                    screen.blit(BarreVide, (int(resolutionx/14.77), int(resolutiony/4.91)))
                                    screen.blit(BarreVide, (int(resolutionx/14.77), int(resolutiony/4.5)))
                                    screen.blit(BarreVide, (int(resolutionx/1.41), int(resolutiony/2.27)))
                                    screen.blit(BarreDeVie, (int(resolutionx/13.24), int(resolutiony/4.91)))
                                    screen.blit(BarreDeXP, (int(resolutionx/13.24), int(resolutiony/4.5)))
                                    screen.blit(BarreDeVie2, (int(resolutionx/1.4), int(resolutiony/2.27)))
                                    screen.blit(chargepog8, (int(resolutionx/1.34), int(resolutiony/6.75)))
                                    screen.blit(chargepog9, (int(resolutionx/8.35), int(resolutiony/3.86)))
                                    screen.blit(textenameE, (int(resolutionx/1.39), int(resolutiony/2.57)))
                                    screen.blit(textenompog1, (int(resolutionx/12.8), int(resolutiony/6.35)))
                                    screen.blit(textenivpog, (int(resolutionx/4.36), int(resolutiony/6.35)))
                                    screen.blit(textenivE, (int(resolutionx/1.15), int(resolutiony/2.57)))
                                    time.sleep(0.3)



                                    if hpActuelE > 0:
                                        for y in range(1, 5):

                                            if dataCombat.get("attaqueE" + str(y)) != None:
                                                nombreAttaque = y

                                        randattaque = random.randint(1, nombreAttaque)

                                        rand = random.randint(0,100)

                                        while dataCombat["attaqueE" + str(randattaque) + "pprestant"] == 0:
                                            if randattaque > 1:
                                                randattaque -=1
                                            else:
                                                for x in range(1, 5):
                                                    if dataCombat.get("attaqueE" + str(x)) != None:
                                                        randattaque = x

                                        dataCombat["attaqueE" + str(randattaque) + "pprestant"] -=1

                                        if attaqueID.get("categorie" + str(randattaque)) == "physique":
                                            attaqueEcat = attaqueE
                                        else:
                                            attaqueEcat = attaquespeE


                                        if rand <= dataCombat["attaqueE" + str(randattaque) + "pre"]:
                                            print("ennemi attaque")

                                            texteAttaque = police3.render((str(nameE) + " utilise " + str(dataCombat["attaqueE" + str(randattaque) + "nom"])),True,pygame.Color("#000000"))
                                            screen.blit(texteAttaque, (int(resolutionx/2.82), int(resolutiony/2.04)))
                                            pygame.display.flip()
                                            time.sleep(0.5)

                                            degatAttaque = dataCombat.get("attaqueE" + str(randattaque) + "deg")
                                            print("attaqueE" + str(dataCombat.get("attaqueE" + str(randattaque) + "nom")))

                                            degatE = int((((niveauE*0.4+2)*attaqueEcat*degatAttaque)/(defense*50))+2)

                                            hpactuel = hpactuel - degatE

                                            if hpactuel <=0:
                                                hpactuel = 0
                                                pauseattaque = False
                                                pause = False
                                                poglemonstats["pog" + str(pogCombat) + "hpActuel"] = hpactuel
                                                poglemonstats["pog" + str(pogCombat) + "xpActuel"] = xpactuel
                                                poglemonstats["pog" + str(pogCombat) + "niv"] = niveau
                                                pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))
                                                chargement.chargementMap(positionx -resolutionx/2, positiony - resolutiony/2, zone, world)
                                                break
                                        else:
                                            print("ennemi rate")
                                            texteAttaque = police3.render((str(nameE) + " rate son attaque!" ),True,pygame.Color("#000000"))
                                            screen.blit(texteAttaque, (int(resolutionx/2.82), int(resolutiony/2.04)))
                                            pygame.display.flip()
                                            time.sleep(0.5)

                                    if vitesse < vitesseE:
                                        rand = random.randint(0,100)
                                        print(rand)

                                        if rand <= attaqueUtilisePre:
                                            print("reussiteAttaque")

                                            texteAttaque = police3.render((str(nompog1) + " utilise " + str(attaqueUtiliseNom),True,pygame.Color("#000000")))
                                            screen.blit(texteAttaque, (int(resolutionx/2.82), int(resolutiony/2.04)))
                                            pygame.display.flip()
                                            time.sleep(0.2)

                                            degat = int((((niveau*0.4+2)*attaquecat*attaqueUtiliseDeg)/(defenseE*50))+2)
                                            print("degat"+str(degat))
                                            hpActuelE = hpActuelE - degat

                                            if hpActuelE <= 0:
                                                hpActuelE = 0

                                        else:
                                            print("attaqueRaté(cheh)")
                                            texteAttaque = police3.render((str(nompog1) + " rate l'attaque!"),True,pygame.Color("#000000"))
                                            screen.blit(texteAttaque, (int(resolutionx/2.82), int(resolutiony/2.04)))
                                            pygame.display.flip()
                                            time.sleep(0.2)



                                    pauseattaque = False
                                    time.sleep(0.1)
                                    break















def initialisationpogleSauvage(pog, niveau, pog1):

    hpE = int((((statsPog["pog" + "hp" + str(pog)]*2)*niveau)/100) + niveau + 10)
    attaqueE = int((((statsPog["pog" + "atk" + str(pog)]*2)*niveau)/100) + 5)
    attaquespeE = int((((statsPog["pog" + "spatk" + str(pog)]*2)*niveau)/100) + 5)
    defenseE = int((((statsPog["pog" + "def" + str(pog)]*2)*niveau)/100) + 5)
    defensespeE = int((((statsPog["pog" + "spdef" + str(pog)]*2)*niveau)/100) + 5)
    vitesseE = int((((statsPog["pog" + "vit" + str(pog)]*2)*niveau)/100) + 5)

    type1E = statsPog.get("type1" + str(pog))
    type2E = statsPog.get("type2" + str(pog))

    nameE = statsPog.get("pog" + "name" + str(pog))

    attaqueliste = {}
    num = 1
    for x in range (1,7):

        if statsPog.get("pog" + str(pog) + "attaque" + str(x)) == True:
            if statsPog.get("pog" + str(pog) + "attaqueniv" + str(x)) <= niveau:
                if num <= 4:
                    attaqueliste[num] = x
                    num +=1
                elif num == 5:
                    rand = random.randint(1,5)
                    print("rand")
                    print(rand)
                    if rand != 5:
                        attaqueliste[rand] = x

    dataCombat= {}
    dataCombat["pogE"] = pog
    dataCombat["hpE"] = hpE
    dataCombat["attaqueE"] = attaqueE
    dataCombat["attaquespeE"] = attaquespeE
    dataCombat["defenseE"] = defenseE
    dataCombat["defensespeE"] = defensespeE
    dataCombat["vitesseE"] = vitesseE
    dataCombat["type1E"] = type1E
    dataCombat["type2E"] = type2E
    dataCombat["nameE"] = nameE
    dataCombat["niveauE"] = niveau

    for y in range (1,5):
        if attaqueliste.get(y) != None:
            dataCombat["attaqueE" + str(y) ] = str(attaqueliste[y])
            dataCombat["attaqueE" + str(y) + "nom"] = attaqueID["nom" + str(attaqueliste[y])]
            dataCombat["attaqueE" + str(y) + "deg"] = attaqueID["degat" + str(attaqueliste[y])]
            dataCombat["attaqueE" + str(y) + "pp"] = attaqueID["pp" + str(attaqueliste[y])]
            dataCombat["attaqueE" + str(y) + "pprestant"] = dataCombat["attaqueE" + str(y) + "pp"]
            dataCombat["attaqueE" + str(y) + "pre"] = attaqueID["precision" + str(attaqueliste[y])]



    pickle.dump(dataCombat, open( "../save/dataCombat", "wb" ))

    poglemonCharge.poglemonCombat(pog, pog1)
