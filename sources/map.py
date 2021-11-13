import numpy, random

def InitialisationMap():

    world = numpy.mat([ [1]*3600  for n in range(3600)])

    position = 1

    for x in range(0, 10):
        for y in range(0,36):
            if x/2 == int(x/2):
                if position == 1:
                    world[x,y] = 3
                    world[x + 26,y] = 3
                    position = 0
                elif position == 0:
                    world[x,y] = 2
                    world[x + 26,y] = 2
                    position = 1

            else:
                world[x,y] = 2
                world[x + 26,y] = 2

    position = 1

    for y in range(0, 10):
        for x in range(0, 36):
            if y/2 == int(y/2):
                if position == 1:
                    world[x,y] = 3
                    world[x ,y+26] = 3
                    position = 0
                elif position == 0:
                    world[x,y] = 2
                    world[x ,y +26] = 2
                    position = 1

            else:
                world[x,y] = 2
                world[x ,y +26] = 2

    position = 1

    for y in range(10, 20):
        for x in range(0, 36):
            if y/2 == int(y/2):
                if position == 1:
                    world[x ,y + 26] = 3
                    position = 0
                elif position == 0:
                    world[x ,y + 26] = 2
                    position = 1

            else:
                world[x ,y +26] = 2


    for x in range(11,25):
        for y in range(11,25):
            randome = random.randint(0,10)

            if randome == 1:
                world[x,y] = 0
            else:
                world[x,y] = 1

    world[17, 17] = 15


    for x in range(41,61):
        for y in range(0,20):
            world[x,y] = 4

    world[51, 11] = 16
    world[49, 11] = 17
    world[53, 11] = 18
    world[39, 11] = 69

    numpy.save("../zone/zone1.npy", world)
