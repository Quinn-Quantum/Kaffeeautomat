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
    master = Tk()
    master.geometry('500x500')
    master.title('Rezept')

    labelName = Label(master,text="Name des Geträmkes").place(
        height=40,
        width=120,
        x=10,
        y=10)
    labelZutat1 = Label(master,text="Zutat 1").place(
        height=40,
        width=120,
        x=10,
        y=60)
    labelZutat2 = Label(master,text="Zutat 2").place(
        height=40,
        width=120,
        x=10,
        y=110)
    labelZutat3 = Label(master,text="Zutat 3").place(
        height=40,
        width=120,
        x=10,
        y=160)

    labelMenge1 = Label(master,text="Menge 1").place(
        height=40,
        width=120,
        x=250,
        y=60)
    labelMenge2 = Label(master,text="Menge 2").place(
        height=40,
        width=120,
        x=250,
        y=110)
    labelMenge3 = Label(master,text="Menge 3").place(
        height=40,
        width=120,
        x=250,
        y=160)


    entryName = Entry(master,width=10,background='LightSteelBlue').place(
        height=40,
        width=120,
        x=150,
        y=10)
    entryZutat1 = Entry(master,width=10,background='LightSteelBlue').place(
        height=40,
        width=120,
        x=150,
        y=60)
    entryZutat2 = Entry(master,width=10,background='LightSteelBlue').place(
        height=40,
        width=120,
        x=150,
        y=110)
    entryZutat3 = Entry(master,width=10,background='LightSteelBlue').place(
        height=40,
        width=120,
        x=150,
        y=160)

    entryMenge1 = Entry(master, width=10, background='LightSteelBlue').place(
        height=40,
        width=120,
        x=350,
        y=60)
    entryMenge2 = Entry(master, width=10, background='LightSteelBlue').place(
        height=40,
        width=120,
        x=350,
        y=110)
    entryMenge3 = Entry(master, width=10, background='LightSteelBlue').place(
        height=40,
        width=120,
        x=350,
        y=160)

    Button(master, text="Bestätigen", command=standert, background='SeaGreen', foreground='black').place(
        height=40,
        width=120,
        x=50,
        y=300)
    master.mainloop()

def einstellungen():
    master = Tk()
    master.geometry('200x200')
    master.title('Einstellungen')
    Button(master, text="Rezept hinzufügen", command=addrezept, background='SlateGray', foreground='black').place(
        height=40,
        width=120,
        x=50,
        y=10)
    Button(master, text="Befüllen", command=zutun, background='SlateGray', foreground='black').place(
        height=40,
        width=120, x=50,
        y=50)
    Button(master, text="Exit", command=master.destroy, background='SlateGray', foreground='black').place(height=40,
                                                                                                          width=120,
                                                                                                          x=50,
                                                                                                          y=100)
    master.mainloop()

def mixEspresso():
    bestellung = Kaffee()
    bestellung = main.makecaffe("Espresso")

    Label(frm, text=bestellung.getName(), foreground='black').place(height=20, width=100, x=90, y=0)

def mixEspressoMachiarto():
    bestellung = Kaffee()
    bestellung = main.makecaffe("Espresso Machiarto")

    Label(frm, text=bestellung.getName(), foreground='black').place(height=20, width=100, x=90, y=0)

def mixCappuccino():
    bestellung = Kaffee()
    bestellung = main.makecaffe("Cappuccino")

    Label(frm, text=bestellung.getName(), foreground='black').place(height=20, width=100, x=90, y=0)

def mixCafeeLatte():
    bestellung = Kaffee()
    bestellung = main.makecaffe("Café Latte")

    Label(frm, text=bestellung.getName(), foreground='black').place(height=20, width=100, x=90, y=0)


root = Tk()
root.geometry('300x400')
root.title('Kaffeeautomat')
frm = ttk.Frame(root, padding=20).pack()

#Labels
Label(frm, text="Kaffee Auswahl", background = 'LightBlue', foreground = 'black').place( height=20, width=100, x = 90, y = 0)


#Buttons
buttonEspresso = Button(frm, text="Espresso",command= mixEspresso , background = 'MediumPurple', foreground = 'black').place( height=40, width=120, x = 20, y = 40)
buttonEspressoMachiarto = Button(frm, text="Espresso Machiarto", command= mixEspressoMachiarto, background = 'MediumPurple', foreground = 'black').place(height=40, width=120, x = 160, y = 40)
buttonCappuccino = Button(frm, text="Cappuccino", command= mixCappuccino , background = 'MediumPurple', foreground = 'black').place(height=40, width=120, x = 20, y = 90)
buttonCafeeLatte = Button(frm, text="Cafee Latte", command= mixCafeeLatte , background = 'MediumPurple', foreground = 'black').place( height=40, width=120, x = 160, y = 90)
buttonEinstellungen = Button(frm, text="Einstellungen" ,  background = 'SlateGray', foreground = 'black', command = einstellungen).place( height=40, width=120, x = 20, y = 200)
Button(frm, text="Exit", command=root.destroy, background = 'SlateGray', foreground = 'black').place( height=40, width=120, x = 150, y = 200)
root.mainloop()