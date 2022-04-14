from Automat.Kaffeeautomat import Kaffeautomat
from Getraenke.CafeLatte import CafeLatte
from Getraenke.Cappuccino import Cappuccino
from Getraenke.EspressoMacchiato import EspressoMacchiato
from Getraenke.Espresso import Espresso

if __name__ == '__main__':
    verfuegbareGetraenke = [Espresso(), EspressoMacchiato(), Cappuccino(), CafeLatte()]
    kaffeautomat = Kaffeautomat(verfuegbareGetraenke)

    while kaffeautomat.wirdBenutzt():
        kaffeautomat.printGetraenke()
        benutzerauswahl = input("Wählen Sie Ihr Getränk: ")
        kaffeautomat.verarbeiteBenutzerauswahl(benutzerauswahl)