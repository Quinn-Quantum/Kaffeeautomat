import csv

import Kaffee
def listecaffees():
    listekaffes =[]
    with open('Kaffees.csv') as csvdatei:
        readerCSV = csv.reader(csvdatei)
        for zeile in readerCSV:
            listekaffes +=[zeile]
    return listekaffes

def saveListe(listeKaffees):
    file = open('Kaffees.csv', 'w', newline='')
    while file:
        writerCSV = csv.writer(file)
        for row in listeKaffees:
            writerCSV.writerow(row)
        pass

def makecaffe(name):
    # Liste: Name, Inhalt, Menge, gesamt Preis
    listekaffes = listecaffees()
    i = 0
    for i in range(len(listekaffes)):
        if listekaffes[i][0] == name:
            caffe = Kaffee()
            setName = caffe.listekaffes[i][0]
            setZutat1 = caffe.listekaffes[i][1]
            setMenge1 = caffe.listekaffes[i][2]
            setZutat2 = caffe.listekaffes[i][3]
            setMenge2 = caffe.listekaffes[i][4]
            setZutat3 = caffe.listekaffes[i][3]
            setMenge3 = caffe.listekaffes[i][4]
            setPreis= caffe.listekaffes[i][5]
            return caffe


