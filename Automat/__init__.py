from kaffees import *
def as_int(number):
    try:
        return int(number)
    except ValueError:
        pass
    return None

def auswahlBearbeiten(wahlDesTrinks):
    zuZahlen = 0.5
    if wahlDesTrinks == 1:
        espresso = Espresso()
        zuZahlen = zuZahlen + (espresso.getPreisEspresso() * espresso.getMengeEspresso())
        return zuZahlen
    elif wahlDesTrinks == 2:
        espresso = Espresso()
        zuZahlen = zuZahlen + (espresso.getPreisEspresso() * espresso.getMengeEspresso())
        espressoMacchiato = EspressoMacchiato()
        zuZahlen = zuZahlen + (espressoMacchiato.getPreisMilchschaum() * espressoMacchiato.getMengeMilchschaum())
        return zuZahlen
    elif wahlDesTrinks == 3:
        espresso = Espresso()
        zuZahlen = zuZahlen + (espresso.getPreisEspresso() * espresso.getMengeEspresso())
        cappuccino = Cappuccino()
        preisMilch = cappuccino.getPreisMilchschaum1() * cappuccino.getMengeMilchschaum1()
        preisHeiß = cappuccino.getPreisHeißeMilch1() * cappuccino.getMengeHeißeMilch1()
        zuZahlen = zuZahlen + preisMilch + preisHeiß
        return zuZahlen
    else:
        espresso = Espresso()
        zuZahlen = zuZahlen + (espresso.getPreisEspresso() * espresso.getMengeEspresso())
        cafeLatte = CafeLatte()
        preisMilch = cafeLatte.getPreisMilchschaum2() * cafeLatte.getMengeMilchschaum2()
        preisHeiß = cafeLatte.getPreisHeißeMilch2() * cafeLatte.getMengeHeißeMilch2()
        zuZahlen = zuZahlen + preisMilch + preisHeiß
        return zuZahlen


def kaffeeautomat():
    '''
    Start funktion
    Logik:
        Abfrage was Kunde drinken möchte
        Abrechnung
        verarbeitung der auswahl
    '''
    run = True
    while run:
        print('Guten Tag Geniezer')
        print('Was Möchten Sie drinken?')
        print('1: Espresso')
        print('2: Espresso macchiato:')
        print('3: Cappuccino')
        print('4: Café Latte: ')
        wahlDesTrinks = input('Auswahl eingeben: ')
        wahlDesTrinks = as_int(wahlDesTrinks)
        zuBezahlen = auswahlBearbeiten(wahlDesTrinks)





        #Abfrage ob kaffeautomat() weiter laufen soll
        reRun = input('Soll ich an bleiben? j/n: ')
        try:
            if str(reRun) == 'j':
                run=True
            else:
                run = False
        except ValueError:
            run = False





kaffeeautomat()