import pygame, numpy, pickle

def deplacePogleAuto(poglemonstats):

    for x in range(1,6):

        attaqueliste = {}
        attaquelistenom = {}
        attaquelistedeg = {}
        attaquelistepp = {}
        attaquelistepprestant = {}
        attaquelistepre = {}

        if poglemonstats.get("pog" + str(x)) == None and poglemonstats.get("pog" + str(x+1)) != None:


            pogechange = poglemonstats["pog" + str(x + 1)]
            pogechangeid = poglemonstats["pog" + str(x+ 1) + "id"]
            pogechangehp = poglemonstats["pog" + str(x+ 1) + "hp"]
            pogechangehpActuel = poglemonstats["pog" + str(x+ 1) + "hpActuel"]
            pogechangexp = poglemonstats["pog" + str(x+ 1) + "xp"]
            pogechangexpActuel = poglemonstats["pog" + str(x+ 1) + "xpActuel"]
            pogechangeatk = poglemonstats["pog" + str(x+ 1) + "atk"]
            pogechangespatk = poglemonstats["pog" + str(x+ 1) + "spatk"]
            pogechangedef = poglemonstats["pog" + str(x+ 1) + "def"]
            pogechangespdef = poglemonstats["pog" + str(x+ 1) + "spdef"]
            pogechangevit = poglemonstats["pog" + str(x+ 1) + "vit"]
            pogechangeniv = poglemonstats["pog" + str(x+ 1) + "niv"]
            pogechangetype1 = poglemonstats["pog" + str(x+ 1) + "type1"]
            pogechangetype2 = poglemonstats["pog" + str(x+ 1) + "type2"]
            pogechangename = poglemonstats["pog" + str(x+ 1) + "name"]



            for y in range(1,5):
                    attaqueliste[y] = poglemonstats.get("pog" + str(x+ 1) + "attaque" + str(y))
                    attaquelistenom[y] = poglemonstats.get("pog" + str(x+ 1) + "attaque" + str(y) + "nom")
                    attaquelistedeg[y] = poglemonstats.get("pog" + str(x+ 1) + "attaque" + str(y) + "deg")
                    attaquelistepp[y] = poglemonstats.get("pog" + str(x+ 1) + "attaque" + str(y) + "pp")
                    attaquelistepprestant[y] = poglemonstats.get("pog" + str(x+ 1) + "attaque" + str(y) + "pprestant")
                    attaquelistepre[y] = poglemonstats.get("pog" + str(x+ 1) + "attaque" + str(y) + "pre")

            poglemonstats["pog" + str(x + 1)] = None
            poglemonstats["pog" + str(x+ 1) + "id"] = None
            poglemonstats["pog" + str(x+ 1) + "hp"] = None
            poglemonstats["pog" + str(x+ 1) + "hpActuel"] = None
            poglemonstats["pog" + str(x+ 1) + "xp"] = None
            poglemonstats["pog" + str(x+ 1) + "xpActuel"] = None
            poglemonstats["pog" + str(x+ 1) + "atk"] =None
            poglemonstats["pog" + str(x+ 1) + "spatk"] = None
            poglemonstats["pog" + str(x+ 1) + "def"] = None
            poglemonstats["pog" + str(x+ 1) + "spdef"] = None
            poglemonstats["pog" + str(x+ 1) + "vit"] = None
            poglemonstats["pog" + str(x+ 1) + "niv"] = None
            poglemonstats["pog" + str(x+ 1) + "type1"] = None
            poglemonstats["pog" + str(x+ 1) + "type2"] = None
            poglemonstats["pog" + str(x+ 1) + "name"] = None
            for y in range(1,5):
                    poglemonstats["pog" + str(x+ 1) + "attaque" + str(y)] = None
                    poglemonstats["pog" + str(x+ 1) + "attaque" + str(y) + "nom"] = None
                    poglemonstats["pog" + str(x+ 1) + "attaque" + str(y) + "deg"] = None
                    poglemonstats["pog" + str(x+ 1) + "attaque" + str(y) + "pp"] = None
                    poglemonstats["pog" + str(x+ 1) + "attaque" + str(y) + "pprestant"] = None
                    poglemonstats["pog" + str(x+ 1) + "attaque" + str(y) + "pre"] = None

            poglemonstats["pog" + str(x )] = pogechange
            poglemonstats["pog" + str(x) + "id"] = pogechangeid
            poglemonstats["pog" + str(x) + "hp"] = pogechangehp
            poglemonstats["pog" + str(x) + "hpActuel"] = pogechangehpActuel
            poglemonstats["pog" + str(x) + "xp"] = pogechangexp
            poglemonstats["pog" + str(x) + "xpActuel"] = pogechangexpActuel
            poglemonstats["pog" + str(x) + "atk"] = pogechangeatk
            poglemonstats["pog" + str(x) + "spatk"] = pogechangespatk
            poglemonstats["pog" + str(x) + "def"] = pogechangedef
            poglemonstats["pog" + str(x) + "spdef"] = pogechangespdef
            poglemonstats["pog" + str(x) + "vit"] = pogechangevit
            poglemonstats["pog" + str(x) + "niv"] = pogechangeniv
            poglemonstats["pog" + str(x) + "type1"] = pogechangetype1
            poglemonstats["pog" + str(x) + "type2"] = pogechangetype2
            poglemonstats["pog" + str(x) + "name"] = pogechangename
            for y in range(1,5):
                    poglemonstats["pog" + str(x) + "attaque" + str(y) ] = attaqueliste[y]
                    poglemonstats["pog" + str(x) + "attaque" + str(y) + "nom"] = attaquelistenom[y]
                    poglemonstats["pog" + str(x) + "attaque" + str(y) + "deg"] = attaquelistedeg[y]
                    poglemonstats["pog" + str(x) + "attaque" + str(y) + "pp"] = attaquelistepp[y]
                    poglemonstats["pog" + str(x) + "attaque" + str(y) + "pprestant"] = attaquelistepprestant[y]
                    poglemonstats["pog" + str(x) + "attaque" + str(y) + "pre"] = attaquelistepre[y]



    pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))
    return poglemonstats



def deplacePogleEquipe(poglemonstats, emplacementMenuInit, emplacementMenu):

    attaqueequipe = {}
    attaqueequipenom = {}
    attaqueequipedeg = {}
    attaqueequipepp = {}
    attaqueequipepprestant = {}
    attaqueequipepre = {}

    attaqueremplace = {}
    attaqueremplacenom = {}
    attaqueremplacedeg = {}
    attaqueremplacepp = {}
    attaqueremplacepprestant = {}
    attaqueremplacepre = {}

    pogequipe = poglemonstats["pog" + str(emplacementMenuInit)]
    pogequipeid = poglemonstats["pog" + str(emplacementMenuInit) + "id"]
    pogequipehp = poglemonstats["pog" + str(emplacementMenuInit) + "hp"]
    pogequipehpActuel = poglemonstats["pog" + str(emplacementMenuInit) + "hpActuel"]
    pogequipexp = poglemonstats["pog" + str(emplacementMenuInit) + "xp"]
    pogequipexpActuel = poglemonstats["pog" + str(emplacementMenuInit) + "xpActuel"]
    pogequipeatk = poglemonstats["pog" + str(emplacementMenuInit) + "atk"]
    pogequipespatk = poglemonstats["pog" + str(emplacementMenuInit) + "spatk"]
    pogequipedef = poglemonstats["pog" + str(emplacementMenuInit) + "def"]
    pogequipespdef = poglemonstats["pog" + str(emplacementMenuInit) + "spdef"]
    pogequipevit = poglemonstats["pog" + str(emplacementMenuInit) + "vit"]
    pogequipeniv = poglemonstats["pog" + str(emplacementMenuInit) + "niv"]
    pogequipetype1 = poglemonstats["pog" + str(emplacementMenuInit) + "type1"]
    pogequipetype2 = poglemonstats.get("pog" + str(emplacementMenuInit) + "type2")
    pogequipename = poglemonstats["pog" + str(emplacementMenuInit) + "name"]
    for y in range(1,5):
            attaqueequipe[y] = poglemonstats.get("pog" + str(emplacementMenuInit) + "attaque" + str(y))
            attaqueequipenom[y] = poglemonstats.get("pog" + str(emplacementMenuInit) + "attaque" + str(y) + "nom")
            attaqueequipedeg[y] = poglemonstats.get("pog" + str(emplacementMenuInit) + "attaque" + str(y) + "deg")
            attaqueequipepp[y] = poglemonstats.get("pog" + str(emplacementMenuInit) + "attaque" + str(y) + "pp")
            attaqueequipepprestant[y] = poglemonstats.get("pog" + str(emplacementMenuInit) + "attaque" + str(y) + "pprestant")
            attaqueequipepre[y] = poglemonstats.get("pog" + str(emplacementMenuInit) + "attaque" + str(y) + "pre")




    pogremplace = poglemonstats["pog" + str(emplacementMenu)]
    pogremplaceid = poglemonstats["pog" + str(emplacementMenu) + "id"]
    pogremplacehp = poglemonstats["pog" + str(emplacementMenu) + "hp"]
    pogremplacehpActuel = poglemonstats["pog" + str(emplacementMenu) + "hpActuel"]
    pogremplacexp = poglemonstats["pog" + str(emplacementMenu) + "xp"]
    pogremplacexpActuel = poglemonstats["pog" + str(emplacementMenu) + "xpActuel"]
    pogremplaceatk = poglemonstats["pog" + str(emplacementMenu) + "atk"]
    pogremplacespatk = poglemonstats["pog" + str(emplacementMenu) + "spatk"]
    pogremplacedef = poglemonstats["pog" + str(emplacementMenu) + "def"]
    pogremplacespdef = poglemonstats["pog" + str(emplacementMenu) + "spdef"]
    pogremplacevit = poglemonstats["pog" + str(emplacementMenu) + "vit"]
    pogremplaceniv = poglemonstats["pog" + str(emplacementMenu) + "niv"]
    pogremplacetype1 = poglemonstats["pog" + str(emplacementMenu) + "type1"]
    pogremplacetype2 = poglemonstats.get("pog" + str(emplacementMenu) + "type2")
    pogremplacename = poglemonstats["pog" + str(emplacementMenu) + "name"]
    for y in range(1,5):
            attaqueremplace[y] = poglemonstats.get("pog" + str(emplacementMenu) + "attaque" + str(y))
            attaqueremplacenom[y] = poglemonstats.get("pog" + str(emplacementMenu) + "attaque" + str(y) + "nom")
            attaqueremplacedeg[y] = poglemonstats.get("pog" + str(emplacementMenu) + "attaque" + str(y) + "deg")
            attaqueremplacepp[y] = poglemonstats.get("pog" + str(emplacementMenu) + "attaque" + str(y) + "pp")
            attaqueremplacepprestant[y] = poglemonstats.get("pog" + str(emplacementMenu) + "attaque" + str(y) + "pprestant")
            attaqueremplacepre[y] = poglemonstats.get("pog" + str(emplacementMenu) + "attaque" + str(y) + "pre")

    poglemonstats["pog" + str(emplacementMenuInit)] = pogremplace
    poglemonstats["pog" + str(emplacementMenuInit) + "id"] = pogremplaceid
    poglemonstats["pog" + str(emplacementMenuInit) + "hp"] = pogremplacehp
    poglemonstats["pog" + str(emplacementMenuInit) + "hpActuel"] = pogremplacehpActuel
    poglemonstats["pog" + str(emplacementMenuInit) + "xp"] = pogremplacexp
    poglemonstats["pog" + str(emplacementMenuInit) + "xpActuel"] = pogremplacexpActuel
    poglemonstats["pog" + str(emplacementMenuInit) + "atk"] = pogremplaceatk
    poglemonstats["pog" + str(emplacementMenuInit) + "spatk"] = pogremplacespatk
    poglemonstats["pog" + str(emplacementMenuInit) + "def"] = pogremplacedef
    poglemonstats["pog" + str(emplacementMenuInit) + "spdef"] = pogremplacespdef
    poglemonstats["pog" + str(emplacementMenuInit) + "vit"] = pogremplacevit
    poglemonstats["pog" + str(emplacementMenuInit) + "niv"] = pogremplaceniv
    poglemonstats["pog" + str(emplacementMenuInit) + "type1"] = pogremplacetype1
    poglemonstats["pog" + str(emplacementMenuInit) + "type2"] = pogremplacetype2
    poglemonstats["pog" + str(emplacementMenuInit) + "name"] = pogremplacename
    for y in range(1,5):
            poglemonstats["pog" + str(emplacementMenuInit) + "attaque" + str(y)]=attaqueremplace[y]
            poglemonstats["pog" + str(emplacementMenuInit) + "attaque" + str(y) + "nom"]=attaqueremplacenom[y]
            poglemonstats["pog" + str(emplacementMenuInit) + "attaque" + str(y) + "deg"]=attaqueremplacedeg[y]
            poglemonstats["pog" + str(emplacementMenuInit) + "attaque" + str(y) + "pp"]=attaqueremplacepp[y]
            poglemonstats["pog" + str(emplacementMenuInit) + "attaque" + str(y) + "pprestant"]=attaqueremplacepprestant[y]
            poglemonstats["pog" + str(emplacementMenuInit) + "attaque" + str(y) + "pre"]=attaqueremplacepre[y]


    poglemonstats["pog" + str(emplacementMenu)] = pogequipe
    poglemonstats["pog" + str(emplacementMenu) + "id"] = pogequipeid
    poglemonstats["pog" + str(emplacementMenu) + "hp"] = pogequipehp
    poglemonstats["pog" + str(emplacementMenu) + "hpActuel"] = pogequipehpActuel
    poglemonstats["pog" + str(emplacementMenu) + "xp"] = pogequipexp
    poglemonstats["pog" + str(emplacementMenu) + "xpActuel"] = pogequipexpActuel
    poglemonstats["pog" + str(emplacementMenu) + "atk"] = pogequipeatk
    poglemonstats["pog" + str(emplacementMenu) + "spatk"] = pogequipespatk
    poglemonstats["pog" + str(emplacementMenu) + "def"] = pogequipedef
    poglemonstats["pog" + str(emplacementMenu) + "spdef"] = pogequipespdef
    poglemonstats["pog" + str(emplacementMenu) + "vit"] = pogequipevit
    poglemonstats["pog" + str(emplacementMenu) + "niv"] = pogequipeniv
    poglemonstats["pog" + str(emplacementMenu) + "type1"] = pogequipetype1
    poglemonstats["pog" + str(emplacementMenu) + "type2"] = pogequipetype2
    poglemonstats["pog" + str(emplacementMenu) + "name"] = pogequipename
    for y in range(1,5):
            poglemonstats["pog" + str(emplacementMenu) + "attaque" + str(y)]=attaqueequipe[y]
            poglemonstats["pog" + str(emplacementMenu) + "attaque" + str(y) + "nom"]=attaqueequipenom[y]
            poglemonstats["pog" + str(emplacementMenu) + "attaque" + str(y) + "deg"]=attaqueequipedeg[y]
            poglemonstats["pog" + str(emplacementMenu) + "attaque" + str(y) + "pp"]=attaqueequipepp[y]
            poglemonstats["pog" + str(emplacementMenu) + "attaque" + str(y) + "pprestant"]=attaqueequipepprestant[y]
            poglemonstats["pog" + str(emplacementMenu) + "attaque" + str(y) + "pre"]=attaqueequipepre[y]

    pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))
    return poglemonstats

def retirePogle(poglemonstats, numeroPog, pogchangeequipe):

    attaqueequipe = {}
    attaqueequipenom = {}
    attaqueequipedeg = {}
    attaqueequipepp = {}
    attaqueequipepprestant = {}
    attaqueequipepre = {}

    attaqueremplace = {}
    attaqueremplacenom = {}
    attaqueremplacedeg = {}
    attaqueremplacepp = {}
    attaqueremplacepprestant = {}
    attaqueremplacepre = {}

    pogechange = poglemonstats["pc" + str(numeroPog)]
    pogechangeid = poglemonstats["pc" + str(numeroPog) + "id"]
    pogechangehp = poglemonstats["pc" + str(numeroPog) + "hp"]
    pogechangehpActuel = poglemonstats["pc" + str(numeroPog) + "hpActuel"]
    pogechangexp = poglemonstats["pc" + str(numeroPog) + "xp"]
    pogechangexpActuel = poglemonstats["pc" + str(numeroPog) + "xpActuel"]
    pogechangeatk = poglemonstats["pc" + str(numeroPog) + "atk"]
    pogechangespatk = poglemonstats["pc" + str(numeroPog) + "spatk"]
    pogechangedef = poglemonstats["pc" + str(numeroPog) + "def"]
    pogechangespdef = poglemonstats["pc" + str(numeroPog) + "spdef"]
    pogechangevit = poglemonstats["pc" + str(numeroPog) + "vit"]
    pogechangeniv = poglemonstats["pc" + str(numeroPog) + "niv"]
    pogechangetype1 = poglemonstats["pc" + str(numeroPog) + "type1"]
    pogechangetype2 = poglemonstats.get("pc" + str(numeroPog) + "type2")
    pogechangename = poglemonstats["pc" + str(numeroPog) + "name"]
    for y in range(1,5):
            attaqueremplace[y] = poglemonstats.get("pc" + str(numeroPog) + "attaque" + str(y))
            attaqueremplacenom[y] = poglemonstats.get("pc" + str(numeroPog) + "attaque" + str(y) + "nom")
            attaqueremplacedeg[y] = poglemonstats.get("pc" + str(numeroPog) + "attaque" + str(y) + "deg")
            attaqueremplacepp[y] = poglemonstats.get("pc" + str(numeroPog) + "attaque" + str(y) + "pp")
            attaqueremplacepprestant[y] = poglemonstats.get("pc" + str(numeroPog) + "attaque" + str(y) + "pprestant")
            attaqueremplacepre[y] = poglemonstats.get("pc" + str(numeroPog) + "attaque" + str(y) + "pre")

    if pogchangeequipe != 999:

        pogequipestats = poglemonstats.get("pog" + str(pogchangeequipe))

        if pogequipestats != None:

            pogequipe = poglemonstats["pog" + str(pogchangeequipe)]
            pogequipeid = poglemonstats["pog" + str(pogchangeequipe) + "id"]
            pogequipehp = poglemonstats["pog" + str(pogchangeequipe) + "hp"]
            pogequipehpActuel = poglemonstats["pog" + str(pogchangeequipe) + "hpActuel"]
            pogequipexp = poglemonstats["pog" + str(pogchangeequipe) + "xp"]
            pogequipexpActuel = poglemonstats["pog" + str(pogchangeequipe) + "xpActuel"]
            pogequipeatk = poglemonstats["pog" + str(pogchangeequipe) + "atk"]
            pogequipespatk = poglemonstats["pog" + str(pogchangeequipe) + "spatk"]
            pogequipedef = poglemonstats["pog" + str(pogchangeequipe) + "def"]
            pogequipespdef = poglemonstats["pog" + str(pogchangeequipe) + "spdef"]
            pogequipevit = poglemonstats["pog" + str(pogchangeequipe) + "vit"]
            pogequipeniv = poglemonstats["pog" + str(pogchangeequipe) + "niv"]
            pogequipetype1 = poglemonstats["pog" + str(pogchangeequipe) + "type1"]
            pogequipetype2 = poglemonstats.get("pog" + str(pogchangeequipe) + "type2")
            pogequipename = poglemonstats["pog" + str(pogchangeequipe) + "name"]

            for y in range(1,5):
                    attaqueequipe[y] = poglemonstats.get("pog" + str(pogchangeequipe) + "attaque" + str(y))
                    attaqueequipenom[y] = poglemonstats.get("pog" + str(pogchangeequipe) + "attaque" + str(y) + "nom")
                    attaqueequipedeg[y] = poglemonstats.get("pog" + str(pogchangeequipe) + "attaque" + str(y) + "deg")
                    attaqueequipepp[y] = poglemonstats.get("pog" + str(pogchangeequipe) + "attaque" + str(y) + "pp")
                    attaqueequipepprestant[y] = poglemonstats.get("pog" + str(pogchangeequipe) + "attaque" + str(y) + "pprestant")
                    attaqueequipepre[y] = poglemonstats.get("pog" + str(pogchangeequipe) + "attaque" + str(y) + "pre")

            poglemonstats["pc" + str(numeroPog)] = pogequipe
            poglemonstats["pc" + str(numeroPog) + "id"] = pogequipeid
            poglemonstats["pc" + str(numeroPog) + "hp"] = pogequipehp
            poglemonstats["pc" + str(numeroPog) + "hpActuel"] = pogequipehpActuel
            poglemonstats["pc" + str(numeroPog) + "xp"] = pogequipexp
            poglemonstats["pc" + str(numeroPog) + "xpActuel"] = pogequipexpActuel
            poglemonstats["pc" + str(numeroPog) + "atk"] = pogequipeatk
            poglemonstats["pc" + str(numeroPog) + "spatk"] = pogequipespatk
            poglemonstats["pc" + str(numeroPog) + "def"] = pogequipedef
            poglemonstats["pc" + str(numeroPog) + "spdef"] = pogequipespdef
            poglemonstats["pc" + str(numeroPog) + "vit"] = pogequipevit
            poglemonstats["pc" + str(numeroPog) + "niv"] = pogequipeniv
            poglemonstats["pc" + str(numeroPog) + "type1"] = pogequipetype1
            poglemonstats["pc" + str(numeroPog) + "type2"] = pogequipetype2
            poglemonstats["pc" + str(numeroPog) + "name"] = pogequipename
            for y in range(1,5):
                    poglemonstats["pc" + str(numeroPog) + "attaque" + str(y)]=attaqueequipe[y]
                    poglemonstats["pc" + str(numeroPog) + "attaque" + str(y) + "nom"]=attaqueequipenom[y]
                    poglemonstats["pc" + str(numeroPog) + "attaque" + str(y) + "deg"]=attaqueequipedeg[y]
                    poglemonstats["pc" + str(numeroPog) + "attaque" + str(y) + "pp"]=attaqueequipepp[y]
                    poglemonstats["pc" + str(numeroPog) + "attaque" + str(y) + "pprestant"]=attaqueequipepprestant[y]
                    poglemonstats["pc" + str(numeroPog) + "attaque" + str(y) + "pre"]=attaqueequipepre[y]

        poglemonstats["pog" + str(pogchangeequipe)] = pogechange
        poglemonstats["pog" + str(pogchangeequipe) + "id"] = pogechangeid
        poglemonstats["pog" + str(pogchangeequipe) + "hp"] = pogechangehp
        poglemonstats["pog" + str(pogchangeequipe) + "hpActuel"] = pogechangehpActuel
        poglemonstats["pog" + str(pogchangeequipe) + "xp"] = pogechangexp
        poglemonstats["pog" + str(pogchangeequipe) + "xpActuel"] = pogechangexpActuel
        poglemonstats["pog" + str(pogchangeequipe) + "atk"] = pogechangeatk
        poglemonstats["pog" + str(pogchangeequipe) + "spatk"] = pogechangespatk
        poglemonstats["pog" + str(pogchangeequipe) + "def"] = pogechangedef
        poglemonstats["pog" + str(pogchangeequipe) + "spdef"] = pogechangespdef
        poglemonstats["pog" + str(pogchangeequipe) + "vit"] = pogechangevit
        poglemonstats["pog" + str(pogchangeequipe) + "niv"] = pogechangeniv
        poglemonstats["pog" + str(pogchangeequipe) + "type1"] = pogechangetype1
        poglemonstats["pog" + str(pogchangeequipe) + "type2"] = pogechangetype2
        poglemonstats["pog" + str(pogchangeequipe) + "name"] = pogechangename
        for y in range(1,5):
                poglemonstats["pog" + str(pogchangeequipe) + "attaque" + str(y)]=attaqueremplace[y]
                poglemonstats["pog" + str(pogchangeequipe) + "attaque" + str(y) + "nom"]=attaqueremplacenom[y]
                poglemonstats["pog" + str(pogchangeequipe) + "attaque" + str(y) + "deg"]=attaqueremplacedeg[y]
                poglemonstats["pog" + str(pogchangeequipe) + "attaque" + str(y) + "pp"]=attaqueremplacepp[y]
                poglemonstats["pog" + str(pogchangeequipe) + "attaque" + str(y) + "pprestant"]=attaqueremplacepprestant[y]
                poglemonstats["pog" + str(pogchangeequipe) + "attaque" + str(y) + "pre"]=attaqueremplacepre[y]

        if pogequipestats == None:

            poglemonstats["pc" + str(numeroPog)] = None
            poglemonstats["pc" + str(numeroPog) + "id"] = None
            poglemonstats["pc" + str(numeroPog) + "hp"] = None
            poglemonstats["pc" + str(numeroPog) + "hpActuel"] = None
            poglemonstats["pc" + str(numeroPog) + "xp"] = None
            poglemonstats["pc" + str(numeroPog) + "xpActuel"] = None
            poglemonstats["pc" + str(numeroPog) + "atk"] = None
            poglemonstats["pc" + str(numeroPog) + "spatk"] = None
            poglemonstats["pc" + str(numeroPog) + "def"] = None
            poglemonstats["pc" + str(numeroPog) + "spdef"] = None
            poglemonstats["pc" + str(numeroPog) + "vit"] = None
            poglemonstats["pc" + str(numeroPog) + "niv"] =None
            poglemonstats["pc" + str(numeroPog) + "type1"] = None
            poglemonstats["pc" + str(numeroPog) + "type2"] = None
            poglemonstats["pc" + str(numeroPog) + "name"] = None
            for y in range(1,5):
                    poglemonstats["pc" + str(numeroPog) + "attaque" + str(y)]=None
                    poglemonstats["pc" + str(numeroPog) + "attaque" + str(y) + "nom"]=None
                    poglemonstats["pc" + str(numeroPog) + "attaque" + str(y) + "deg"]=None
                    poglemonstats["pc" + str(numeroPog) + "attaque" + str(y) + "pp"]=None
                    poglemonstats["pc" + str(numeroPog) + "attaque" + str(y) + "pprestant"]=None
                    poglemonstats["pc" + str(numeroPog) + "attaque" + str(y) + "pre"]=None

    pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))
    return poglemonstats

def posePogle(pogchangeequipe, poglemonstats, x):

    attaqueequipe = {}
    attaqueequipenom = {}
    attaqueequipedeg = {}
    attaqueequipepp = {}
    attaqueequipepprestant = {}
    attaqueequipepre = {}

    pogequipe = poglemonstats["pog" + str(pogchangeequipe)]
    pogequipeid = poglemonstats["pog" + str(pogchangeequipe) + "id"]
    pogequipehp = poglemonstats["pog" + str(pogchangeequipe) + "hp"]
    pogequipehpActuel = poglemonstats["pog" + str(pogchangeequipe) + "hpActuel"]
    pogequipexp = poglemonstats["pog" + str(pogchangeequipe) + "xp"]
    pogequipexpActuel = poglemonstats["pog" + str(pogchangeequipe) + "xpActuel"]
    pogequipeatk = poglemonstats["pog" + str(pogchangeequipe) + "atk"]
    pogequipespatk = poglemonstats["pog" + str(pogchangeequipe) + "spatk"]
    pogequipedef = poglemonstats["pog" + str(pogchangeequipe) + "def"]
    pogequipespdef = poglemonstats["pog" + str(pogchangeequipe) + "spdef"]
    pogequipevit = poglemonstats["pog" + str(pogchangeequipe) + "vit"]
    pogequipeniv = poglemonstats["pog" + str(pogchangeequipe) + "niv"]
    pogequipetype1 = poglemonstats["pog" + str(pogchangeequipe) + "type1"]
    pogequipetype2 = poglemonstats.get("pog" + str(pogchangeequipe) + "type2")
    pogequipename = poglemonstats["pog" + str(pogchangeequipe) + "name"]
    for y in range(1,5):
            attaqueequipe[y] = poglemonstats.get("pog" + str(pogchangeequipe) + "attaque" + str(y))
            attaqueequipenom[y] = poglemonstats.get("pog" + str(pogchangeequipe) + "attaque" + str(y) + "nom")
            attaqueequipedeg[y] = poglemonstats.get("pog" + str(pogchangeequipe) + "attaque" + str(y) + "deg")
            attaqueequipepp[y] = poglemonstats.get("pog" + str(pogchangeequipe) + "attaque" + str(y) + "pp")
            attaqueequipepprestant[y] = poglemonstats.get("pog" + str(pogchangeequipe) + "attaque" + str(y) + "pprestant")
            attaqueequipepre[y] = poglemonstats.get("pog" + str(pogchangeequipe) + "attaque" + str(y) + "pre")

    poglemonstats["pc" + str(x)] = pogequipe
    poglemonstats["pc" + str(x) + "id"] = pogequipeid
    poglemonstats["pc" + str(x) + "hp"] = pogequipehp
    poglemonstats["pc" + str(x) + "hpActuel"] = pogequipehpActuel
    poglemonstats["pc" + str(x) + "xp"] = pogequipexp
    poglemonstats["pc" + str(x) + "xpActuel"] = pogequipexpActuel
    poglemonstats["pc" + str(x) + "atk"] = pogequipeatk
    poglemonstats["pc" + str(x) + "spatk"] = pogequipespatk
    poglemonstats["pc" + str(x) + "def"] = pogequipedef
    poglemonstats["pc" + str(x) + "spdef"] = pogequipespdef
    poglemonstats["pc" + str(x) + "vit"] = pogequipevit
    poglemonstats["pc" + str(x) + "niv"] = pogequipeniv
    poglemonstats["pc" + str(x) + "type1"] = pogequipetype1
    poglemonstats["pc" + str(x) + "type2"] = pogequipetype2
    poglemonstats["pc" + str(x) + "name"] = pogequipename
    for y in range(1,5):
            poglemonstats["pc" + str(x) + "attaque" + str(y)]=attaqueequipe[y]
            poglemonstats["pc" + str(x) + "attaque" + str(y) + "nom"]=attaqueequipenom[y]
            poglemonstats["pc" + str(x) + "attaque" + str(y) + "deg"]=attaqueequipedeg[y]
            poglemonstats["pc" + str(x) + "attaque" + str(y) + "pp"]=attaqueequipepp[y]
            poglemonstats["pc" + str(x) + "attaque" + str(y) + "pprestant"]=attaqueequipepprestant[y]
            poglemonstats["pc" + str(x) + "attaque" + str(y) + "pre"]=attaqueequipepre[y]

    poglemonstats["pog" + str(pogchangeequipe)] = None
    poglemonstats["pog" + str(pogchangeequipe) + "id"] = None
    poglemonstats["pog" + str(pogchangeequipe) + "hp"] = None
    poglemonstats["pog" + str(pogchangeequipe) + "hpActuel"] = None
    poglemonstats["pog" + str(pogchangeequipe) + "xp"] = None
    poglemonstats["pog" + str(pogchangeequipe) + "xpActuel"] = None
    poglemonstats["pog" + str(pogchangeequipe) + "atk"] = None
    poglemonstats["pog" + str(pogchangeequipe) + "spatk"] = None
    poglemonstats["pog" + str(pogchangeequipe) + "def"]= None
    poglemonstats["pog" + str(pogchangeequipe) + "spdef"] = None
    poglemonstats["pog" + str(pogchangeequipe) + "vit"]= None
    poglemonstats["pog" + str(pogchangeequipe) + "niv"]= None
    poglemonstats["pog" + str(pogchangeequipe) + "type1"] = None
    poglemonstats["pog" + str(pogchangeequipe) + "type2"]= None
    poglemonstats["pog" + str(pogchangeequipe) + "name"]= None
    for y in range(1,5):
            poglemonstats["pog" + str(pogchangeequipe) + "attaque" + str(y)]=None
            poglemonstats["pog" + str(pogchangeequipe) + "attaque" + str(y) + "nom"]=None
            poglemonstats["pog" + str(pogchangeequipe) + "attaque" + str(y) + "deg"]=None
            poglemonstats["pog" + str(pogchangeequipe) + "attaque" + str(y) + "pp"]=None
            poglemonstats["pog" + str(pogchangeequipe) + "attaque" + str(y) + "pprestant"]=None
            poglemonstats["pog" + str(pogchangeequipe) + "attaque" + str(y) + "pre"]=None

    pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))
    return poglemonstats

def deplacePoglePC(poglemonstats, pogdeplace, emplacementBoite2):

    attaqueequipe = {}
    attaqueequipenom = {}
    attaqueequipedeg = {}
    attaqueequipepp = {}
    attaqueequipepprestant = {}
    attaqueequipepre = {}

    attaqueremplace = {}
    attaqueremplacenom = {}
    attaqueremplacedeg = {}
    attaqueremplacepp = {}
    attaqueremplacepprestant = {}
    attaqueremplacepre = {}

    pogequipe = poglemonstats["pc" + str(pogdeplace)]
    pogequipeid = poglemonstats["pc" + str(pogdeplace) +"id"]
    pogequipehp = poglemonstats["pc" + str(pogdeplace) + "hp"]
    pogequipehpActuel = poglemonstats["pc" + str(pogdeplace) + "hpActuel"]
    pogequipexp = poglemonstats["pc" + str(pogdeplace) + "xp"]
    pogequipexpActuel = poglemonstats["pc" + str(pogdeplace) + "xpActuel"]
    pogequipeatk = poglemonstats["pc" + str(pogdeplace) + "atk"]
    pogequipespatk = poglemonstats["pc" + str(pogdeplace) + "spatk"]
    pogequipedef = poglemonstats["pc" + str(pogdeplace) + "def"]
    pogequipespdef = poglemonstats["pc" + str(pogdeplace) + "spdef"]
    pogequipevit = poglemonstats["pc" + str(pogdeplace) + "vit"]
    pogequipeniv = poglemonstats["pc" + str(pogdeplace) + "niv"]
    pogequipetype1 = poglemonstats["pc" + str(pogdeplace) + "type1"]
    pogequipetype2 = poglemonstats.get("pc" + str(pogdeplace) + "type2")
    pogequipename = poglemonstats["pc" + str(pogdeplace) + "name"]
    for y in range(1,5):
            attaqueequipe[y] = poglemonstats.get("pc" + str(pogdeplace) + "attaque" + str(y))
            attaqueequipenom[y] = poglemonstats.get("pc" + str(pogdeplace) + "attaque" + str(y) + "nom")
            attaqueequipedeg[y] = poglemonstats.get("pc" + str(pogdeplace) + "attaque" + str(y) + "deg")
            attaqueequipepp[y] = poglemonstats.get("pc" + str(pogdeplace) + "attaque" + str(y) + "pp")
            attaqueequipepprestant[y] = poglemonstats.get("pc" + str(pogdeplace) + "attaque" + str(y) + "pprestant")
            attaqueequipepre[y] = poglemonstats.get("pc" + str(pogdeplace) + "attaque" + str(y) + "pre")


    if poglemonstats.get("pc"+str(emplacementBoite2)) != None:

        pogremplace = poglemonstats["pc" + str(emplacementBoite2)]
        pogremplaceid = poglemonstats["pc" + str(emplacementBoite2) + "id"]
        pogremplacehp = poglemonstats["pc" + str(emplacementBoite2) + "hp"]
        pogremplacehpActuel = poglemonstats["pc" + str(emplacementBoite2) + "hpActuel"]
        pogremplacexp = poglemonstats["pc" + str(emplacementBoite2) + "xp"]
        pogremplacexpActuel = poglemonstats["pc" + str(emplacementBoite2) + "xpActuel"]
        pogremplaceatk = poglemonstats["pc" + str(emplacementBoite2) + "atk"]
        pogremplacespatk = poglemonstats["pc" + str(emplacementBoite2) + "spatk"]
        pogremplacedef = poglemonstats["pc" + str(emplacementBoite2) + "def"]
        pogremplacespdef = poglemonstats["pc" + str(emplacementBoite2) + "spdef"]
        pogremplacevit = poglemonstats["pc" + str(emplacementBoite2) + "vit"]
        pogremplaceniv = poglemonstats["pc" + str(emplacementBoite2) + "niv"]
        pogremplacetype1 = poglemonstats["pc" + str(emplacementBoite2) + "type1"]
        pogremplacetype2 = poglemonstats.get("pc" + str(emplacementBoite2) + "type2")
        pogremplacename = poglemonstats["pc" + str(emplacementBoite2) + "name"]
        for y in range(1,5):
                attaqueremplace[y] = poglemonstats.get("pc" + str(emplacementBoite2) + "attaque" + str(y))
                attaqueremplacenom[y] = poglemonstats.get("pc" + str(emplacementBoite2) + "attaque" + str(y) + "nom")
                attaqueremplacedeg[y] = poglemonstats.get("pc" + str(emplacementBoite2) + "attaque" + str(y) + "deg")
                attaqueremplacepp[y] = poglemonstats.get("pc" + str(emplacementBoite2) + "attaque" + str(y) + "pp")
                attaqueremplacepprestant[y] = poglemonstats.get("pc" + str(emplacementBoite2) + "attaque" + str(y) + "pprestant")
                attaqueremplacepre[y] = poglemonstats.get("pc" + str(emplacementBoite2) + "attaque" + str(y) + "pre")

        poglemonstats["pc" + str(pogdeplace)] = pogremplace
        poglemonstats["pc" + str(pogdeplace) + "id"] = pogremplaceid
        poglemonstats["pc" + str(pogdeplace) + "hp"] = pogremplacehp
        poglemonstats["pc" + str(pogdeplace) + "hpActuel"] = pogremplacehpActuel
        poglemonstats["pc" + str(pogdeplace) + "xp"] = pogremplacexp
        poglemonstats["pc" + str(pogdeplace) + "xpActuel"] = pogremplacexpActuel
        poglemonstats["pc" + str(pogdeplace) + "atk"] = pogremplaceatk
        poglemonstats["pc" + str(pogdeplace) + "spatk"] = pogremplacespatk
        poglemonstats["pc" + str(pogdeplace) + "def"] = pogremplacedef
        poglemonstats["pc" + str(pogdeplace) + "spdef"] = pogremplacespdef
        poglemonstats["pc" + str(pogdeplace) + "vit"] = pogremplacevit
        poglemonstats["pc" + str(pogdeplace) + "niv"] = pogremplaceniv
        poglemonstats["pc" + str(pogdeplace) + "type1"] = pogremplacetype1
        poglemonstats["pc" + str(pogdeplace) + "type2"] = pogremplacetype2
        poglemonstats["pc" + str(pogdeplace) + "name"] = pogremplacename
        for y in range(1,5):
                poglemonstats["pc" + str(pogdeplace) + "attaque" + str(y)]=attaqueremplace[y]
                poglemonstats["pc" + str(pogdeplace) + "attaque" + str(y) + "nom"]=attaqueremplacenom[y]
                poglemonstats["pc" + str(pogdeplace) + "attaque" + str(y) + "deg"]=attaqueremplacedeg[y]
                poglemonstats["pc" + str(pogdeplace) + "attaque" + str(y) + "pp"]=attaqueremplacepp[y]
                poglemonstats["pc" + str(pogdeplace) + "attaque" + str(y) + "pprestant"]=attaqueremplacepprestant[y]
                poglemonstats["pc" + str(pogdeplace) + "attaque" + str(y) + "pre"]=attaqueremplacepre[y]

    if poglemonstats.get("pc"+str(emplacementBoite2)) == None:

        poglemonstats["pc" + str(pogdeplace)] = None
        poglemonstats["pc" + str(pogdeplace) + "id"] = None
        poglemonstats["pc" + str(pogdeplace) + "hp"] = None
        poglemonstats["pc" + str(pogdeplace) + "hpActuel"] = None
        poglemonstats["pc" + str(pogdeplace) + "xp"] = None
        poglemonstats["pc" + str(pogdeplace) + "xpActuel"] = None
        poglemonstats["pc" + str(pogdeplace) + "atk"] = None
        poglemonstats["pc" + str(pogdeplace) + "spatk"] = None
        poglemonstats["pc" + str(pogdeplace) + "def"] = None
        poglemonstats["pc" + str(pogdeplace) + "spdef"] = None
        poglemonstats["pc" + str(pogdeplace) + "vit"] = None
        poglemonstats["pc" + str(pogdeplace) + "niv"] = None
        poglemonstats["pc" + str(pogdeplace) + "type1"] = None
        poglemonstats["pc" + str(pogdeplace) + "type2"] = None
        poglemonstats["pc" + str(pogdeplace) + "name"] = None
        for y in range(1,5):
                poglemonstats["pc" + str(pogdeplace) + "attaque" + str(y)]=None
                poglemonstats["pc" + str(pogdeplace) + "attaque" + str(y) + "nom"]=None
                poglemonstats["pc" + str(pogdeplace) + "attaque" + str(y) + "deg"]=None
                poglemonstats["pc" + str(pogdeplace) + "attaque" + str(y) + "pp"]=None
                poglemonstats["pc" + str(pogdeplace) + "attaque" + str(y) + "pprestant"]=None
                poglemonstats["pc" + str(pogdeplace) + "attaque" + str(y) + "pre"]=None


    poglemonstats["pc" + str(emplacementBoite2)] = pogequipe
    poglemonstats["pc" + str(emplacementBoite2) + "id"] = pogequipeid
    poglemonstats["pc" + str(emplacementBoite2) + "hp"] = pogequipehp
    poglemonstats["pc" + str(emplacementBoite2) + "hpActuel"] = pogequipehpActuel
    poglemonstats["pc" + str(emplacementBoite2) + "xp"] = pogequipexp
    poglemonstats["pc" + str(emplacementBoite2) + "xpActuel"] = pogequipexpActuel
    poglemonstats["pc" + str(emplacementBoite2) + "atk"] = pogequipeatk
    poglemonstats["pc" + str(emplacementBoite2) + "spatk"] = pogequipespatk
    poglemonstats["pc" + str(emplacementBoite2) + "def"] = pogequipedef
    poglemonstats["pc" + str(emplacementBoite2) + "spdef"] = pogequipespdef
    poglemonstats["pc" + str(emplacementBoite2) + "vit"] = pogequipevit
    poglemonstats["pc" + str(emplacementBoite2) + "niv"] = pogequipeniv
    poglemonstats["pc" + str(emplacementBoite2) + "type1"] = pogequipetype1
    poglemonstats["pc" + str(emplacementBoite2) + "type2"] = pogequipetype2
    poglemonstats["pc" + str(emplacementBoite2) + "name"] = pogequipename
    for y in range(1,5):
            poglemonstats["pc" + str(emplacementBoite2) + "attaque" + str(y)]=attaqueequipe[y]
            poglemonstats["pc" + str(emplacementBoite2) + "attaque" + str(y) + "nom"]=attaqueequipenom[y]
            poglemonstats["pc" + str(emplacementBoite2) + "attaque" + str(y) + "deg"]=attaqueequipedeg[y]
            poglemonstats["pc" + str(emplacementBoite2) + "attaque" + str(y) + "pp"]=attaqueequipepp[y]
            poglemonstats["pc" + str(emplacementBoite2) + "attaque" + str(y) + "pprestant"]=attaqueequipepprestant[y]
            poglemonstats["pc" + str(emplacementBoite2) + "attaque" + str(y) + "pre"]=attaqueequipepre[y]

    pickle.dump(poglemonstats, open( "../save/poglemonstats", "wb" ))
    return poglemonstats
