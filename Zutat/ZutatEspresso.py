from Zutat.Zutat import Zutat


class ZutatEspresso(Zutat):
    def __init__(self, menge):
        preis = 1
        super(ZutatEspresso, self).__init__("Espresso", menge, preis)