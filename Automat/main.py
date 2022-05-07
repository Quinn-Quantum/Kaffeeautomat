import csv
import time
import Verwaltung

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


def bestandstests(objektKaffee):
    listeZutaten = []
    bMengenangabe = True
    with open('Bestand.csv') as csvdatei:
        reader = csv.reader(csvdatei)
        for row in reader:
            listeZutaten += [row]

    for i in range(len(listeZutaten)):
        for j in range(len(listeZutaten[i])):
            if listeZutaten[i][j] == objektKaffee.getZutat1():
                if listeZutaten[i][j+1] < objektKaffee.getMenge1():
                    bMengenangabe = False
            if listeZutaten[i][j]  == objektKaffee.getZutat2():
                if listeZutaten[i][j+1] < objektKaffee.getMenge2():
                    bMengenangabe = False
            if listeZutaten[i][j] == objektKaffee.getZutat3():
                if listeZutaten[i][j+1] < objektKaffee.getMenge3():
                    bMengenangabe = False
    return bMengenangabe

