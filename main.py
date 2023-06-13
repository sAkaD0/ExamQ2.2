from gestionnaireFichier import *

class Menu():
    def main(self):
        print("1. Ajouter Employé")
        print("2. Afficher Employé")
        print("3. Ajouter Attraction avec ses chemins")
        print("4. Récupérer les chemins liés à une Attraction")
        print("5. Quitter")
        choix = input("Votre choix: ")
        return choix

    def choixUser(self, choix):
        if choix == "1":
            chargerMatricules()
            chargerChemins()
            chargerAttractions()
            menu.newEmploye()
        if choix == "2":
            chargerMatricules()
            Employe.get_Employe(employe, input("Entrez un matricule, un nom, ou une équipe: "))
        if choix == "3":
            chargerChemins()
            chargerAttractions()
            menu.newAtt()
        if choix == "4":
            pass
        if choix == "5":
            quit()

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

    def newAtt(self):
        self.nom = input("Entrez un nom d'Attraction: ")
        Attraction.listeAttraction.append(self.nom)

        while 1:
            print(attraction.listeChemin)
            chemin = input("Entrez un chemin: ")
            if chemin == "":
                break
            if chemin in attraction.listeChemin:
                print("Ce chemin est déjà introduit")
            else:
                attraction.listeChemin.append(chemin)
                fs = open("chemin.txt", "a")
                fs.write("\n"+self.nom)

                for chemins in attraction.listeChemin:
                    if chemins.index == len(attraction.listeChemin):
                        fs.write(chemins + "\n")
                    else:
                        fs.write(chemins + "#")

                fs.close()


menu = Menu()
employe = Employe("a", "a", "a", "a")
attraction = Attraction("a")

while True:
    choix = menu.main()
    menu.choixUser(choix)
