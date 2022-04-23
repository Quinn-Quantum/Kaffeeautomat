from tkinter import *
from tkinter import ttk
import main
import Kaffee


#Butten Funktionen


def standert():
    pass


def zutun():
    master = Tk()
    master.geometry('200x200')
    master.title('Einstellungen')
    Button(master, text="Standert", command=standert, background='SlateGray', foreground='black').place(
        height=40,
        width=120,
        x=50,
        y=10)
    master.mainloop()




def addrezept():
    def buttonHinzufügen():
        listevorhandenerRezepte = main.listecaffees()
        # Übernahme der Daten
        name = str(entryName.get())
        print(name)

        zutat1 = str(entryZutat1.get())
        zutat2 = str(entryZutat2.get())
        zutat3 = str(entryZutat3.get())

        menge1 = int(entryMenge1.get())
        menge2 = int(entryMenge2.get())
        menge3 = int(entryMenge3.get())

        preis = float(entryPreis.get())

        # Verarbeitung der Daten
        listevorhandenerRezepte += [
            [name, zutat1,menge1, zutat2, menge2,
             zutat3, menge3, preis]]
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
    entryMenge1 = Entry(master=tkFenster, bg='LightSteelBlue')
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
    master = Tk()
    master.geometry('200x200')
    master.title('Einstellungen')
    Button(master, text="Rezept hinzufügen", command=addrezept, background='LightGrey', foreground='black').place(
        height=40,
        width=120,
        x=50,
        y=10)
    Button(master, text="Befüllen", command=zutun, background='LightGrey', foreground='black').place(
        height=40,
        width=120, x=50,
        y=50)

    master.mainloop()

def mixEspresso():
    bestellung = Kaffee.Kaffee()
    bestellung = main.makecaffe("Espresso")

    Label(frm, text=bestellung.getName(), foreground='black').place(height=20, width=100, x=90, y=0)

def mixEspressoMachiarto():
    bestellung = Kaffee.Kaffee()
    bestellung = main.makecaffe("Espresso Machiarto")

    Label(frm, text=bestellung.getName(), foreground='black').place(height=20, width=100, x=90, y=0)

def mixCappuccino():
    bestellung = Kaffee.Kaffee()()
    bestellung = main.makecaffe("Cappuccino")

    Label(frm, text=bestellung.getName(), foreground='black').place(height=20, width=100, x=90, y=0)

def mixCafeeLatte():
    bestellung = Kaffee.Kaffee()()
    bestellung = main.makecaffe("Café Latte")

    Label(frm, text=bestellung.getName(), foreground='black').place(height=20, width=100, x=90, y=0)

if __name__ == "__main__":
    root = Tk()
    root.geometry('300x400')
    root.title('Kaffeeautomat')
    frm = ttk.Frame(root, padding=20).pack()

    #Labels
    Label(frm, text="Kaffee Auswahl", background = 'LightBlue', foreground = 'black').place( height=20, width=100, x = 90, y = 0)


    #Buttons
    buttonEspresso = Button(frm, text="Espresso",command= mixEspresso , background = 'Tan', foreground = 'black').place( height=40, width=120, x = 20, y = 40)
    buttonEspressoMachiarto = Button(frm, text="Espresso Machiarto", command= mixEspressoMachiarto, background = 'Tan', foreground = 'black').place(height=40, width=120, x = 160, y = 40)
    buttonCappuccino = Button(frm, text="Cappuccino", command= mixCappuccino , background = 'Tan', foreground = 'black').place(height=40, width=120, x = 20, y = 90)
    buttonCafeeLatte = Button(frm, text="Cafee Latte", command= mixCafeeLatte , background = 'Tan', foreground = 'black').place( height=40, width=120, x = 160, y = 90)
    buttonEinstellungen = Button(frm, text="Einstellungen" ,  background = 'LightGrey', foreground = 'black', command = einstellungen).place( height=40, width=120, x = 20, y = 200)
    Button(frm, text="Exit", command=root.destroy, background = 'LightGrey', foreground = 'black').place( height=40, width=120, x = 150, y = 200)
    root.mainloop()