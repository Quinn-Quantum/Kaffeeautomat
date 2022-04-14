import time


class Kaffeautomat:
    __wirdBenutzt = True
    __verfuegbareGetraenke = []
    __verfuegbareMuenzen = [2, 1, 0.5]

    def __init__(self, verfuegbareGetraenke):
        self.__verfuegbareGetraenke = verfuegbareGetraenke

    def wirdBenutzt(self):
        return self.__wirdBenutzt

    def printGetraenke(self):
        for i, getraenk in enumerate(self.__verfuegbareGetraenke):
            print(str(i) + ": " + getraenk.getName())
        print(str(len(self.__verfuegbareGetraenke)) + ": Exit")

    def verarbeiteBenutzerauswahl(self, benutzerauswahl):
        if self.isIntStr(benutzerauswahl) == False:
            print("Keine gültige Eingabe. Es sind nur Zahlen erlaubt!")
            return

        benutzerauswahl = int(benutzerauswahl)
        if benutzerauswahl not in range(len(self.__verfuegbareGetraenke) + 1):
            print("Keine gültige Eingabe. Bitte geben Sie die Zahlen neben dem Namen ein: ")
            return

        # Beende Programm wenn Exit ausgewählt
        if benutzerauswahl == len(self.__verfuegbareGetraenke):
            self.__wirdBenutzt = False
            return

        # Gültige Eingabe eines Getränks
        getraenk = self.__verfuegbareGetraenke[benutzerauswahl]
        print("Das Getränk kostet " + str(getraenk.getPreis()))
        wechselgeld = self.geldEntgegenNehmen(getraenk.getPreis())
        self.wechselgeldAusgeben(wechselgeld)
        self.getraenkAnfertigen(getraenk)

    def geldEntgegenNehmen(self, zuZahlenderBetrag):
        while zuZahlenderBetrag > 0:
            print("Sie müssen noch " + str(zuZahlenderBetrag) + " bezahlen")
            eingeworfeneMuenze = input("Münze einwerfen (Mögliche Münzen: " + str(self.__verfuegbareMuenzen) + "): ")
            # Prüft ob Zahl ein float ist und eine verfügbare Münze
            if not eingeworfeneMuenze.replace(".", "").isdigit() \
                    or float(eingeworfeneMuenze) not in self.__verfuegbareMuenzen:
                print("Ungültige Eingabe!")
                continue
            zuZahlenderBetrag -= float(eingeworfeneMuenze)

        return zuZahlenderBetrag # Zu viel gezahlter Betrag/Wechselgeld


    def wechselgeldAusgeben(self, summeWechselgeld):
        # Algorithmus benötigt positives Geld
        summeWechselgeld = abs(summeWechselgeld) # abs entfernt das Vorzeichen (betrag)
        print("Sie erhalten " + str(summeWechselgeld) + " zurück")

        # Liste muss absteigend sein
        self.__verfuegbareMuenzen.sort(reverse=True)

        for muenze in self.__verfuegbareMuenzen:
            while summeWechselgeld >= muenze:
                summeWechselgeld -= muenze
                print("Münze " + str(muenze) + " ausgegeben")
            if summeWechselgeld == 0:
                break


    def getraenkAnfertigen(self, getraenk):
        print("Das Getränk wird ausgegeben...")
        zutaten = getraenk.getZutaten()
        for zutat in zutaten:
            print(zutat.getName() + "...")
            time.sleep(1)
        print("Getränk erfolgreich ausgegeben")
        print()
        print()

    # https://stackoverflow.com/questions/1265665/how-can-i-check-if-a-string-represents-an-int-without-using-try-except
    def isIntStr(self, string):
        string = str(string)
        return (
                    string.startswith(('-', '+')) and string[1:].isdigit()
               ) or string.isdigit()