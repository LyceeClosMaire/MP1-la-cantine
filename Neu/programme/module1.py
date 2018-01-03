import csv
#on importe le module csv pour lire notre tableau

import os
dossier = "//DC1-0210006T/SI - Echange/ISN/MP1 la cantine/Neu"
os.chdir(dossier)
atf = "atf.csv"
# j'ai importé mon fichier csv dans le programme


#je veux ensuite lire dans mon fichier csv

fichier = open(atf, mode='r', newline='')
#j'utilise donc le mode lecture reading 'r'

entree = csv.reader(fichier, delimiter=';')
#je traduis le fichier en listes python
donnees = []
for ligne in entree:
    print(ligne)
    donnees.append(ligne)
#la liste de valeur prend la forme d'un tableau

fichier.close()

def verification(donnees, code_barre, nom, prenom):
