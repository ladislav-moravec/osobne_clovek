class Clovek:


    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def pozdrav(self, kolikrat=2):
        print("Ahoj, jsem {} {} a je mi {} let.\n".format(
            self.barva,
            self.jmeno,
            self.vek
        ) * kolikrat)
