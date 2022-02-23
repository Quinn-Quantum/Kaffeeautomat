class Espresso:
    '''
    Erstellt die Classe Espresso
    Variabln:
    String _zutatEspresso
    floate __preis
    int _menge
    '''
    def __init__(self):
        self._zutatEspresso = 'Espresso'
        self.__preis = 1
        self._menge = 1

    def getPreis(self):
        return self.__preis

    def getZutatEspresso(self):
        return self._zutatEspresso

    def getMengeEspresso(self):
        return self._menge

class EspressoMacchiato(Espresso):
    '''
    Erstellt die Classe EspressoMacchiato
    Variabln:
    String _zutatMilchschaum
    floate __preisMilchschaum
    int _mengeMilchschaum
    '''
    def __init__(self):
        self._zutatMilchschaum = 'Milchschaum'
        self.__preisMilchschaums = 1
        self._mengeMilchschaum = 0.5

    def getPreisMilchschaum(self):
        return self.__preisMilchschaum

    def getZutatMilchschaum(self):
        return self._zutatMilchschaum

    def getMengeMilchschaum(self):
        return self._mengeMilchschaum


class Cappuccino(Espresso):
    '''
    Erstellt die Classe Cappuccino
    Variabln:
    String _zutatMilchschaum
    floate __preisMilchschaum
    int _mengeMilchschaum
    String _zutatHeißeMilch
    floate __preisHeißeMilch
    ini _mengeHeißeMilch
    '''

    def __init__(self):
        self._zutatMilchschaum = 'Milchschaum'
        self.__preisMilchschaums = 0.5
        self._mengeMilchschaum = 2
        self._zutatHeißeMilch = 'HeißeMilch'
        self.__preisHeißeMilch = 1
        self._mengeHeißeMilch = 1

    def getPreisMilchschaum(self):
        return self.__preisMilchschaum

    def getZutatMilchschaum(self):
        return self._zutatMilchschaum

    def getMengeMilchschaum(self):
        return self._mengeMilchschaum

    def getPreisHeißeMilch(self):
        return self.__preisHeißeMilch

    def getZutatHeißeMilch(self):
        return self._zutatHeißeMilch
    
    def getMengeHeißeMilch(self):
        return self._mengeHeißeMilch

class CafeLatte(Espresso):
    '''
    Erstellt die Classe CafeLatte
    Variabln:
    String _zutatMilchschaum
    floate __preisMilchschaum
    int _mengeMilchschaum
    String _zutatHeißeMilch
    floate __preisHeißeMilch
    ini _mengeHeißeMilch
    '''

    def __init__(self):
        self._zutatMilchschaum = 'Milchschaum'
        self.__preisMilchschaums = 0.5
        self._mengeMilchschaum = 1
        self._zutatHeißeMilch = 'HeißeMilch'
        self.__preisHeißeMilch = 1
        self._mengeHeißeMilch = 2

    def getPreisMilchschaum(self):
        return self.__preisMilchschaum

    def getZutatMilchschaum(self):
        return self._zutatMilchschaum

    def getMengeMilchschaum(self):
        return self._mengeMilchschaum

    def getPreisHeißeMilch(self):
        return self.__preisHeißeMilch

    def getZutatHeißeMilch(self):
        return self._zutatHeißeMilch

    def getMengeHeißeMilch(self):
        return self._mengeHeißeMilch