class Espresso:
    '''
    Erstellt die Klasse Espresso
    Variablen:
    String _zutatEspresso
    floate __preis
    int _menge
    '''
    def __init__(self):
        self.__name ='Espresso'
        self._zutatEspresso = 'Espresso'
        self.__preis = 1
        self._menge = 1

    def getName(self):
        return self.__name

    def getPreisEspresso(self):
        return self.__preis

    def getZutatEspresso(self):
        return self._zutatEspresso

    def getMengeEspresso(self):
        return self._menge