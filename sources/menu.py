import pygame, numpy, time, pickle, os

import chargement
import save
import pc
import poglemonCharge
import echangePogle
import statsPog

from pygame.locals import *

menu = pygame.image.load("../textures/cadreMenu.png")
cadreTexte = pygame.image.load("../textures/cadreTexte.png")
cadreTexte2 = pygame.image.load("../textures/cadreTexte2.png")
cadrePogle = pygame.image.load("../textures/cadrePogle.png")
cadreStats = pygame.image.load("../textures/StatsPoke.png")
cadreMenuPC = pygame.image.load("../textures/cadreMenuPC.png")
cadreMenuPCselection = pygame.image.load("../textures/cadreMenuPCselection.png")

player = pygame.image.load("../textures/player1.png")




def start():

    global menu, cadreTexte, cadreTexte2, cadrePogle, cadreStats, cadreMenuPC, cadreMenuPCselection, resolutionx, resolutiony, screen, police ,police2 ,police3 ,police4, positionxcadre, positionycadre, listeco

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

    menu = pygame.image.load("../textures/cadreMenu.png")
    cadreTexte = pygame.image.load("../textures/cadreTexte.png")
    cadreTexte2 = pygame.image.load("../textures/cadreTexte2.png")
    cadrePogle = pygame.image.load("../textures/cadrePogle.png")
    cadreStats = pygame.image.load("../textures/StatsPoke.png")
    cadreMenuPC = pygame.image.load("../textures/cadreMenuPC.png")
    cadreMenuPCselection = pygame.image.load("../textures/cadreMenuPCselection.png")


    menu = pygame.transform.scale(menu, (int(resolutionx/3.84), resolutiony))
    cadreTexte = pygame.transform.scale(cadreTexte, (int(resolutionx/4.8), int(resolutiony/10.8)))
    cadreTexte2 = pygame.transform.scale(cadreTexte2, (int(resolutionx/2.4), int(resolutiony/3.09)))
    cadrePogle = pygame.transform.scale(cadrePogle, (resolutionx, resolutiony))
    cadreStats = pygame.transform.scale(cadreStats, (resolutionx, resolutiony))
    cadreMenuPC = pygame.transform.scale(cadreMenuPC, (int(resolutionx/5.05), int(resolutiony/1.96)))
    cadreMenuPCselection = pygame.transform.scale(cadreMenuPCselection, (int(resolutionx/5.65), int(resolutiony/9)))




    police = pygame.font.Font(None,int(resolutionx/19.2))
    police2 = pygame.font.Font(None,int(resolutionx/9.6))
    police3 = pygame.font.Font(None,int(resolutionx/25.6))
    police4 = pygame.font.Font(None,int(resolutionx/42.67))

    positionxcadre = int(resolutionx/1.32)
    positionycadre = int(resolutiony/36)

    listeco = {}
    listeco[1] = int(resolutionx/4.8), int(resolutiony/6)
    listeco[2] = int(resolutionx/1.43), int(resolutiony/6)
    listeco[3] = int(resolutionx/4.8), int(resolutiony/2.1)
    listeco[4] = int(resolutionx/1.43), int(resolutiony/2.1)
    listeco[5] = int(resolutionx/4.8), int(resolutiony/1.27)
    listeco[6] = int(resolutionx/1.43), int(resolutiony/1.27)




#Menu du jeu

def chargementMenu(positionx, positiony, zone, world, data, poglemonstats):

    global positionycadre




    pause = True

    while pause == True:

        screen.blit(menu, (int(resolutionx/1.35),  0))
        texte1 = police.render(("Poglemon"),True,pygame.Color("#000000"))
        texte2 = police.render(("Sac"),True,pygame.Color("#000000"))
        texte4 = police.render(("Sauver"),True,pygame.Color("#000000"))
        texte3 = police.render(("Quitter"),True,pygame.Color("#000000"))
        texte5 = police.render(("PC"),True,pygame.Color("#000000"))

        screen.blit(texte1, (int(resolutionx/1.31), int(resolutiony/21.6)))
        screen.blit(texte2, (int(resolutionx/1.31), int(resolutiony/7.2)))
        screen.blit(texte4, (int(resolutionx/1.31), int(resolutiony/4.32)))
        screen.blit(texte5, (int(resolutionx/1.31), int(resolutiony/3.09)))
        screen.blit(texte3, (int(resolutionx/1.31), int(resolutiony/1.14)))


        screen.blit(cadreTexte, (positionxcadre, positionycadre))
        pygame.display.flip()


        time.sleep(0.1)

        for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_s and positionycadre == (int(resolutiony/36) + 9*int(resolutiony/10.8)):
                        positionycadre = int(resolutiony/36)
                        screen.blit(cadreTexte, (positionxcadre, positionycadre))
                        pygame.display.flip()

                        event.key = 0

                    if event.key == pygame.K_s and positionycadre < (int(resolutiony/36) + 9*int(resolutiony/10.8)):
                        positionycadre += int(resolutiony/10.8)
                        screen.blit(cadreTexte, (positionxcadre, positionycadre))
                        pygame.display.flip()

                    if event.key == pygame.K_w and positionycadre == int(resolutiony/36):
                        positionycadre = (int(resolutiony/36) + 9*int(resolutiony/10.8))
                        screen.blit(cadreTexte, (positionxcadre, positionycadre))
                        pygame.display.flip()

                        event.key = 0


                    if event.key == pygame.K_w and positionycadre > int(resolutiony/36):
                        positionycadre -= int(resolutiony/10.8)
                        screen.blit(cadreTexte, (positionxcadre, positionycadre))
                        pygame.display.flip()


                    if event.key == pygame.K_SPACE and positionycadre == (int(resolutiony/36) + 9*int(resolutiony/10.8)):
                        pause = False
                        time.sleep(0.2)

                    if event.key == pygame.K_SPACE and positionycadre == (int(resolutiony/36) + 3*int(resolutiony/10.8)):
                        chargement.chargementMap(positionx, positiony, zone, world)
                        pygame.display.flip()
                        pc.chargementPc(poglemonstats, pause)
                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))
                        chargement.chargementMap(positionx, positiony, zone, world)
                        screen.blit(player, (resolutionx/2 ,resolutiony/2))
                        pygame.display.flip()

                    if event.key == pygame.K_SPACE and positionycadre == int(resolutiony/36):

                        chargementPogle(positionxcadre, positionycadre, pause, poglemonstats)
                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))
                        chargement.chargementMap(positionx, positiony, zone, world)
                        screen.blit(player, (resolutionx/2 ,resolutiony/2))
                        pygame.display.flip()

                    if event.key == pygame.K_SPACE and positionycadre == (int(resolutiony/36) + 2*int(resolutiony/10.8)):

                        print("save")
                        save.sauver(positionx + resolutionx/2,positiony + resolutiony/2,world, data, zone, poglemonstats)

                        screen.blit(menu, (int(resolutionx/1.35),  0))
                        texte1 = police.render(("Poglemon"),True,pygame.Color("#000000"))
                        texte2 = police.render(("Sac"),True,pygame.Color("#000000"))
                        texte4 = police.render(("Reussi"),True,pygame.Color("#000000"))
                        texte3 = police.render(("Quitter"),True,pygame.Color("#000000"))
                        texte5 = police.render(("PC"),True,pygame.Color("#000000"))

                        screen.blit(texte1, (int(resolutionx/1.31), int(resolutiony/21.6)))
                        screen.blit(texte2, (int(resolutionx/1.31), int(resolutiony/7.2)))
                        screen.blit(texte4, (int(resolutionx/1.31), int(resolutiony/4.32)))
                        screen.blit(texte5, (int(resolutionx/1.31), int(resolutiony/3.09)))
                        screen.blit(texte3, (int(resolutionx/1.31), int(resolutiony/1.14)))

                        pygame.display.flip()

                        time.sleep(1)

                    if event.key == pygame.K_ESCAPE:
                        pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))
                        pause = False
                        time.sleep(0.2)
                        break


#menu des Poglemons de l'équipe


def chargementPogle(positionxcadre, positionycadre, pause, poglemonstats):


    positionxcadre = int(resolutionx/64)
    positionycadre = int(resolutiony/54)

    emplacementMenu = 1


    screen.blit(cadreTexte2, (positionxcadre, positionycadre))



    poglemonCharge.poglemonMenu(poglemonstats)


    chargepog = {}

    echangePogle.deplacePogleAuto(poglemonstats)

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

            texteNiveau[x] = police3.render("Niveau:" + (str(niveau[x])),True,pygame.Color("#000000"))
            texteName[x] = police3.render((str(name[x])),True,pygame.Color("#000000"))
            texteVie[x] = police3.render((str(hpactuel[x]) + "/" + str(hp[x])),True,pygame.Color("#000000"))
            BarreDeVie[x] = pygame.transform.scale(BarreDeVie[x], (int(int(resolutionx/6.4) * (hpactuel[x]/hp[x])), int(resolutiony/108)))
            BarreDeXp[x] = pygame.transform.scale(BarreDeXp[x], (int(int(resolutionx/6.4) * (xpactuel[x]/xp[x])), int(resolutiony/108)))




    pygame.display.flip()

    while pause == True:

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


        echangePogle.deplacePogleAuto(poglemonstats)
        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))



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

                texteNiveau[x] = police3.render("Niveau:" + (str(niveau[x])),True,pygame.Color("#000000"))
                texteName[x] = police3.render((str(name[x])),True,pygame.Color("#000000"))
                texteVie[x] = police3.render((str(hpactuel[x]) + "/" + str(hp[x])),True,pygame.Color("#000000"))
                BarreDeVie[x] = pygame.transform.scale(BarreDeVie[x], (int(int(resolutionx/6.4) * (hpactuel[x]/hp[x])), int(resolutiony/108)))
                BarreDeXp[x] = pygame.transform.scale(BarreDeXp[x], (int(int(resolutionx/6.4) * (xpactuel[x]/xp[x])), int(resolutiony/108)))




        pygame.display.flip()

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
                    pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))
                    pause = False
                    break

                if event.key == pygame.K_SPACE and poglemonstats.get("pog" + str(emplacementMenu)) != None:

                    if positionxcadre <= resolutionx/2:
                        if positionycadre <= int(resolutiony/2.45):

                            difference = 0
                        else:
                            difference = -int(resolutiony/2.7)

                        screen.blit(cadreMenuPC, (positionxcadre + int(resolutionx/7.1), positionycadre + difference))

                        texteMenuPC = police.render(("Résumé"),True,pygame.Color("#000000"))
                        screen.blit(texteMenuPC, (positionxcadre + int(resolutionx/6.4), positionycadre + int(resolutiony/27) + difference))

                        texteMenuPC2 = police.render(("Deposer"),True,pygame.Color("#000000"))
                        screen.blit(texteMenuPC2, (positionxcadre + int(resolutionx/6.4), positionycadre + int(resolutiony/7.71) + difference))

                        texteMenuPC3 = police.render(("Quitter"),True,pygame.Color("#000000"))
                        screen.blit(texteMenuPC3, (positionxcadre + int(resolutionx/6.4), positionycadre + int(resolutiony/2.45) + difference))

                        texteMenuPC4 = police.render(("Deplacer"),True,pygame.Color("#000000"))
                        screen.blit(texteMenuPC4, (positionxcadre + int(resolutionx/6.4), positionycadre + int(resolutiony/4.5) + difference))


                        pygame.display.flip()



                        positionCadreX2 = positionxcadre + int(resolutionx/6.62)
                        positionCadreY2 = positionycadre + int(resolutiony/72) + difference
                    else:
                        if positionycadre <= int(resolutiony/2.45):
                            difference = 0
                        else:
                            difference = -int(resolutiony/2.7)

                        screen.blit(cadreMenuPC, (positionxcadre - int(resolutionx/5.82), positionycadre + difference))

                        texteMenuPC = police.render(("Résumé"),True,pygame.Color("#000000"))
                        screen.blit(texteMenuPC, (positionxcadre - int(resolutionx/6.4), positionycadre + int(resolutiony/27) + difference))

                        texteMenuPC2 = police.render(("Deposer"),True,pygame.Color("#000000"))
                        screen.blit(texteMenuPC2, (positionxcadre - int(resolutionx/6.4), positionycadre + int(resolutiony/7.71) + difference))

                        texteMenuPC3 = police.render(("Quitter"),True,pygame.Color("#000000"))
                        screen.blit(texteMenuPC3, (positionxcadre - int(resolutionx/6.4), positionycadre + int(resolutiony/2.45) + difference))

                        texteMenuPC4 = police.render(("Deplacer"),True,pygame.Color("#000000"))
                        screen.blit(texteMenuPC4, (positionxcadre - int(resolutionx/6.4), positionycadre + int(resolutiony/4.5) + difference))



                        pygame.display.flip()



                        positionCadreX2 = positionxcadre - int(resolutionx/6.19)
                        positionCadreY2 = positionycadre + difference + int(resolutiony/72)

                    screen.blit(cadreMenuPCselection, (positionCadreX2, positionCadreY2))

                    pause2 = True

                    while pause2 == True:

                        if positionxcadre <= resolutionx/2:
                            if positionycadre <= int(resolutiony/2.45):
                                difference = 0
                            else:
                                difference = -int(resolutiony/2.7)

                            screen.blit(texteMenuPC, (positionxcadre + int(resolutionx/6.4), positionycadre + int(resolutiony/27) + difference))
                            screen.blit(texteMenuPC2, (positionxcadre + int(resolutionx/6.4), positionycadre + int(resolutiony/7.71) + difference))
                            screen.blit(texteMenuPC3, (positionxcadre + int(resolutionx/6.4), positionycadre + int(resolutiony/2.45) + difference))
                            screen.blit(texteMenuPC4, (positionxcadre + int(resolutionx/6.4), positionycadre + int(resolutiony/4.5) + difference))

                            pygame.display.flip()
                            screen.blit(cadreMenuPC, (positionxcadre + int(resolutionx/7.1), positionycadre + difference))
                        else:
                            if positionycadre <= int(resolutiony/2.45):
                                difference = 0
                            else:
                                difference = -int(resolutiony/2.7)

                            screen.blit(texteMenuPC, (positionxcadre - int(resolutionx/6.4), positionycadre + int(resolutiony/27) + difference))
                            screen.blit(texteMenuPC2, (positionxcadre - int(resolutionx/6.4), positionycadre + int(resolutiony/7.71) + difference))
                            screen.blit(texteMenuPC3, (positionxcadre - int(resolutionx/6.4), positionycadre + int(resolutiony/2.45) + difference))
                            screen.blit(texteMenuPC4, (positionxcadre - int(resolutionx/6.4), positionycadre + int(resolutiony/4.5) + difference))
                            pygame.display.flip()
                            screen.blit(cadreMenuPC, (positionxcadre - int(resolutionx/5.82), positionycadre + difference))

                        screen.blit(cadreMenuPCselection, (positionCadreX2, positionCadreY2))

                        time.sleep(0.1)

                        for event in pygame.event.get():

                            if event.type == pygame.KEYDOWN:

                                if event.key == pygame.K_s and positionCadreY2 != positionycadre + int(resolutiony/72) + difference + 4*int(resolutiony/10.8):
                                    positionCadreY2 += int(resolutiony/10.8)

                                if event.key == pygame.K_w and positionCadreY2 != positionycadre + int(resolutiony/72) + difference:
                                    positionCadreY2 -= int(resolutiony/10.8)

                                if event.key == pygame.K_ESCAPE:
                                    pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))
                                    pause2 = False
                                    break

                                if event.key == pygame.K_SPACE:

                                    if positionCadreY2 == positionycadre + int(resolutiony/72) + difference:

                                        statsPog.statsPog(emplacementMenu, pause, poglemonstats, "pog")
                                        screen.blit(cadrePogle, (0, 0))
                                        screen.blit(cadreTexte2, (positionxcadre, positionycadre))
                                        screen.blit(chargepog[1], (int(resolutionx/19.2), int(resolutiony/8)))
                                        screen.blit(chargepog[2], (int(resolutionx/1.85), int(resolutiony/8)))
                                        screen.blit(chargepog[3], (int(resolutionx/19.2), int(resolutiony/2.3)))
                                        screen.blit(chargepog[4], (int(resolutionx/1.85), int(resolutiony/2.3)))
                                        screen.blit(chargepog[5], (int(resolutionx/19.2), int(resolutiony/1.34)))
                                        screen.blit(chargepog[6], (int(resolutionx/1.85), int(resolutiony/1.34)))
                                        pause2 = False
                                        break


                                    if positionCadreY2 == positionycadre + int(resolutiony/72) + 4*int(resolutiony/10.8) + difference:
                                        pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))
                                        pause2 = False
                                        time.sleep(0.2)
                                        break

                                    if positionCadreY2 == positionycadre + int(resolutiony/72) + int(resolutiony/10.8) + difference and poglemonstats.get("pog2") != None:
                                        pc.echangepogleEquipe(emplacementMenu, pause, poglemonstats)
                                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))
                                        screen.blit(cadrePogle, (0, 0))



                                        for x in range(1, 7):

                                            chargepog[x] = pygame.image.load("../textures/chargePog" + str(x) + ".png")
                                            chargepog[x] = pygame.transform.scale(chargepog[x], (int(resolutionx/9.9), int(resolutiony/5.77)))

                                        screen.blit(chargepog[1], (int(resolutionx/19.2), int(resolutiony/8)))
                                        screen.blit(chargepog[2], (int(resolutionx/1.85), int(resolutiony/8)))
                                        screen.blit(chargepog[3], (int(resolutionx/19.2), int(resolutiony/2.3)))
                                        screen.blit(chargepog[4], (int(resolutionx/1.85), int(resolutiony/2.3)))
                                        screen.blit(chargepog[5], (int(resolutionx/19.2), int(resolutiony/1.34)))
                                        screen.blit(chargepog[6], (int(resolutionx/1.85), int(resolutiony/1.34)))
                                        pygame.display.flip()
                                        pause2 = False
                                        break

                                    if positionCadreY2 == positionycadre + int(resolutiony/72) + 2*int(resolutiony/10.8) + difference:
                                        deplacementpogEquipe(emplacementMenu, poglemonstats, positionxcadre, positionycadre)
                                        poglemonstats = pickle.load( open( "../save/poglemonstats", "rb" ))

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

                                                texteNiveau[x] = police3.render("Niveau:" + (str(niveau[x])),True,pygame.Color("#000000"))
                                                texteName[x] = police3.render((str(name[x])),True,pygame.Color("#000000"))
                                                texteVie[x] = police3.render((str(hpactuel[x]) + "/" + str(hp[x])),True,pygame.Color("#000000"))
                                                BarreDeVie[x] = pygame.transform.scale(BarreDeVie[x], (int(int(resolutionx/6.4) * (hpactuel[x]/hp[x])), int(resolutiony/108)))
                                                BarreDeXp[x] = pygame.transform.scale(BarreDeXp[x], (int(int(resolutionx/6.4) * (xpactuel[x]/xp[x])), int(resolutiony/108)))

                                        pause2 = False
                                        break




#Déplacement poglemon de l'équipe

def deplacementpogEquipe(emplacementMenu, poglemonstats, positionxcadre, positionycadre):

    screen.blit(cadreTexte2, (positionxcadre, positionycadre))

    emplacementMenuInit = emplacementMenu

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

            texteNiveau[x] = police3.render("Niveau:" + (str(niveau[x])),True,pygame.Color("#000000"))
            texteName[x] = police3.render((str(name[x])),True,pygame.Color("#000000"))
            texteVie[x] = police3.render((str(hpactuel[x]) + "/" + str(hp[x])),True,pygame.Color("#000000"))
            BarreDeVie[x] = pygame.transform.scale(BarreDeVie[x], (int(int(resolutionx/6.4) * (hpactuel[x]/hp[x])), int(resolutiony/108)))
            BarreDeXp[x] = pygame.transform.scale(BarreDeXp[x], (int(int(resolutionx/6.4) * (xpactuel[x]/xp[x])), int(resolutiony/108)))

    pygame.display.flip()

    pause2 = True

    while pause2 == True:
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
                    pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))
                    pause2 = False
                    break

                if event.key == pygame.K_SPACE and poglemonstats.get("pog" + str(emplacementMenu)) != None:


                    echangePogle.deplacePogleEquipe(poglemonstats, emplacementMenuInit, emplacementMenu)

                    pause2 = False
                    pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))

                    break
