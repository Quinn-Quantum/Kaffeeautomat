import csv
import time
import Verwaltung
import Verwaltung_Bestand

#Gibt eine Liste ter Kaffees mit ihren Zutaten und den dazugehörigen Mengen so wie den Gesamtpreis zurück
def listecaffees():
    listekaffes =[]
    with open('Kaffees.csv') as csvdatei:
        readerCSV = csv.reader(csvdatei)
        for zeile in readerCSV:
            listekaffes +=[zeile]
    return listekaffes

#Überschreibt die CSV mit der neuen Liste
def saveListe(listeKaffees):
    file = open('Kaffees.csv', 'w', newline='')
    while file:
        writerCSV = csv.writer(file)
        for row in listeKaffees:
            writerCSV.writerow(row)
        return True

#Kaffee wird ausgelesen und in seine Bestandteile zerlägt
def makecaffe(name):
    listekaffes = listecaffees()
    #Der Kaffee wird als Opjekt gehandelt um seine Variablen einzelt zu verwänden
    caffe = Verwaltung.Kaffee()
    i = 0
    for i in range(len(listekaffes)):
        if listekaffes[i][0] == name:
            caffe.setName(listekaffes[i][0])
            caffe.setZutat1(listekaffes[i][1])
            caffe.setMenge1(listekaffes[i][2])
            caffe.setZutat2(listekaffes[i][3])
            caffe.setMenge2(listekaffes[i][4])
            caffe.setZutat3(listekaffes[i][5])
            caffe.setMenge3(listekaffes[i][6])
            caffe.setPreis(listekaffes[i][7])
            return caffe

#Überprüfung ob eine der Zutaten zu gerin vorhanden ist und zum abziehen der benötigten Zutaten
def bestandstests(objektKaffee):
    listeZutaten = []
    bMengenangabe = True
    #aus Bestand.csv in eine Liste zum vergleichen mit dem Objekt
    with open('Bestand.csv') as csvdatei:
        reader = csv.reader(csvdatei)
        for row in reader:
            listeZutaten += [row]

    for i in range(len(listeZutaten)):
        for j in range(len(listeZutaten[i])):
            #Test ob die Zuteten mit den Mengen und Zuteten in der Liste übereinstimmen
            #solte die Zutat zugering vorhanden sein wird die Funktion beendet und ein Fals zu rückgegeben
            #else: die benötigte Menge wird abgezogen
            if listeZutaten[i][j] == objektKaffee.getZutat1():
                if listeZutaten[i][j+1] < objektKaffee.getMenge1():
                    bMengenangabe = False
                    return bMengenangabe
                else:
                    listeZutaten[i][j + 1]= int(listeZutaten[i][j + 1]) - int(objektKaffee.getMenge1())

            elif listeZutaten[i][j]  == objektKaffee.getZutat2():
                if listeZutaten[i][j+1] < objektKaffee.getMenge2():
                    bMengenangabe = False
                    return bMengenangabe
                else:
                    listeZutaten[i][j + 1] = int(listeZutaten[i][j + 1]) - int(objektKaffee.getMenge2())

            elif listeZutaten[i][j] == objektKaffee.getZutat3():
                if listeZutaten[i][j+1] < objektKaffee.getMenge3():
                    bMengenangabe = False
                    return bMengenangabe
                else:
                    listeZutaten[i][j + 1]= int(listeZutaten[i][j + 1]) - int(objektKaffee.getMenge3())
    #veränderte Liste wieder in CSV schreiben
    file =open('Bestand.csv','w',newline='')
    with file :
        writer = csv.writer(file)
        for row in listeZutaten:
            writer.writerow(row)
    return bMengenangabe

#Funktion um die Daten aus der Bestand.csv in ein Objektzu schreiben
def bestandCSVauslesen():
    with open('Bestand.csv') as csvdatei:
        readerCSV = csv.reader(csvdatei)
        for row in readerCSV:
            bestand = Verwaltung_Bestand.Bestand(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
    return bestand