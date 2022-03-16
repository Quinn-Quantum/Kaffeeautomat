class EspressoMacchiato:
    '''
    Erstellt die Classe EspressoMacchiato
    Variabln:
    String _zutatMilchschaum
    floate __preisMilchschaum
    int _mengeMilchschaum
    '''
    def __init__(self):
        self.__name = 'Espresso Macchiato'
        self._zutatMilchschaum = 'Milchschaum'
        self.__preisMilchschaum = 1
        self._mengeMilchschaum = 0.5

    def getName(self):
        return self.__name

    def getPreisMilchschaum(self):
        return self.__preisMilchschaum

    def getZutatMilchschaum(self):
        return self._zutatMilchschaum

    def getMengeMilchschaum(self):
        return self._mengeMilchschaum
