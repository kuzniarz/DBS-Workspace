import csv
import psycopg2

conn_string = "host='localhost' dbname='election' user='postgres' password='postgres'"

conn = psycopg2.connect(conn_string)

cursor = conn.cursor()

inputT= open(r'/home/kuzniarz/Desktop/Workspace/Datenbanken/Projekt/DBS-Workspace/aetDATA.csv', 'r')
cursor.copy_from(inputT, "tweet", sep=';')
inputT.close()

inputH= open(r'/home/kuzniarz/Desktop/Workspace/Datenbanken/Projekt/DBS-Workspace/aetTAG.csv', 'r')
cursor.copy_from(inputH, "hashtag", sep=';')
inputH.close()

#an der stelle muss nun ein cursor.execute kommen welcher die Relationelle Tabelle erstellt. Damit das so hinhaut muss man Aufgabe 2 noch anpassen(spalten aus tweet liste richtig sortieren und hashtag liste mit total_count versehen), sonst müsste das Ding komplett richtig sein
