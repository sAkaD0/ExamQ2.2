from Employe import Employe

class Soigneur(Employe):
    def __init__(self, n, m, a, e, s, num):
        super.__init__(n, m, a, e)
        self.specialisation = s
        self.numUrgence = num
