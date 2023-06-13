class Attraction:
    listeAttraction = []
    def __init__(self, n):
        self.nom = n
        self.listeChemin = []

    def newAtt(self):
        self.nom = input("Entrez un nom d'Attraction: ")
        Attraction.listeAttraction.append(self.nom)

        while 1:
            print(self.listeChemin)
            chemin = input("Entrez un chemin: ")
            if chemin == "":
                break
            if chemin in self.listeChemin:
                print("Ce chemin est déjà introduit")
            else:
                self.listeChemin.append(chemin)
                fs = open("chemin.txt", "a")
                fs.write("\n"+self.nom)

                for chemins in self.listeChemin:
                    if chemins.index == len(self.listeChemin):
                        fs.write(chemins + "\n")
                    else:
                        fs.write(chemins + "#")

                fs.close()
