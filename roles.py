class Mago:
    pass
class Arquero:
    pass
class Espadachin:
    pass

class Espadachin_Magico(Espadachin, Mago):
    pass
class Espadachin_Arquero(Espadachin, Arquero):
    pass
class Mago_Arquero(Mago, Arquero):
    pass
