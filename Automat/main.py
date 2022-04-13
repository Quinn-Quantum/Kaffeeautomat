from Kaffee import *

def makecaffe(name):
    # Liste: Name, Inhalt, Menge, gesamt Preis
    listekaffes = [['Espresso', 'Espresso', 1,'',False, 1.5], ['Espresso Macchaito', 'Espresso', 1, 'Milchschaum', 1, 2]]
    for i in listekaffes:
        if listekaffes[i][0] == name:
            caffe = Kaffe()
            setName = caffe.listekaffes[i][0]
            setZutat1 = caffe.listekaffes[i][1]
            setMenge1 = caffe.listekaffes[i][2]
            setZutat2 = caffe.listekaffes[i][3]
            setMenge2 = caffe.listekaffes[i][4]
            setPreis= caffe.listekaffes[i][5]
    return caffe


