class CafeLatte():
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
        self.__name = 'CafeLatte'
        self._zutatMilchschaum = 'Milchschaum'
        self.__preisMilchschaum = 0.5
        self._mengeMilchschaum = 1
        self._zutatHeißeMilch = 'HeißeMilch'
        self.__preisHeißeMilch = 1
        self._mengeHeißeMilch = 2

    def getName(self):
        return self.__name

    def getPreisMilchschaum2(self):
        return self.__preisMilchschaum

    def getZutatMilchschaum2(self):
        return self._zutatMilchschaum

    def getMengeMilchschaum2(self):
        return self._mengeMilchschaum

    def getPreisHeißeMilch2(self):
        return self.__preisHeißeMilch

    def getZutatHeißeMilch2(self):
        return self._zutatHeißeMilch

    def getMengeHeißeMilch2(self):
        return self._mengeHeißeMilch
