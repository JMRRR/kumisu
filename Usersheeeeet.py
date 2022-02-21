#!/usr/bin/env python3
      
#Importiert die notwendigen Bibliotheken
import os
from base64 import b64encode
#geniert Passworter rundommäßig


#Setzt die variablen Namen: Vor- und Nachname
V="Vorname"
N="Nachname"
#Erzeugt Passwörter in die Variablen key und Key1 ein
key = os.urandom(15)
key1 = os.urandom(15)

#Setzt Variablen PW und PW1 und wandelt diese in ASCII-Code um
PW = b64encode(key).decode('ASCII')
PW1 = b64encode(key1).decode('ASCII')

#Schreibt die zuvor gesetzten Variablen in ein variables Textfile ein

my_file = open((V)+"_"+(N)+"_Einarbeitungsheet.txt","w+")
my_file.write((V)+" & "+(N)+"\n"+"Passwort:     "+(PW)+"\n\n")

my_file.write((V)+"-"+(N)+".mellowmessage.de\n"+"Passwort:     "+(PW1)+"\n\n\n\n\n\n\n")

#Die folgenden Variablen können beliebig angepasst werden

my_file.write("/PFADE/ZU/SERVER/"+(V)+" oder Sonstige Infos\n")
my_file.write("/PFADE/ZU/SERVER/ oder Sonstige Infos\n")
my_file.write("/PFADE/ZU/SERVER/ oder Sonstige Infos\n")
my_file.write("/PFADE/ZU/SERVER/ oder Sonstige Infos\n")
my_file.write("/PFADE/ZU/SERVER/ oder Sonstige Infos\n")
my_file.write("/PFADE/ZU/SERVER/ oder Sonstige Infos\n")
my_file.write("/PFADE/ZU/SERVER/ oder Sonstige Infos\n")
my_file.write("/PFADE/ZU/SERVER/ oder Sonstige Infos\n")
my_file.write("/PFADE/ZU/SERVER/ oder Sonstige Infos\n")
my_file.write("/PFADE/ZU/SERVER/ oder Sonstige Infos\n")
my_file.write("/PFADE/ZU/SERVER/ oder Sonstige Infos\n")
my_file.write("/PFADE/ZU/SERVER/ oder Sonstige Infos\n")
