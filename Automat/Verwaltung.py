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