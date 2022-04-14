from Zutat.Zutat import Zutat


class ZutatMilchschaum(Zutat):
    def __init__(self, menge):
        preis = 0.5
        super(ZutatMilchschaum, self).__init__("Milchschaum", menge, preis)