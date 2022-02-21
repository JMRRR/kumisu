#!/usr/bin/env python3
      
import os
from base64 import b64encode
#geniert Passworter rundommäßig

V="Loumi"
N="Rumitz"
key = os.urandom(15)
key1 = os.urandom(15)

PW = b64encode(key).decode('ASCII')
PW1 = b64encode(key1).decode('ASCII')

my_file = open((V)+"_"+(N)+"_Einarbeitungsheet.txt","w+")
my_file.write((V)+" & "+(N)+"\n"+"Passwort:     "+(PW)+"\n\n")

my_file.write((V)+"-"+(N)+".mellowmessage.de\n"+"Passwort:     "+(PW1)+"\n\n\n\n\n\n\n")


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
