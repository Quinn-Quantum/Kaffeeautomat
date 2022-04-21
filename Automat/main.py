import Kaffee
def listecaffees():
    listekaffes = [['Espresso', 'Espresso', 1, '', 0, '', 0, 1.5],
                   ['Espresso Macchaito', 'Espresso', 1, 'Milchschaum', 1, '', 0, 2.0],
                   ['Cappuccino', 'Espresso', 1, 'heiße Milch', 1, 'Milchschaum', 2, 3.5]
                   ['Café Latte', 'Espresso', 1, 'heiße Milch', 2, 'Milchschaum', 1, 4.0]]
    return(listekaffes)

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


