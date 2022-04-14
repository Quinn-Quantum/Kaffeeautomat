class Getraenk:

    __name = ""
    __grundpreis = 0.5
    __zutaten = []

    def __init__(self, name, zutaten):
        self.__name = name
        self.__zutaten = zutaten

    def getPreis(self):
        preisZutaten = 0
        for zutat in self.__zutaten:
            preisZutaten += zutat.getPreis()
        return self.__grundpreis + preisZutaten

    def getName(self):
        return self.__name

    def getZutaten(self):
        return self.__zutaten