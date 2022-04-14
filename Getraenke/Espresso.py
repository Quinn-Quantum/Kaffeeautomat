from Getraenke.Getraenk import Getraenk
from Zutat.ZutatEspresso import ZutatEspresso


class Espresso(Getraenk):
    def __init__(self):
        zutaten = [ZutatEspresso(1)]
        super(Espresso, self).__init__("Espresso", zutaten)