# Kaffeeautomat

## Class
- main 
  - Funktionen
    - Zahlen - Steaffen ->Gui Anbindung
    - hinzufügen von Rezepten -Maria
- Getränke - Steffen
  - Variablen
    - zutaten 1-4
    - gesamtpreis
    - name
- Bestand - Steffen
  - Zutaten
  - Menge
- GUI - Maria
    - Buttens für Getränke
    - Button für Einstelungen
      - Zutaten auffüllen
      - Rezept hinzufügen

## DB - Maria -später erst mit Liste
- Liste an Getränken mit Gesamtpreis



def addrezept():
    def okRezept():
        listevorhandenerRezepte = main.listecaffees()
        print(int(entryMenge1.get()))
        listevorhandenerRezepte += [
            [entryName.get(), entryZutat1.get(), entryMenge1.get(), entryZutat2.get(), entryMenge1.get(),
             entryZutat3.get(), entryMenge1.get(), entryPreis.get()]]
        main.saveListe(listevorhandenerRezepte)
        master2.destroy()

Espresso, Espresso, 1, , 0, , 0, 1.5,
Espresso Macchaito, Espresso, 1, Milchschaum, 1, , 0, 2.0,
Cappuccino, Espresso, 1, heiße Milch, 1, Milchschaum, 2, 3.5
Cafee Latte, Espresso, 1, heiße Milch, 2, 'Milchschaum', 1, 4.0
