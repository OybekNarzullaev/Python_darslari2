import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="oybek25.99"
)

mycursor = mydb.cursor()

mycursor.execute("show databases")  # fetching data -> bazagi malumot b/n ishlash

bazalar = []

for db in mycursor:
    bazalar.append(db[0])

print(bazalar)

meningBazam = input("baza nomini kirting: ")

if meningBazam in bazalar:
    print("bor")
    mycursor.execute(f"drop database {meningBazam}")
    print("o'chirildi")
else:
    print("yaratildi")
    mycursor.execute(f"create database {meningBazam}")
