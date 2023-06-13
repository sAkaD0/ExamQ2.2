from Attraction import Attraction

class Employe:
    listeMatricule = []
    listeEquipe = []
    def __init__(self, n, m, a, e):
        self.nom = n
        self.matricule = m
        self.attraction = a
        self.equipe = e

    def newEmploye(self):
        self.nom = input("Entrez un nom: ")

        while 1:
            self.matricule = input("Entrez un matricule: ")

            if self.matricule in Employe.listeMatricule:
                print("Le matricule est déjà attribué !")
            else:
                Employe.listeMatricule.append(self.matricule)
                break

        while 1:
            print(Attraction.listeAttraction)
            attraction = input("Entrez une attraction: ")

            if attraction in Attraction.listeAttraction:
                self.attraction = attraction
                break
            else :
                print("Cette Attraction n'existe pas !")


        print("Voici la liste des équipes :", Employe.listeEquipe, "\n", "Si elle n'est pas créée, entrer le nom de votre équipe.")
        self.equipe = input("Nom de l'équipe: ")
        if self.equipe in Employe.listeEquipe:
            pass
        else :
            Employe.listeEquipe.append(self.equipe)

        fs = open("users.txt", "a")
        fs.write(self.nom+"#"+self.matricule+"#"+self.attraction+"#"+self.equipe+"\n")
        fs.close()


    def get_Employe(self, key):

        with open("users.txt", "r") as fs:
            for row in fs:
                if key in row:
                    print(row.strip().split("#"))
            return None