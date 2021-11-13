import pygame, numpy, time, pickle, os

import poglemonCharge
import chargement
import echangePogle
import statsPog

from pygame.locals import *

menu = pygame.image.load("../textures/cadreBoitePC.png")
cadreMenuPC = pygame.image.load("../textures/cadreMenuPC.png")
cadreMenuPCselection = pygame.image.load("../textures/cadreMenuPCselection.png")
cadreTexte2 = pygame.image.load("../textures/cadreTexte2.png")
cadrePogle = pygame.image.load("../textures/cadrePogle.png")
cadreBoite = pygame.image.load("../textures/cadreBoite.png")



def start():

    global menu, cadreMenuPC, cadreMenuPCselection, cadreTexte2, cadrePogle, cadreBoite, resolutionx, resolutiony, screen, police ,police1 ,police2 ,police3 ,police4, positionCadreX, positionCadreY, listeco


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

    menu = pygame.image.load("../textures/cadreBoitePC.png")
    cadreMenuPC = pygame.image.load("../textures/cadreMenuPC.png")
    cadreMenuPCselection = pygame.image.load("../textures/cadreMenuPCselection.png")
    cadreTexte2 = pygame.image.load("../textures/cadreTexte2.png")
    cadrePogle = pygame.image.load("../textures/cadrePogle.png")
    cadreBoite = pygame.image.load("../textures/cadreBoite.png")

    menu = pygame.transform.scale(menu, (resolutionx, resolutiony))
    cadreMenuPC = pygame.transform.scale(cadreMenuPC, (int(resolutionx/5.05), int(resolutiony/1.96)))
    cadreMenuPCselection = pygame.transform.scale(cadreMenuPCselection, (int(resolutionx/5.65), int(resolutiony/9)))
    cadreTexte2 = pygame.transform.scale(cadreTexte2, (int(resolutionx/2.4), int(resolutiony/3.09)))
    cadrePogle = pygame.transform.scale(cadrePogle, (resolutionx, resolutiony))
    cadreBoite = pygame.transform.scale(cadreBoite, (int(resolutionx/10.67), int(resolutiony/6)))


    police1 = pygame.font.Font(None,int(resolutionx/19.2))
    police = pygame.font.Font(None,int(resolutionx/19.2))
    police2 = pygame.font.Font(None,int(resolutionx/9.6))
    police4 = pygame.font.Font(None,int(resolutionx/25.6))
    police3 = pygame.font.Font(None,int(resolutionx/42.67))

    listeco = {}
    listeco[1] = int(resolutionx/4.8), int(resolutiony/6)
    listeco[2] = int(resolutionx/1.43), int(resolutiony/6)
    listeco[3] = int(resolutionx/4.8), int(resolutiony/2.1)
    listeco[4] = int(resolutionx/1.43), int(resolutiony/2.1)
    listeco[5] = int(resolutionx/4.8), int(resolutiony/1.27)
    listeco[6] = int(resolutionx/1.43), int(resolutiony/1.27)

    positionCadreX = int(resolutionx/10.38)
    positionCadreY = int(resolutiony/5.4)


numeroBoite = 1
emplacementBoite = 1


#Menu du PC

def chargementPc(poglemonstats, pause):

    global positionCadreX, positionCadreY, numeroBoite, emplacementBoite
    screen.blit(menu, (0,0))

    while pause == True:


        texteBoite = police2.render(("Boite " + str(numeroBoite)),True,pygame.Color("#000000"))


        screen.blit(texteBoite, (int(resolutionx/2.74), int(resolutiony/21.6)))

        screen.blit(cadreBoite,(positionCadreX, positionCadreY))

        poglemonCharge.poglemonPcMenu(numeroBoite, poglemonstats)

        pygame.display.flip()
        screen.blit(menu, (0,0))
        time.sleep(0.1)

        poglemonCharge.poglemonPcMenu(numeroBoite, poglemonstats)


        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))
                    pause = False
                    break

                if event.key == pygame.K_SPACE and poglemonstats.get("pc" + str(emplacementBoite)) != None:


                    if positionCadreX <= resolutionx/2:
                        if positionCadreY <= int(resolutiony/2.45):

                            difference = 0
                        else:
                            difference = -int(resolutiony/2.7)

                        screen.blit(cadreMenuPC, (positionCadreX + int(resolutionx/7.1), positionCadreY + difference))

                        texteMenuPC = police.render(("Résumé"),True,pygame.Color("#000000"))
                        screen.blit(texteMenuPC, (positionCadreX + int(resolutionx/6.4), positionCadreY + int(resolutiony/27) + difference))

                        texteMenuPC2 = police.render(("Retirer"),True,pygame.Color("#000000"))
                        screen.blit(texteMenuPC2, (positionCadreX + int(resolutionx/6.4), positionCadreY + int(resolutiony/7.71) + difference))

                        texteMenuPC3 = police.render(("Quitter"),True,pygame.Color("#000000"))
                        screen.blit(texteMenuPC3, (positionCadreX + int(resolutionx/6.4), positionCadreY + int(resolutiony/2.45) + difference))

                        texteMenuPC4 = police.render(("Deplacer"),True,pygame.Color("#000000"))
                        screen.blit(texteMenuPC4, (positionCadreX + int(resolutionx/6.4), positionCadreY + int(resolutiony/4.5) + difference))

                        screen.blit(texteBoite, (int(resolutionx/2.74), int(resolutiony/21.6)))


                        pygame.display.flip()



                        positionCadreX2 = positionCadreX + int(resolutionx/6.62)
                        positionCadreY2 = positionCadreY + int(resolutiony/72) + difference
                    else:
                        if positionCadreY <= int(resolutiony/2.45):
                            difference = 0
                        else:
                            difference = -int(resolutiony/2.7)

                        screen.blit(cadreMenuPC, (positionCadreX - int(resolutionx/5.82), positionCadreY + difference))

                        texteMenuPC = police.render(("Résumé"),True,pygame.Color("#000000"))
                        screen.blit(texteMenuPC, (positionCadreX - int(resolutionx/6.4), positionCadreY + int(resolutiony/27) + difference))

                        texteMenuPC2 = police.render(("Retirer"),True,pygame.Color("#000000"))
                        screen.blit(texteMenuPC2, (positionCadreX - int(resolutionx/6.4), positionCadreY + int(resolutiony/7.71) + difference))

                        texteMenuPC3 = police.render(("Quitter"),True,pygame.Color("#000000"))
                        screen.blit(texteMenuPC3, (positionCadreX - int(resolutionx/6.4), positionCadreY + int(resolutiony/2.45) + difference))

                        texteMenuPC4 = police.render(("Deplacer"),True,pygame.Color("#000000"))
                        screen.blit(texteMenuPC4, (positionCadreX - int(resolutionx/6.4), positionCadreY + int(resolutiony/4.5) + difference))

                        screen.blit(texteBoite, (int(resolutionx/2.74), int(resolutiony/21.6)))

                        pygame.display.flip()



                        positionCadreX2 = positionCadreX - int(resolutionx/6.19)
                        positionCadreY2 = positionCadreY + difference + int(resolutiony/72)

                    screen.blit(cadreMenuPCselection, (positionCadreX2, positionCadreY2))

                    pause2 = True

                    while pause2 == True:

                        if positionCadreX <= resolutionx/2:
                            if positionCadreY <= int(resolutiony/2.45):
                                difference = 0
                            else:
                                difference = -int(resolutiony/2.7)

                            screen.blit(texteMenuPC, (positionCadreX + int(resolutionx/6.4), positionCadreY + int(resolutiony/27) + difference))
                            screen.blit(texteMenuPC2, (positionCadreX + int(resolutionx/6.4), positionCadreY + int(resolutiony/7.71) + difference))
                            screen.blit(texteMenuPC3, (positionCadreX + int(resolutionx/6.4), positionCadreY + int(resolutiony/2.45) + difference))
                            screen.blit(texteMenuPC4, (positionCadreX + int(resolutionx/6.4), positionCadreY + int(resolutiony/4.5) + difference))

                            pygame.display.flip()
                            screen.blit(cadreMenuPC, (positionCadreX + int(resolutionx/7.1), positionCadreY + difference))
                        else:
                            if positionCadreY <= int(resolutiony/2.45):
                                difference = 0
                            else:
                                difference = -int(resolutiony/2.7)

                            screen.blit(texteMenuPC, (positionCadreX - int(resolutionx/6.4), positionCadreY + int(resolutiony/27) + difference))
                            screen.blit(texteMenuPC2, (positionCadreX - int(resolutionx/6.4), positionCadreY + int(resolutiony/7.71) + difference))
                            screen.blit(texteMenuPC3, (positionCadreX - int(resolutionx/6.4), positionCadreY + int(resolutiony/2.45) + difference))
                            screen.blit(texteMenuPC4, (positionCadreX - int(resolutionx/6.4), positionCadreY + int(resolutiony/4.5) + difference))
                            pygame.display.flip()
                            screen.blit(cadreMenuPC, (positionCadreX - int(resolutionx/5.82), positionCadreY + difference))

                        screen.blit(texteBoite, (int(resolutionx/2.74), int(resolutiony/21.6)))
                        screen.blit(cadreMenuPCselection, (positionCadreX2, positionCadreY2))

                        time.sleep(0.1)

                        for event in pygame.event.get():

                            if event.type == pygame.KEYDOWN:

                                if event.key == pygame.K_s and positionCadreY2 != positionCadreY + int(resolutiony/72) + difference + 4*int(resolutiony/10.8):
                                    positionCadreY2 += int(resolutiony/10.8)

                                if event.key == pygame.K_w and positionCadreY2 != positionCadreY + int(resolutiony/72) + difference:
                                    positionCadreY2 -= int(resolutiony/10.8)

                                if event.key == pygame.K_ESCAPE:
                                    pause2 = False
                                    break

                                if event.key == pygame.K_SPACE:

                                    if positionCadreY2 == positionCadreY+ int(resolutiony/72) + difference:

                                        statsPog.statsPog(emplacementBoite, pause, poglemonstats, "pc")
                                        screen.blit(menu, (0,0))

                                        poglemonCharge.poglemonPcMenu(numeroBoite, poglemonstats)

                                    if positionCadreY2 == positionCadreY + int(resolutiony/72) + 4*int(resolutiony/10.8) + difference:
                                        pause2 = False
                                        time.sleep(0.2)
                                        break

                                    if positionCadreY2 == positionCadreY + int(resolutiony/72) + int(resolutiony/10.8) + difference:
                                        echangepogle(emplacementBoite, pause, poglemonstats, numeroBoite)
                                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))

                                        pause2 = False
                                        break

                                    if positionCadreY2 == positionCadreY + int(resolutiony/72) + 2*int(resolutiony/10.8) + difference:
                                        deplacementPogle(emplacementBoite, poglemonstats, positionCadreX, positionCadreY, numeroBoite)
                                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))
                                        pause2 = False
                                        break




                if event.key == pygame.K_d and positionCadreX != int(resolutionx/10.38) + 5*int(resolutionx/7.11):
                    positionCadreX += int(resolutionx/7.11)
                    emplacementBoite += 1
                    print(emplacementBoite)

                if event.key == pygame.K_a and positionCadreX != int(resolutionx/10.38):
                    positionCadreX -= int(resolutionx/7.11)
                    emplacementBoite -= 1
                    print(emplacementBoite)

                if event.key == pygame.K_s and positionCadreY != int(resolutiony/5.4) + 4*int(resolutiony/6.35):
                    positionCadreY += int(resolutiony/6.35)
                    emplacementBoite += 6
                    print(emplacementBoite)

                if event.key == pygame.K_w and positionCadreY != int(resolutiony/5.4):
                    positionCadreY -= int(resolutiony/6.35)
                    emplacementBoite -= 6
                    print(emplacementBoite)

                if event.key == pygame.K_e and numeroBoite <= 31:
                    numeroBoite += 1
                    emplacementBoite += 30
                    print(emplacementBoite)

                if event.key == pygame.K_q and numeroBoite >= 2:
                    numeroBoite -= 1
                    emplacementBoite -= 30
                    print(emplacementBoite)




#Retirer un Pogle


def echangepogle(numeroPog, pause, poglemonstats, numeroBoite):




    if poglemonstats.get("pog1") == None:
        pogchangeequipe = 1
    elif poglemonstats.get("pog2") == None:
        pogchangeequipe = 2
    elif poglemonstats.get("pog3") == None:
        pogchangeequipe = 3
    elif poglemonstats.get("pog4") == None:
        pogchangeequipe = 4
    elif poglemonstats.get("pog5") == None:
        pogchangeequipe = 5
    elif poglemonstats.get("pog6") == None:
        pogchangeequipe = 6
    else:

        positionxcadre = int(resolutionx/64)
        positionycadre = int(resolutiony/54)

        emplacementMenu = 1


        screen.blit(cadreTexte2, (positionxcadre, positionycadre))

        poglemonCharge.poglemonMenu(poglemonstats)
        chargepog = {}

        for x in range(1, 7):

            chargepog[x] = pygame.image.load("../textures/chargePog" + str(x) + ".png")
            chargepog[x] = pygame.transform.scale(chargepog[x], (int(resolutionx/9.9), int(resolutiony/5.77)))

        hp ={}
        hpactuel ={}
        xp ={}
        xpactuel ={}
        niveau = {}
        name = {}
        BarreDeVie = {}
        BarreDeXp = {}
        texteNiveau = {}
        texteName = {}
        texteVie = {}

        BarreDeVieVide = pygame.image.load("../textures/BarreDeVieVide.png")
        BarreDeVieVide = pygame.transform.scale(BarreDeVieVide, (int(resolutionx/6.19), int(resolutiony/108)))

        x = 1

        for x in range (1, 7):

            if poglemonstats.get("pog" + str(x)) != None:

                hp[x] = int(poglemonstats.get("pog" + str(x) + "hp"))
                hpactuel[x] = int(poglemonstats.get("pog" + str(x) + "hpActuel"))
                xp[x] = int(poglemonstats.get("pog" + str(x) + "xp"))
                xpactuel[x] = int(poglemonstats.get("pog" + str(x) + "xpActuel"))
                niveau[x] = int(poglemonstats.get("pog" + str(x) + "niv"))
                name[x] = str(poglemonstats.get("pog" + str(x) + "name"))

                BarreDeVie[x] = pygame.image.load("../textures/BarreDeVie.png")
                BarreDeXp[x] = pygame.image.load("../textures/BarreDeXP.png")

                texteNiveau[x] = police4.render("Niveau:" + (str(niveau[x])),True,pygame.Color("#000000"))
                texteName[x] = police4.render((str(name[x])),True,pygame.Color("#000000"))
                texteVie[x] = police4.render((str(hpactuel[x]) + "/" + str(hp[x])),True,pygame.Color("#000000"))
                BarreDeVie[x] = pygame.transform.scale(BarreDeVie[x], (int(int(resolutionx/6.4) * (hpactuel[x]/hp[x])), int(resolutiony/108)))
                BarreDeXp[x] = pygame.transform.scale(BarreDeXp[x], (int(int(resolutionx/6.4) * (xpactuel[x]/xp[x])), int(resolutiony/108)))

        screen.blit(cadrePogle, (0, 0))
        screen.blit(cadreTexte2, (positionxcadre, positionycadre))


        pygame.display.flip()

        pause3 = True

        while pause3 == True:
            screen.blit(cadrePogle, (0, 0))
            screen.blit(cadreTexte2, (positionxcadre, positionycadre))

            screen.blit(chargepog[1], (int(resolutionx/19.2), int(resolutiony/8)))
            screen.blit(chargepog[2], (int(resolutionx/1.85), int(resolutiony/8)))
            screen.blit(chargepog[3], (int(resolutionx/19.2), int(resolutiony/2.3)))
            screen.blit(chargepog[4], (int(resolutionx/1.85), int(resolutiony/2.3)))
            screen.blit(chargepog[5], (int(resolutionx/19.2), int(resolutiony/1.34)))
            screen.blit(chargepog[6], (int(resolutionx/1.85), int(resolutiony/1.34)))

            for pogactuel in range(7):
                if poglemonstats.get("pog" + str(pogactuel)) !=None:

                    cox, coy = listeco[pogactuel]
                    screen.blit(BarreDeVieVide, (cox, coy))
                    screen.blit(BarreDeVie[pogactuel], (cox + int(resolutionx/384), coy))
                    screen.blit(BarreDeVieVide, (cox, coy + int(resolutiony/13.5)))
                    screen.blit(BarreDeXp[pogactuel], (cox + int(resolutionx/354), coy + int(resolutiony/13.5)))
                    screen.blit(texteNiveau[pogactuel], (cox + int(resolutionx/19.2), coy - int(resolutiony/10.8)))
                    screen.blit(texteName[pogactuel], (cox - int(resolutionx/6.4), coy - int(resolutiony/10.8)))
                    screen.blit(texteVie[pogactuel], (cox + int(resolutionx/12.8), coy + int(resolutiony/54)))

            pygame.display.flip()
            time.sleep(0.1)

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_s and positionycadre < (int(resolutiony/54) + 2*int(resolutiony/3.22)):
                        positionycadre += int(resolutiony/3.22)
                        emplacementMenu += 2

                    if event.key == pygame.K_w and positionycadre > int(resolutiony/54):
                        positionycadre -= int(resolutiony/3.22)
                        emplacementMenu -= 2

                    if event.key == pygame.K_a and positionxcadre > int(resolutionx/64):
                        positionxcadre -= int(resolutionx/2.04)
                        emplacementMenu -= 1

                    if event.key == pygame.K_d and positionxcadre < (int(resolutionx/64) + int(resolutionx/2.04)):
                        positionxcadre += int(resolutionx/2.04)
                        emplacementMenu += 1

                    if event.key == pygame.K_ESCAPE:
                        pause3 = False
                        pogchangeequipe = 999
                        break

                    if event.key == pygame.K_SPACE:
                        pogchangeequipe = emplacementMenu
                        screen.blit(menu, (0,0))

                        pause3 = False
                        break

    echangePogle.retirePogle(poglemonstats, numeroPog, pogchangeequipe)



    poglemonCharge.poglemonPcMenu(numeroBoite, poglemonstats)

    poglemonCharge.poglemonMenu(poglemonstats)
    pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))


#Deposer un Poglemon dans la boite


def echangepogleEquipe(pogchangeequipe, pause, poglemonstats):

    x = 1

    while poglemonstats.get("pc"+str(x)) != None:
        x += 1

    echangePogle.posePogle(pogchangeequipe, poglemonstats, x)


    poglemonCharge.poglemonMenu(poglemonstats)
    pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))



#Deplacer un Poglemon dans la boite

def deplacementPogle(emplacementBoite2, poglemonstats, positionCadreX3, positionCadreY3, numeroBoite2):


    screen.blit(menu, (0,0))
    texteBoite2 = police2.render(("Deplacer vers?"),True,pygame.Color("#000000"))
    screen.blit(texteBoite2, (int(resolutionx/4.8), int(resolutiony/21.6)))
    screen.blit(cadreBoite,(positionCadreX3, positionCadreY3))

    pogdeplace = emplacementBoite2


    pause4 = True

    while pause4 == True:


        screen.blit(cadreBoite,(positionCadreX3, positionCadreY3))


        screen.blit(texteBoite2, (int(resolutionx/4.8), int(resolutiony/21.6)))


        poglemonCharge.poglemonPcMenu(numeroBoite2, poglemonstats)

        pygame.display.flip()
        screen.blit(menu, (0,0))
        time.sleep(0.1)

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pause4 = False
                    pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))
                    break

                if event.key == pygame.K_d and positionCadreX3 != int(resolutionx/10.38) + 5*int(resolutionx/7.11):
                    positionCadreX3 += int(resolutionx/7.11)
                    emplacementBoite2 += 1
                    print(emplacementBoite2)

                if event.key == pygame.K_a and positionCadreX3 != int(resolutionx/10.38):
                    positionCadreX3 -= int(resolutionx/7.11)
                    emplacementBoite2 -= 1
                    print(emplacementBoite2)

                if event.key == pygame.K_s and positionCadreY3 != int(resolutiony/5.4) + 4*int(resolutiony/6.35):
                    positionCadreY3 += int(resolutiony/6.35)
                    emplacementBoite2 += 6
                    print(emplacementBoite2)

                if event.key == pygame.K_w and positionCadreY3 != int(resolutiony/5.4):
                    positionCadreY3 -= int(resolutiony/6.35)
                    emplacementBoite2 -= 6
                    print(emplacementBoite2)

                if event.key == pygame.K_e and numeroBoite2 <= 31:
                    numeroBoite2 += 1
                    emplacementBoite2 += 30
                    print(emplacementBoite2)

                if event.key == pygame.K_q and numeroBoite2 >= 2:
                    numeroBoite2 -= 1
                    emplacementBoite2 -= 30
                    print(emplacementBoite2)

                if event.key == pygame.K_SPACE:

                    echangePogle.deplacePoglePC(poglemonstats, pogdeplace, emplacementBoite2)


                    pause4 = False
                    break



    pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))
