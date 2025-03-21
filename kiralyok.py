from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='mysql',
                                 host='127.0.0.1',
                                 database='kiralyok')

#táblák megjelenitése
cursor = cnx.cursor()
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)



#uralkodok megjelenitése
cursor.execute("SELECT * FROM uralkodo")
for uralkodo in cursor:
    print(uralkodo)

#Uralkodo I.Mátyás

cursor.execute("SELECT * FROM uralkodo WHERE nev = ' I.Mátyás'")
for uralkodo in cursor:
    print(uralkodo)

#Mátyás Király adatai

cursor.execute("SELECT szul,hal FROM uralkodo WHERE uralkodo. nev = ' I.Mátyás'")
for uralkodo in cursor:
    print(uralkodo)




cnx.close()