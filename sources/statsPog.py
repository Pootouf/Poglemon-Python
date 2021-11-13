import pygame, os, pickle
import poglemonCharge

from pygame.locals import *

cadreStats = pygame.image.load("../textures/StatsPoke.png")



def start():

    global cadreStats, resolutionx, resolutiony, screen, police1 ,police2 ,police3 ,police4, police5

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

    cadreStats = pygame.image.load("../textures/StatsPoke.png")



    cadreStats = pygame.transform.scale(cadreStats, (resolutionx, resolutiony))

    police1 = pygame.font.Font(None,int(resolutionx/19.2))
    police2 = pygame.font.Font(None,int(resolutionx/9.6))
    police3 = pygame.font.Font(None,int(resolutionx/25.6))
    police4 = pygame.font.Font(None,int(resolutionx/42.67))
    police5 = pygame.font.Font(None,int(resolutionx/35))


def statsPog(numeroPog, pause, poglemonstats, EquipePC):

    screen.blit(cadreStats, (0,0))




    pog = poglemonstats.get(str(EquipePC) + str(numeroPog))
    id = poglemonstats.get(str(EquipePC) + str(numeroPog) + "id")
    hp = poglemonstats.get(str(EquipePC) + str(numeroPog) + "hp")
    hpActuel = poglemonstats.get(str(EquipePC) + str(numeroPog) + "hpActuel")
    xp = poglemonstats.get(str(EquipePC) + str(numeroPog) + "xp")
    xpactuel = poglemonstats.get(str(EquipePC) + str(numeroPog) + "xpActuel")
    attaque = poglemonstats.get(str(EquipePC) + str(numeroPog) + "atk")
    attaquespe = poglemonstats.get(str(EquipePC) + str(numeroPog) + "spatk")
    defense = poglemonstats.get(str(EquipePC) + str(numeroPog) + "def")
    defensespe = poglemonstats.get(str(EquipePC) + str(numeroPog) + "spdef")
    vitesse = poglemonstats.get(str(EquipePC) + str(numeroPog) + "vit")
    niveau = poglemonstats.get(str(EquipePC) + str(numeroPog) + "niv")
    type1 = poglemonstats.get(str(EquipePC) + str(numeroPog) + "type1")
    name = poglemonstats.get(str(EquipePC) + str(numeroPog) + "name")

    if poglemonstats.get(str(EquipePC) + str(numeroPog) + "type2") != None:
        type2 = poglemonstats.get(str(EquipePC) + str(numeroPog) + "type2")
        textetype2 = police1.render((str(type2)),True,pygame.Color("#000000"))
        screen.blit(textetype2, (int(resolutionx/3.49), int(resolutiony/1.62)))


    for x in range(1,5):
        if poglemonstats.get(str(EquipePC) + str(numeroPog) + "attaque" + str(x)) != None:
            attaquelistenom = poglemonstats.get(str(EquipePC) + str(numeroPog) + "attaque" + str(x) + "nom")
            attaquelistedeg = poglemonstats.get(str(EquipePC) + str(numeroPog) + "attaque" + str(x) + "deg")
            attaquelistepp = poglemonstats.get(str(EquipePC) + str(numeroPog) + "attaque" + str(x) + "pp")
            attaquelistepprestant = poglemonstats.get(str(EquipePC) + str(numeroPog) + "attaque" + str(x) + "pprestant")
            attaquelistepre = poglemonstats.get(str(EquipePC) + str(numeroPog) + "attaque" + str(x) + "pre")
            attaquelistecategorie = poglemonstats.get(str(EquipePC) + str(numeroPog) + "attaque" + str(x) + "categorie")

            texteattaquelistenom = police5.render((str(attaquelistenom)),True,pygame.Color("#000000"))
            texteattaquelistedeg = police4.render(("Deg: " + str(attaquelistedeg)),True,pygame.Color("#000000"))
            texteattaquelistepprestant = police4.render((str(attaquelistepprestant) + "/" + str(attaquelistepp)),True,pygame.Color("#000000"))
            texteattaquelistepre = police4.render(("Pre: " + str(attaquelistepre)),True,pygame.Color("#000000"))

            if attaquelistecategorie == "physique":
                texteattaquelistecategorie = police4.render(("PHY"),True,pygame.Color("#000000"))
            else:
                texteattaquelistecategorie = police4.render(("SPE"),True,pygame.Color("#000000"))



            if x == 1:
                screen.blit(texteattaquelistenom, (int(resolutionx/2.06), int(resolutiony/1.51)))
                screen.blit(texteattaquelistedeg, (int(resolutionx/1.61), int(resolutiony/1.51)))
                screen.blit(texteattaquelistepre, (int(resolutionx/1.61), int(resolutiony/1.38)))
                screen.blit(texteattaquelistepprestant, (int(resolutionx/2.06), int(resolutiony/1.38)))
                screen.blit(texteattaquelistecategorie, (int(resolutionx/1.81), int(resolutiony/1.38)))

            if x == 2:
                screen.blit(texteattaquelistenom, (int(resolutionx/1.37), int(resolutiony/1.51)))
                screen.blit(texteattaquelistedeg, (int(resolutionx/1.16), int(resolutiony/1.51)))
                screen.blit(texteattaquelistepre, (int(resolutionx/1.16), int(resolutiony/1.38)))
                screen.blit(texteattaquelistepprestant, (int(resolutionx/1.37), int(resolutiony/1.38)))
                screen.blit(texteattaquelistecategorie, (int(resolutionx/1.26), int(resolutiony/1.38)))

            if x == 3:
                screen.blit(texteattaquelistenom, (int(resolutionx/2.06), int(resolutiony/1.23)))
                screen.blit(texteattaquelistedeg, (int(resolutionx/1.61), int(resolutiony/1.23)))
                screen.blit(texteattaquelistepre, (int(resolutionx/1.61), int(resolutiony/1.15)))
                screen.blit(texteattaquelistepprestant, (int(resolutionx/2.06), int(resolutiony/1.15)))
                screen.blit(texteattaquelistecategorie, (int(resolutionx/1.81), int(resolutiony/1.15)))

            if x == 4:
                screen.blit(texteattaquelistenom, (int(resolutionx/1.37), int(resolutiony/1.23)))
                screen.blit(texteattaquelistedeg, (int(resolutionx/1.16), int(resolutiony/1.23)))
                screen.blit(texteattaquelistepre, (int(resolutionx/1.16), int(resolutiony/1.15)))
                screen.blit(texteattaquelistepprestant, (int(resolutionx/1.37), int(resolutiony/1.15)))
                screen.blit(texteattaquelistecategorie, (int(resolutionx/1.26), int(resolutiony/1.15)))



    print(pog)

    poglemonCharge.poglemonPC(pog)
    chargepog7 = pygame.image.load("../textures/chargePog7.png")
    chargepog7 = pygame.transform.scale(chargepog7, (int(resolutionx/4.8), int(resolutiony/2.88)))

    textePogledex = police1.render((str(pog)),True,pygame.Color("#000000"))
    texteID = police4.render((str(id)),True,pygame.Color("#000000"))
    textehp = police1.render(str(hpActuel) + "/" + (str(hp)),True,pygame.Color("#000000"))
    texteatk = police1.render((str(attaque)),True,pygame.Color("#000000"))
    textespatk = police1.render((str(attaquespe)),True,pygame.Color("#000000"))
    textedef = police1.render((str(defense)),True,pygame.Color("#000000"))
    textespdef = police1.render((str(defensespe)),True,pygame.Color("#000000"))
    textevit = police1.render((str(vitesse)),True,pygame.Color("#000000"))
    texteniv = police1.render((str(niveau)),True,pygame.Color("#000000"))
    textetype1 = police1.render((str(type1)),True,pygame.Color("#000000"))
    textename = police1.render((str(name)),True,pygame.Color("#000000"))

    BarreDeXp = pygame.image.load("../textures/BarreDeXP.png")
    BarreDeXp = pygame.transform.scale(BarreDeXp, (int(int(resolutionx/6.4) * (xpactuel/xp)), int(resolutiony/108)))

    BarreDeVieVide = pygame.image.load("../textures/BarreDeVieVide.png")
    BarreDeVieVide = pygame.transform.scale(BarreDeVieVide, (int(int(resolutionx/6.19)), int(resolutiony/108)))


    screen.blit(chargepog7, (int(resolutionx/14.22), int(resolutiony/4.6)))

    screen.blit(textePogledex, (int(resolutionx/2.74), int(resolutiony/1.44)))
    screen.blit(texteID, (int(resolutionx/2.11), int(resolutiony/13.5)))
    screen.blit(texteniv, (int(resolutionx/1.11), int(resolutiony/18)))
    screen.blit(textehp, (int(resolutionx/2.02), int(resolutiony/5.4)))
    screen.blit(texteatk, (int(resolutionx/2.02), int(resolutiony/4.08)))
    screen.blit(textespatk, (int(resolutionx/2.02), int(resolutiony/3.18)))
    screen.blit(textedef, (int(resolutionx/2.02), int(resolutiony/2.63)))
    screen.blit(textespdef, (int(resolutionx/2.02), int(resolutiony/2.25)))
    screen.blit(textevit, (int(resolutionx/2.02), int(resolutiony/1.93)))
    screen.blit(textetype1, (int(resolutionx/6.4), int(resolutiony/1.62)))
    screen.blit(textename, (int(resolutionx/13.71), int(resolutiony/13.5)))

    screen.blit(BarreDeVieVide, (int(resolutionx/1.3), int(resolutiony/3.6)))
    screen.blit(BarreDeXp, (int(resolutionx/1.29), int(resolutiony/3.6)))

    pygame.display.flip()

    while pause == True:

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                        pause = False
                        break
