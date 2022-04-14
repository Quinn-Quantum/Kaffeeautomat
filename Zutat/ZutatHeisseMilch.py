from Zutat.Zutat import Zutat


class ZutatHeisseMilch(Zutat):
    def __init__(self, menge):
        preis = 1
        super(ZutatHeisseMilch, self).__init__("Heiße Milch", menge, preis)