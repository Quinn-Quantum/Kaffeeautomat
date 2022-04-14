from Getraenke.Getraenk import Getraenk
from Zutat.ZutatEspresso import ZutatEspresso
from Zutat.ZutatMilchschaum import ZutatMilchschaum


class EspressoMacchiato(Getraenk):
    def __init__(self):
        zutaten = [ZutatEspresso(1), ZutatMilchschaum(1)]
        super(EspressoMacchiato, self).__init__("EspressoMacchiato", zutaten)