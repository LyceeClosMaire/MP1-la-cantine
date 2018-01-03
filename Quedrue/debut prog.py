import csv
import os


dossier_de_travail = "E:\ISN"
os.chdir(dossier_de_travail)
nom_csv = "cantine.csv"



fichier_csv = open(nom_csv, mode='w', newline='')

sortie_csv = csv.writer(fichier_csv, delimiter=';')

sortie_csv.writerows( [ ['Code barre','Nom','Prénom','Pain','Entrée','Viandes','Accompagnement','Taille du plat','Laitage','Dessert'], ['1234','T-F','Audrey','1','2','3','4','3','0','0'] ] )


fichier_csv.close()


