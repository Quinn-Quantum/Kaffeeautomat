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
            caffe.setName(caffe.listekaffes[i][0])
            caffe.setZutat1(caffe.listekaffes[i][1])
            caffe.setMenge1(caffe.listekaffes[i][2])
            caffe.setZutat2(caffe.listekaffes[i][3])
            caffe.setMenge2(caffe.listekaffes[i][4])
            caffe.setZutat3(caffe.listekaffes[i][5])
            caffe.setMenge3(caffe.listekaffes[i][6])
            caffe.setPreis(caffe.listekaffes[i][7])
            return caffe


