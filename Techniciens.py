from Employe import Employe

class Technicien(Employe):
    def __init__(self, n, m, a, e, cm):
        super.__init__(n, m, a, e)
        self.corpsMetier = cm


