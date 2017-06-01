import csv
import psycopg2

#conn_string contains all the needed settings for the database connection
conn_string = "host='localhost' dbname='election' user='postgres' password='postgres'"

conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

#Read Tweet Data and copy to database
inputT= open(r'/home/kuzniarz/Desktop/Workspace/Datenbanken/Projekt/DBS-Workspace/aetDATA.csv', 'r')
cursor.copy_from(inputT, "tweet", sep=';')
inputT.close()

#Read Hashtag Data and copy to database
inputH= open(r'/home/kuzniarz/Desktop/Workspace/Datenbanken/Projekt/DBS-Workspace/aetTAG.csv', 'r')
cursor.copy_from(inputH, "hashtag", sep=';')
inputH.close()
