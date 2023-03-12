from clovek import Clovek
from programator import Programator

karel = Clovek("Karel", 42)
karel.barva = "černý"
karel.jmeno = "Jan"
karel.vek = 22
print(karel)
karel.pozdrav()

martin = Programator("Martin", 111, "Python")
martin.barva = "bílý"
martin.jmeno = "Martin Malý"
martin.vek = 112
print(martin)
martin.pozdrav()
martin.pozdrav(4)



