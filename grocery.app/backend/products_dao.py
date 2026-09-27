import mysql.connector

cnx = mysql.connector.connect(user='root', password='Ti44NaS6hE*##$66',
                               host='127.0.0.1',
                               database='grocery_store')

cursor= cnx.cursor()
query = ("SELECT * FROM grocery_store.products")

cursor.execute(query)

for() in cursor:
    print()

cnx.close()