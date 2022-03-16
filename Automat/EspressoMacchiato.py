class EspressoMacchiato:
    '''
    Erstellt die Klasse EspressoMacchiato
    Variablen:
    String _zutatMilchschaum
    floate __preisMilchschaum
    int _mengeMilchschaum
    '''
    def __init__(self):
        self.__name = 'Espresso Macchiato'
        self._zutatMilchschaum = 'Milchschaum'
        self.__preisMilchschaum = 0.5
        self._mengeMilchschaum = 1

    def getName(self):
        return self.__name

    def getPreisMilchschaum(self):
        return self.__preisMilchschaum

    def getZutatMilchschaum(self):
        return self._zutatMilchschaum

    def getMengeMilchschaum(self):
        return self._mengeMilchschaum
