from Employe import Employe
from Attraction import Attraction

def chargerMatricules():

    fs = open("users.txt", "r")
    rows = fs.readlines()

    for matricules in rows:
        Employe.listeMatricule.append(matricules.strip().split("#")[1])

    fs.close()

def chargerAttractions():

    fs = open("chemin.txt", "r")
    rows = fs.readlines()

    for attractions in rows:
        Attraction.listeAttraction.append(attractions.strip().split("#")[0])

    fs.close()

def chargerChemins():

    fs = open("chemin.txt", "r")
    rows = fs.readlines()

    for chemins in rows:
        Attraction.listeAttraction.append(chemins.strip().split("#")[1:])

    fs.close()