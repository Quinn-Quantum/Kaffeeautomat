class Cappuccino():
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
        self.__name = 'Cappuccino'
        self._zutatMilchschaum = 'Milchschaum'
        self.__preisMilchschaum = 0.5
        self._mengeMilchschaum = 2
        self._zutatHeißeMilch = 'HeißeMilch'
        self.__preisHeißeMilch = 1
        self._mengeHeißeMilch = 1

    def getName(self):
        return self.__name

    def getPreisMilchschaum1(self):
        return self.__preisMilchschaum

    def getZutatMilchschaum1(self):
        return self._zutatMilchschaum

    def getMengeMilchschaum1(self):
        return self._mengeMilchschaum

    def getPreisHeißeMilch1(self):
        return self.__preisHeißeMilch

    def getZutatHeißeMilch1(self):
        return self._zutatHeißeMilch

    def getMengeHeißeMilch1(self):
        return self._mengeHeißeMilch