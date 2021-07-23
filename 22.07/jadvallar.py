import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="oybek25.99",
    database="maktab"
)

mycursor = mydb.cursor()

mycursor.execute("show tables")

jadvallar = []
for i in mycursor:
    jadvallar.append(i[0])

if "ismlar" not in jadvallar:
    mycursor.execute(
        """
        create table ismlar
        (ism varchar(50))
        """
    )


print("--Ismlar jadvali--")
print("1. jadvalni ko'rish;")
print("2. ism qo'shish")
print("3. ism o'zgartirish")
print("4. ism o'chirish")
print("0. chiqish")

while True:
    n = int(input("kerakli raqamni tanlang: "))
    print("-----------------------------")
    if n == 1:
        print("ismlar ro'yhati...")
        mycursor.execute("select *from ismlar")
        j = 0
        for i in mycursor:
            j += 1
            print(i)
        if j == 0:
            print("bo'sh")

    elif n == 2:
        print("ism qo'shish...")
        ism = input("yangi ismni kiriting: ")
        mycursor.execute(f"insert into ismlar values('{ism}')")
        mydb.commit()
    elif n == 3:
        print("ism o'zgartirish...")
        eski_ism = input("o'zgartirmoqchi bo'lgan ismni kiriting: ")
        mycursor.execute("select *from ismlar")
        ismlar = []
        for i in mycursor:
            ismlar.append(i[0])

        if eski_ism in ismlar:
            yangi_ism = input("yangi ismni kiriting: ")
            mycursor.execute(f"update ismlar set ism='{yangi_ism}' where ism='{eski_ism}' ")
            mydb.commit()
            print("ism o'zgartirildi")
        else:
            print("bazada bunday ism yo'q")
    elif n == 4:
        print("ism o'chirish...")
        uchadigan_ism = input("o'chiqmoqchi bo'lgan ismni kiriting: ")
        mycursor.execute("select *from ismlar")
        ismlar = []
        for i in mycursor:
            ismlar.append(i[0])

        if uchadigan_ism in ismlar:
            mycursor.execute(f"delete from ismlar where ism='{uchadigan_ism}'")
            print("ism o'chirildi")
        else:
            print("bazada bunday ism yo'q")
    elif n == 0:
        print("xizmatdan foydalanganingiz uchun raxmat")
        break
    else:
        print("to'g'ri raqam tanlang:")
    print("-----------------------------------------------")
