from tkinter import *
from tkinter import ttk
from main import *
from Kaffee import *

#Butten Funktionen

def addrezept():
    pass

def einstellungen():
    master = Tk()
    master.geometry('200x200')
    master.title('Einstellungen')
    Label(master,text="Hallo", foreground = 'black').place(height=20, width=100, x = 90, y = 0)
    Button(master, text="Rezept hinzufügen",command=addrezept,  background='SlateGray', foreground='black').place(height=40,
                                                                                                     width=120, x=50,
                                                                                                     y=10)
    Button(master, text="Exit", command=master.destroy, background='SlateGray', foreground='black').place(height=40,
                                                                                                     width=120, x=50,
                                                                                                     y=10)
    master.mainloop()

def mixEspresso():
     bestellung = main.makecaffe(espresso)

     Label(master, text=bestellung.getName(), foreground='black').place(height=20, width=100, x=90, y=0)






root = Tk()
root.geometry('300x400')
root.title('Kaffeeautomat')
frm = ttk.Frame(root, padding=20).pack()

#Labels
Label(frm, text="Kaffee Auswahl", background = 'LightBlue', foreground = 'black').place( height=20, width=100, x = 90, y = 0)


#Buttons
buttonEspresso = Button(frm, text="Espresso",command= mixEspresso , background = 'MediumPurple', foreground = 'black').place( height=40, width=120, x = 20, y = 40)
buttonEspressoMachiarto = Button(frm, text="Espresso Machiarto", background = 'MediumPurple', foreground = 'black').place(height=40, width=120, x = 160, y = 40)
buttonCappuccino = Button(frm, text="Cappuccino", background = 'MediumPurple', foreground = 'black').place(height=40, width=120, x = 20, y = 90)
buttonCafeeLatte = Button(frm, text="Cafee Latte", background = 'MediumPurple', foreground = 'black').place( height=40, width=120, x = 160, y = 90)
buttonEinstellungen = Button(frm, text="Einstellungen", background = 'SlateGray', foreground = 'black', command = einstellungen).place( height=40, width=120, x = 20, y = 200)
Button(frm, text="Exit", command=root.destroy, background = 'SlateGray', foreground = 'black').place( height=40, width=120, x = 150, y = 200)
root.mainloop()