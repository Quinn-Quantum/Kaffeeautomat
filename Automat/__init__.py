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

def bezahlvorgang(zuZahlen):
    '''
    Bezahlfunktion - Eingabe der entsprechenden Münzen
    '''
    print("Erlaubte Münzen: 50 Cent; 1 Euro; 2Euro")
    muenzeinwurf = 0.0
    while muenzeinwurf < zuZahlen:
        differenz = zuZahlen - muenzeinwurf
        muenzeinwurf = muenzeinwurf + float(input("Bitte werfen Sie den zu zahlenden Betrag in höhe von %.1f Euro ein: " %differenz))


    if muenzeinwurf > zuZahlen:
        rueckgeld = muenzeinwurf - zuZahlen
    else:
        rueckgeld = 0
    print("Sie bekommen %.1f Euro zurück!" %rueckgeld)


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
        print(zuBezahlen)

        bezahlvorgang(zuBezahlen)



        #Abfrage ob kaffeautomat() weiter laufen soll
        reRun = input('Soll ich an bleiben? j/n: ')
        try:
            if str(reRun) == 'j':
                run=True
            else:
                run = False
        except ValueError:
            run = False




#test
kaffeeautomat()