import pygame, numpy, pickle, time, os
from pygame.locals import *


cadreResolution = pygame.image.load("../textures/cadreResolution.png")
cadreResolutionSelection = pygame.image.load("../textures/cadreResolutionSelection.png")

def start():

    global resolutionx, resolutiony, screen, cadreResolution, cadreResolutionSelection, positioncadrex, positioncadrey

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
    positioncadrex = int(resolutionx/42.67) + int(resolutionx/3.76)
    positioncadrey = int(resolutiony/6.75) + int(resolutiony/3.72)

    cadreResolution = pygame.image.load("../textures/cadreResolution.png")
    cadreResolutionSelection = pygame.image.load("../textures/cadreResolutionSelection.png")

    cadreResolution = pygame.transform.scale(cadreResolution, (int(resolutionx/2.13), int(resolutiony/2.16)))
    cadreResolutionSelection = pygame.transform.scale(cadreResolutionSelection, (int(resolutionx/5.26), int(resolutiony/8)))

    flags = DOUBLEBUF
    screen = pygame.display.set_mode(size, flags)
    screen.set_alpha(None)




def changementResolution():
    global positioncadrex, positioncadrey

    pause = True

    chat_command = {}
    chat_command["resolutionx"] = ""
    chat_command["resolutiony"] = ""

    reso = "resolutionx"

    chat_ouvert = True
    police3 = pygame.font.Font(None,int(resolutionx/24))

    while pause == True:
        screen.blit(cadreResolution, (int(resolutionx/3.76), int(resolutiony/3.72)))
        screen.blit(cadreResolutionSelection, (positioncadrex, positioncadrey))
        texteResolutionx = police3.render((chat_command["resolutionx"]),True,pygame.Color("#000000"))
        screen.blit(texteResolutionx, (int(resolutionx/19.2) + int(resolutionx/3.76), int(resolutiony/5.4) + int(resolutiony/3.72)))
        texteResolutiony = police3.render((chat_command["resolutiony"]),True,pygame.Color("#000000"))
        screen.blit(texteResolutiony, (int(resolutionx/3.52) + int(resolutionx/3.76), int(resolutiony/5.4) + int(resolutiony/3.72)))

        pygame.display.flip()
        time.sleep(0.2)

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN and len(chat_command)>0 and chat_ouvert == True:
                    try:
                        resolution = {}

                        resolution["resolutionx"] = int(chat_command["resolutionx"])
                        resolution["resolutiony"] = int(chat_command["resolutiony"])
                        pickle.dump(resolution, open( "../save/resolution", "wb" ))

                        chat_command = {}
                        pause = False
                        break
                    except:
                        print("VALEUR INCORRECTE")
                elif event.key == pygame.K_ESCAPE:
                    chat_command = {}
                    pause = False
                    break
                elif event.key == pygame.K_BACKSPACE and chat_ouvert == True:
                    chat_command[reso] = chat_command[reso][:-1]
                elif event.key == pygame.K_w and positioncadrey != int(resolutiony/6.75) + int(resolutiony/3.72):
                    positioncadrey -= int(resolutiony/8.31)
                    chat_ouvert = True
                elif event.key == pygame.K_s and positioncadrey != int(resolutiony/6.75) + int(resolutiony/3.72) + int(resolutiony/8.31):
                    positioncadrey += int(resolutiony/8.31)
                    chat_ouvert = False
                elif event.key == pygame.K_d and positioncadrex != int(resolutionx/42.67) + int(resolutionx/3.76) + int(resolutionx/4.22):
                    reso = "resolutiony"
                    positioncadrex += int(resolutionx/4.22)
                elif event.key == pygame.K_a and positioncadrex != int(resolutionx/42.67) + int(resolutionx/3.76):
                    reso = "resolutionx"
                    positioncadrex -= int(resolutionx/4.22)

                elif chat_ouvert == True:
                    chat_command[reso] += event.unicode
