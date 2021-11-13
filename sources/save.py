import pygame, numpy, time

import pickle as pickle



def sauver(positionx, positiony, world, data, zone, poglemonstats):

    pog1 = poglemonstats.get("pog1")
    pog2 = poglemonstats.get("pog2")
    pog3 = poglemonstats.get("pog3")
    pog4 = poglemonstats.get("pog4")
    pog5 = poglemonstats.get("pog5")
    pog6 = poglemonstats.get("pog6")

    
    data["positionx"]= positionx
    data["positiony"]= positiony
    data["zone"]= zone
    data["pog1"]= pog1
    data["pog2"]= pog2
    data["pog3"]= pog3
    data["pog4"]= pog4
    data["pog5"]= pog5
    data["pog6"]= pog6
    
    numpy.save("../zone/zone1-2.npy", world)
    print(world[17,17])

    pickle.dump(data, open( "../save/save", "wb" ))
    pickle.dump(poglemonstats, open( "../save/poglemonstatsSAVE", "wb" ))

    time.sleep(0.3)





    





    
    