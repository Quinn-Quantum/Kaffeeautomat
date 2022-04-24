from tkinter import *
from tkinter import ttk
import main
import Verwaltung
import csv


#Butten Funktionen

def aktuellerBestand():
    bestand = Verwaltung.Bestand()

    with open('Bestand.csv') as csvdatei:
        readerCSV = csv.reader(csvdatei)
        for row in readerCSV:
            bestand.setBEspresso(int(row[0]))
            bestand.setBMilchschaum(int(row[1]))
            bestand.setBHeißeMilch(int(row[2]))

    bestandFenster = Tk()
    bestandFenster.geometry('200x200')
    bestandFenster.title('Aktuellerbestand')

    labelText= Label(master=bestandFenster, text='Bestand der Zutaten:')
    labelText.place(x=20, y=10,  height=27)

    labelEspresso = Label(master=bestandFenster, text='Espresso: {}'.format(bestand.getBEspresso()))
    labelEspresso.place(x=20, y=40, height=27)

    labelSchaum = Label(master=bestandFenster, text='Milchschaum: {}'.format(bestand.getBMilchschaum()))
    labelSchaum.place(x=20, y=70,  height=27)

    labelMilch = Label(master=bestandFenster, text='heiße Milch: {}'.format(bestand.getBHeißeMilch()))
    labelMilch.place(x=20, y=100,  height=27)

    bestandFenster.mainloop()

def bestand():
    def standert():
        bestand = Verwaltung.Bestand()
        with open('Bestand.csv') as csvdatei:
            readerCSV = csv.reader(csvdatei)
            for row in readerCSV:
                bestand.setBEspresso(int(row[0]) + 5)
                bestand.setBMilchschaum(int(row[1]) + 5)
                bestand.setBHeißeMilch(int(row[2]) + 5)

        listeBestand = [bestand.getBEspresso(), bestand.getBMilchschaum(), bestand.getBHeißeMilch()]
        file = open('Bestand.csv', 'w', newline='')
        i=0
        while file and i<1:
            writerCSV = csv.writer(file)
            writerCSV.writerow(listeBestand)
            i=1


    master = Tk()
    master.geometry('200x200')
    master.title('Einstellungen')

    buttonBefuellung = Button(master=master, text="standert Befüllung", command=standert, background='LightGrey', foreground='black')
    buttonBefuellung.place(height=40, width=120, x=50, y=10)

    buttonBestand = Button(master=master, text="aktueller Bestand", command=aktuellerBestand, background='LightGrey', foreground='black')
    buttonBestand.place( height=40, width=120, x=50, y=60)

    master.mainloop()

def addrezept():
    def buttonHinzufügen():
        listevorhandenerRezepte = main.listecaffees()
        # Übernahme der Daten
        name = str(entryName.get())

        zutat1 = str(entryZutat1.get())
        zutat2 = str(entryZutat2.get())
        zutat3 = str(entryZutat3.get())

        #Abfrage ob eine Menge Angegeben wurde
        menge1 = entryMenge1.get()
        if menge1 == '' :
            menge1 = 0
        else:
            int(menge1)

        menge2 = entryMenge2.get()
        if menge2 =='' :
            menge2 = 0
        else:
            int(menge2)

        menge3 = entryMenge3.get()
        if menge3 == '' :
            menge3 = 0
        else:
            int(menge1)

        preis = float(entryPreis.get())

        # Verarbeitung der Daten
        listevorhandenerRezepte += [[name,zutat1,menge1,zutat2,menge2,zutat3, menge3,preis]]
        boolVariable=main.saveListe(listevorhandenerRezepte)
        tkFenster.destroy()

    tkFenster = Tk()
    tkFenster.title('Ergänzung')
    tkFenster.geometry('500x500')
    # Label für den Name
    labelName = Label(master=tkFenster, text='Name')
    labelName.place(x=10, y=10, width=100, height=27)
    # Entry für den Namen
    entryName = Entry(master=tkFenster, bg='LightSteelBlue')
    entryName.place(x=150, y=10, width=100, height=27)

    # Label Zutat1
    labelZutat1 = Label(master=tkFenster, text='Zutat 1:')
    labelZutat1.place(x=10, y=60, width=100, height=27)
    # Entry für Zutat1
    entryZutat1 = Entry(master=tkFenster, bg='LightSteelBlue')
    entryZutat1.place(x=150, y=60, width=100, height=27)
    # Label Zutat2
    labelZutat2 = Label(master=tkFenster, text='Zutat 2:')
    labelZutat2.place(x=10, y=110, width=100, height=27)
    # Entry für Zutat2
    entryZutat2 = Entry(master=tkFenster, bg='LightSteelBlue')
    entryZutat2.place(x=150, y=110, width=100, height=27)
    # Label Zutat3
    labelZutat3 = Label(master=tkFenster, text='Zutat 3:')
    labelZutat3.place(x=10, y=160, width=100, height=27)
    # Entry für Zutat3
    entryZutat3 = Entry(master=tkFenster, bg='LightSteelBlue')
    entryZutat3.place(x=150, y=160, width=100, height=27)

    # Label Menge1
    labelMenge1 = Label(master=tkFenster, text='Menge 1:')
    labelMenge1.place(x=250, y=60, width=100, height=27)
    # Entry für Meng1
    entryMenge1 = Entry(master=tkFenster ,bg='LightSteelBlue')
    entryMenge1.place(x=350, y=60, width=100, height=27)
    # Label Menge2
    labelMenge2 = Label(master=tkFenster, text='Menge 2:')
    labelMenge2.place(x=250, y=110, width=100, height=27)
    # Entry für Menge2
    entryMenge2 = Entry(master=tkFenster, bg='LightSteelBlue')
    entryMenge2.place(x=350, y=110, width=100, height=27)
    # Label Menge3
    labelMenge3 = Label(master=tkFenster, text='Menge 3:')
    labelMenge3.place(x=250, y=160, width=100, height=27)
    # Entry für Meng1
    entryMenge3 = Entry(master=tkFenster, bg='LightSteelBlue')
    entryMenge3.place(x=350, y=160, width=100, height=27)

    # Label Preis
    labelPreis = Label(master=tkFenster, text='Preis:')
    labelPreis.place(x=10, y=210, width=100, height=27)
    # Entry für Preis
    entryPreis = Entry(master=tkFenster, bg='LightSteelBlue')
    entryPreis.place(x=150, y=210, width=100, height=27)

    # Button zum hinzufügen
    buttonBerechnen = Button(master=tkFenster, text='Hinzufügen',bg ='LightGreen' , command=buttonHinzufügen)
    buttonBerechnen.place(x=50, y=300, width=100, height=27)

    # Aktivierung des Fensters
    tkFenster.mainloop()

def einstellungen():
    master1 = Tk()
    master1.geometry('200x200')
    master1.title('Einstellungen')
    buttonRezept = Button(master=master1, text="Rezept hinzufügen", command=addrezept, background='LightGrey', foreground='black')
    buttonRezept.place(height=40, width=120, x=50, y=10)

    buttenBestnadsettings = Button(master=master1, text="Bestand", command=bestand, background='LightGrey', foreground='black')
    buttenBestnadsettings.place(height=40, width=120, x=50, y=60)

    master1.mainloop()

def mixKaffee(coffe):
    print(coffe)
    bestellung = Kaffee.Kaffee()
    bestellung = main.makecaffe(coffe)

    Label(frm, text=bestellung.getName(), foreground='black').place(height=20, width=100, x=90, y=0)


if __name__ == "__main__":
    root = Tk()
    root.geometry('300x400')
    root.title('Kaffeeautomat')
    frm = ttk.Frame(root, padding=20).pack()

    #Labels
    Label(frm, text="Kaffee Auswahl", background = 'LightBlue', foreground = 'black').place( height=20, width=100, x = 90, y = 0)

    #Buttons
    buttonEspresso = Button(frm, text="Espresso",command=lambda: mixKaffee("Espresso") , background = 'Tan', foreground = 'black').place( height=40, width=120, x = 20, y = 40)
    buttonEspressoMachiarto = Button(frm, text="Espresso Machiarto", command=lambda: mixKaffee("Espresso Machiarto"), background = 'Tan', foreground = 'black').place(height=40, width=120, x = 160, y = 40)
    buttonCappuccino = Button(frm, text="Cappuccino", command=lambda: mixKaffee("Cappuccino") , background = 'Tan', foreground = 'black').place(height=40, width=120, x = 20, y = 90)
    buttonCafeeLatte = Button(frm, text="Cafee Latte", command=lambda: mixKaffee("Cafee Latte") , background = 'Tan', foreground = 'black').place( height=40, width=120, x = 160, y = 90)
    buttonEinstellungen = Button(frm, text="Einstellungen" ,  background = 'LightGrey', foreground = 'black', command = einstellungen).place( height=40, width=120, x = 20, y = 200)
    Button(frm, text="Exit", command=root.destroy, background = 'LightGrey', foreground = 'black').place( height=40, width=120, x = 150, y = 200)
    root.mainloop()