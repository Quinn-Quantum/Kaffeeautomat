class Bestand:
    __iZutat1 = 0
    __iZutat2 = 0
    __iZutat3 = 0

    __sZutat1 = ""
    __sZutat2 = ""
    __sZutat3 = ""

    __fZutat1 = 0.0
    __fZutat2 = 0.0
    __fZutat3 = 0.0

    def __init__(self,sZutat1, iZutat1,fZutat1,sZutat2, iZutat2, fZutat2,sZutat3, iZutat3, fZutat3):
        self.__sZutat1 = sZutat1
        self.__iZutat1 = iZutat1
        self.__fZutat1 = fZutat1

        self.__sZutat2 = sZutat2
        self.__iZutat2 = iZutat2
        self.__fZutat2 = fZutat2

        self.__sZutat3 = sZutat3
        self.__iZutat3 = iZutat3
        self.__fZutat3 = fZutat3

    # get Menge
    def getIZutat1(self):
        return self.__iZutat1

    def getIZutat2(self):
        return self.__iZutat2

    def getIZutat3(self):
        return self.__iZutat3

    # get Name
    def getSZutat1(self):
        return self.__sZutat1

    def getSZutat2(self):
        return self.__sZutat2

    def getSZutat3(self):
        return self.__sZutat3

    # get Preis
    def getFZutat1(self):
        return self.__fZutat1

    def getFZutat2(self):
        return self.__fZutat2

    def getFZutat3(self):
        return self.__fZutat3

    # set Menge
    def setIZutat1(self, iZutat1):
        self.__iZutat1 = iZutat1

    def setIZutat2(self, iZutat2):
        self.__iZutat2 = iZutat2

    def setIZutat3(self, iZutat3):
        self.__iZutat3 = iZutat3

    # set name
    def setSZutat1(self, sZutat1):
        self.__sZutat1 = sZutat1

    def setSZutat2(self, sZutat2):
        self.__sZutat2 = sZutat2

    def setSZutat3(self, sZutat3):
        self.__sZutat3 = sZutat3

    # set Prreis
    def setFZutat1(self, fZutat1):
        self.__fZutat1 = fZutat1

    def setFZutat2(self, fZutat2):
        self.__fZutat2 = fZutat2

    def setFZutat3(self, fZutat3):
        self.__fZutat3 = fZutat3