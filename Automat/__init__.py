from CafeLatte import *
from Cappuccino import *
from Espresso import *
from EspressoMacchiato import *
from Bestand import *
import time
#Funktion überprüft ob eine Variable ein Integer ist
def as_int(number):
    try:
        return int(number)
    except ValueError:
        pass
    return None

def auswahlBearbeiten(wahlDesTrinks, bestand):
    zuZahlen = 0.5
    if wahlDesTrinks == 1:
        espresso =Espresso()
        zuZahlen = zuZahlen + (espresso.getPreisEspresso() * espresso.getMengeEspresso()) #Berechnung für den Getränkepreis
        bestand.setBEspresso(bestand.getBEspresso() - espresso.getMengeEspresso()) #reduziert den Bestand der Zutat im Automaten
        kaffeeAngaben = [zuZahlen,espresso.getName()] #Liste[Preis des Getränkes, Name des Getränkes]

    elif wahlDesTrinks == 2:
        espresso = Espresso()
        zuZahlen = zuZahlen + (espresso.getPreisEspresso() * espresso.getMengeEspresso())
        bestand.setBEspresso(bestand.getBEspresso() - espresso.getMengeEspresso())

        espressoMacchiato = EspressoMacchiato()
        zuZahlen = zuZahlen + (espressoMacchiato.getPreisMilchschaum() * espressoMacchiato.getMengeMilchschaum())
        bestand.setBMilchschaum(bestand.getBMilchschaum() - espressoMacchiato.getMengeMilchschaum())
        kaffeeAngaben = [zuZahlen,espressoMacchiato.getName()]

    elif wahlDesTrinks == 3:
        espresso = Espresso()
        zuZahlen = zuZahlen + (espresso.getPreisEspresso() * espresso.getMengeEspresso())
        bestand.setBEspresso(bestand.getBEspresso() - espresso.getMengeEspresso())

        cappuccino = Cappuccino()
        preisMilch = cappuccino.getPreisMilchschaum1() * cappuccino.getMengeMilchschaum1()
        bestand.setBMilchschaum(bestand.getBMilchschaum() - cappuccino.getMengeMilchschaum1())

        preisHeiß = cappuccino.getPreisHeißeMilch1() * cappuccino.getMengeHeißeMilch1()
        bestand.setBHeißeMilch(bestand.getBHeißeMilch()- cappuccino.getMengeHeißeMilch1())
        zuZahlen = zuZahlen + preisMilch + preisHeiß
        kaffeeAngaben = [zuZahlen,cappuccino.getName() ]
    else:
        espresso = Espresso()
        zuZahlen = zuZahlen + (espresso.getPreisEspresso() * espresso.getMengeEspresso())
        bestand.setBEspresso(bestand.getBEspresso() - espresso.getMengeEspresso())

        cafeLatte = CafeLatte()
        preisMilch = cafeLatte.getPreisMilchschaum2() * cafeLatte.getMengeMilchschaum2()
        bestand.setBMilchschaum(bestand.getBMilchschaum() - cafeLatte.getMengeMilchschaum2())
        preisHeiß = cafeLatte.getPreisHeißeMilch2() * cafeLatte.getMengeHeißeMilch2()
        bestand.setBHeißeMilch(bestand.getBHeißeMilch() - cafeLatte.getMengeHeißeMilch2())
        zuZahlen = zuZahlen + preisMilch + preisHeiß
        kaffeeAngaben = [zuZahlen,cafeLatte.getName() ]
    return kaffeeAngaben

def bezahlvorgang(zuZahlen):
    '''
    Bezahlfunktion - Eingabe der entsprechenden Münzen
    '''
    print("Erlaubte Münzen: 50 Cent; 1 Euro; 2 Euro.")
    muenzeinwurf = 0.0
    while muenzeinwurf < zuZahlen:
        einwurf = 0.0
        differenz = zuZahlen - muenzeinwurf
        einwurf = float(input("Bitte werfen Sie den zu zahlenden Betrag in höhe von %.1f Euro ein: " % differenz))
        if einwurf == 0.5 or einwurf == 1.0 or einwurf == 2.0:
            muenzeinwurf = muenzeinwurf + einwurf
        else:
            print(einwurf, "zurück - ungültiger Betrag!")
            einwurf = 0.0
            muenzeinwurf = muenzeinwurf + einwurf

    if muenzeinwurf > zuZahlen:
        rueckgeld = muenzeinwurf - zuZahlen
    else:
        rueckgeld = 0
    print("Sie bekommen %.1f Euro zurück!" %rueckgeld)
#Automat wird mit Zutaten befüllt
def refill(bestand):
    befüllen = True
    while befüllen:
        espressoB = bestand.getBEspresso()
        milchschaumB = bestand.getBMilchschaum()
        heißeMilchB = bestand.getBHeißeMilch()
        print("Bestand der Zutaten")
        print("Espresso: %d "  %espressoB)
        print("Milchschaum: %d " %milchschaumB)
        print("Heiße Milch: %d " %heißeMilchB)
        print("Was möchten Sie auffüllen?")
        print("Espresso: 1 " )
        print("Milchschaum: 2 ")
        print("Heiße Milch: 3 ")
        print("Exit: 4")
        eingabe = input('Auswahl eingeben: ')
        eingabe =as_int(eingabe)
        if eingabe == 1:
            nachfüllen = input("Wie viel Espresso möchten Sie nachfüllen? ")
            nachfüllen = as_int(nachfüllen)
            espressoB = espressoB + nachfüllen
            bestand.setBEspresso(espressoB)
        elif eingabe == 2:
            nachfüllen = input("Wie viel Milchschaum möchten Sie nachfüllen? ")
            nachfüllen = as_int(nachfüllen)
            milchschaumB = milchschaumB + nachfüllen
            bestand.setBMilchschaum(milchschaumB)
        elif eingabe == 3:
            nachfüllen = input("Wie viel heiße Milch möchten Sie nachfüllen? ")
            nachfüllen = as_int(nachfüllen)
            heißeMilchB = heißeMilchB + nachfüllen
            bestand.setBHeißeMilch(heißeMilchB)
        else:
            if espressoB >= 2 and milchschaumB >= 2 and heißeMilchB >= 2 :
                print("Auffüllen abgeschlossen.")
                befüllen = False
            else:
                print("Auffüllen noch nicht abgeschlossen.")

    #Objekt bestand wird zurückgegeben
    return bestand


def kaffeeautomat():
    bestand = Bestand()
    #Start Befüllung
    bestand=refill(bestand)
    '''
    Startfunktion
    Logik:
        Abfrage was Kunde trinken möchte
        Abrechnung
        Verarbeitung der auswahl
        Bestand Neukalkulation
    '''
    run = True
    while run:
        print('Guten Tag Genießer')
        print('Was Möchten Sie trinken?')
        print('1: Espresso')
        print('2: Espresso Macchiato')
        print('3: Cappuccino')
        print('4: Café Latte ')
        print('5: Bestand')
        wahlDesTrinks = input('Auswahl eingeben: ')
        wahlDesTrinks = as_int(wahlDesTrinks)

        if wahlDesTrinks == 5:
           print("Espresso Bestand: ",bestand.getBEspresso())
           print("Milchschaum Bestand: ", bestand.getBMilchschaum())
           print("Heiße Milch Bestand: ", bestand.getBHeißeMilch())
        else:
            #Bezahlen und Bestand anpassen
            zuBezahlen = [auswahlBearbeiten(wahlDesTrinks, bestand)]
            bezahlvorgang(zuBezahlen[0][0])


            print('Hier kommt ihr {}'.format(zuBezahlen[0][1]))
            time.sleep(2)

        #Bestand überprüfen
        if bestand.getBEspresso()< 2 and bestand.getBMilchschaum() < 2 and bestand.getBHeißeMilch() < 2:
            bestand = refill(bestand)

        #Abfrage ob kaffeautomat() weiter laufen soll
        reRun = input('Soll ich anbleiben? j/n: ')
        try:
            if str(reRun) == 'j':
                run=True
            else:
                run = False
        except ValueError:
            run = False



kaffeeautomat()