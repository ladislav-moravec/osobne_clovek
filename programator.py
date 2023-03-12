from clovek import Clovek

class Programator(Clovek):

    def __init__(self, jmeno, vek, jazyk):
        super().__init__(jmeno, vek)
        self.jazyk = jazyk

    def pozdrav(self, kolikrat=None):
        if kolikrat == None:
            print("Hello World")
        else:
            super().pozdrav(kolikrat)
