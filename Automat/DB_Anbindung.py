#später
# Modul für die Kommunikation mit einer MySQL Datenbank
import mysql.connector
try:
  #Aufbau einer Verbindung
  db = mysql.connector.connect(
      host="localhost",  # Servername
      user="root",  # Benutzername
      password=""  # Passwort
  )
  # Ausgabe des Hashwertes des initialisierten Objektes
  print(db)
# Wenn ein Fehler vom Typ "mysql.connector.errors.ProgrammingError" aufgetreten ist...
except mysql.connector.errors.ProgrammingError:
  # Ausgabe einer Fehlermeldung auf der Konsole
  print("Fehler beim Aufbau der DB Verbindung aufgetreten!")