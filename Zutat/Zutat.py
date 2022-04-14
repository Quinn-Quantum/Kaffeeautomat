class Zutat:
    __name = ""
    __menge = 0
    __kostenProMenge = 0

    def __init__(self, name, menge, kostenProMenge):
        self.__name = name
        self.__menge = menge
        self.__kostenProMenge = kostenProMenge

    def getName(self):
        return self.__name

    def getPreis(self):
        return self.__kostenProMenge * self.__menge