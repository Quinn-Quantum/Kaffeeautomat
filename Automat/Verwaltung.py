class Kaffee:
    __name = ""
    __gesamtpreis = 0.0
    __zutat1 = ""
    __zutat2 = ""
    __zutat3 = ""
    __menge1 = 0
    __menge2 = 0
    __menge3 = 0

    def __init__(self):
        self.__gesamtpreis
        self.__name
        self.__zutat1
        self.__zutat2
        self.__zutat3
        self.__menge1
        self.__menge2
        self.__menge3
#Get
    def getPreis(self):
        return self.__gesamtpreis

    def getName(self):
        return self.__name

    def getZutat1(self):
        return self.__zutat1

    def getZutat2(self):
        return self.__zutat2

    def getZutat3(self):
        return self.__zutat3

    def getMenge1(self):
        return self.__menge1

    def getMenge2(self):
        return self.__menge2

    def getMenge3(self):
        return self.__menge3

#Set
    def setPreis(self,gesamtpreis):
        self.__gesamtpreis = gesamtpreis

    def setName(self,name):
        self.__name = name

    def setZutat1(self, zutat):
        self.__zutat1 = zutat

    def setZutat2(self,zutat):
        self.__zutat2 = zutat

    def setZutat3(self,zutat):
        self.__zutat3 = zutat

    def setMenge1(self,menge):
        self.__menge1 = menge

    def setMenge2(self,menge):
        self.__menge2 = menge

    def setMenge3(self,menge):
        self.__menge3 = menge


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