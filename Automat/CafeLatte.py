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
        self.__zutatMilchschaum = 'Milchschaum'
        self.__preisMilchschaum = 0.5
        self.__mengeMilchschaum = 1
        self.__zutatHeißeMilch = 'HeißeMilch'
        self.__preisHeißeMilch = 1
        self.__mengeHeißeMilch = 2

    def getName(self):
        return self.__name

    def getPreisMilchschaum2(self):
        return self.__preisMilchschaum

    def getZutatMilchschaum2(self):
        return self.__zutatMilchschaum

    def getMengeMilchschaum2(self):
        return self.__mengeMilchschaum

    def getPreisHeißeMilch2(self):
        return self.__preisHeißeMilch

    def getZutatHeißeMilch2(self):
        return self.__zutatHeißeMilch

    def getMengeHeißeMilch2(self):
        return self.__mengeHeißeMilch
