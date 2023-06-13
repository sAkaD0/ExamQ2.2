from Attraction import Attraction

class Employe:
    listeMatricule = []
    listeEquipe = []
    def __init__(self, n, m, a, e):
        self.nom = n
        self.matricule = m
        self.attraction = a
        self.equipe = e

    def get_Employe(self, key):

        with open("users.txt", "r") as fs:
            for row in fs:
                if key in row:
                    print(row.strip().split("#"))
            return None