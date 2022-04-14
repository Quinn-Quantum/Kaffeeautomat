from Getraenke.Getraenk import Getraenk
from Zutat.ZutatEspresso import ZutatEspresso
from Zutat.ZutatHeisseMilch import ZutatHeisseMilch
from Zutat.ZutatMilchschaum import ZutatMilchschaum


class CafeLatte(Getraenk):
    def __init__(self):
        zutaten = [ZutatEspresso(1), ZutatHeisseMilch(2), ZutatMilchschaum(1)]
        super(CafeLatte, self).__init__("CafeLatte", zutaten)