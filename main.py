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
            employe.newEmploye()
        if choix == "2":
            chargerMatricules()
            Employe.get_Employe(employe, input("Entrez un matricule, un nom, ou une équipe: "))
        if choix == "3":
            chargerChemins()
            chargerAttractions()
            attraction.newAtt()
        if choix == "4":
            pass
        if choix == "5":
            quit()


menu = Menu()
employe = Employe("a", "a", "a", "a")
attraction = Attraction("a")

while True:
    choix = menu.main()
    menu.choixUser(choix)
