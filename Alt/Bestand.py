class Bestand():
    def __init__(self):
        self.__bEspresso = 0
        self.__bMilchschaum = 0
        self.__bHeißeMilch = 0

    #get
    def getBEspresso(self):
        return self.__bEspresso

    def getBMilchschaum(self):
        return self.__bMilchschaum

    def getBHeißeMilch(self):
        return self.__bHeißeMilch

    #set

    def setBEspresso(self, bEspresso):
        self.__bEspresso = bEspresso


    def setBMilchschaum(self,bMilchschaum ):
        self.__bMilchschaum = bMilchschaum


    def setBHeißeMilch(self, bHeißeMilch):
        self.__bHeißeMilch = bHeißeMilch
