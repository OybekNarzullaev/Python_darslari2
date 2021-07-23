import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="oybek25.99",
    database="maktab"
)

mycursor = mydb.cursor()


def jadvallar(cursor):
    cursor.execute("show tables")
    for i in cursor:
        print(i)


# jadvallar(mycursor)


def jadvalni_kurish(cursor):
    cursor.execute("select *from uqituvchilar")
    for i in cursor:
        print(i)


jadvalni_kurish(mycursor)

mycursor.execute("""insert into uqituvchilar values(7, "R.R", 4000000, "jizzax", "")""")

