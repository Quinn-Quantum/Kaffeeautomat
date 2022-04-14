from Getraenke.Getraenk import Getraenk
from Zutat.ZutatEspresso import ZutatEspresso
from Zutat.ZutatHeisseMilch import ZutatHeisseMilch
from Zutat.ZutatMilchschaum import ZutatMilchschaum


class Cappuccino(Getraenk):
    def __init__(self):
        zutaten = [ZutatEspresso(1), ZutatHeisseMilch(1), ZutatMilchschaum(2)]
        super(Cappuccino, self).__init__("Cappuccino", zutaten)