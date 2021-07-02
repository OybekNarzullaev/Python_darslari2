# Bugungi mavzu massivlar -> Array
# python aynan massiv tuhdhuncha yo'q

a = '123456'
b = 123

sonlar = [1, 2, 3, 'salom', True, [1, 2.3]]  # ro'yhat
print(type(sonlar))
# xulosa: Pythonda massiv o'rniga ro'yhatdan foydalaniladi
# Ro'yhatning massivdan asosiy farqi bu turli xil toifali elementlarga ega bo'lishi

# List -> Ro'yhat

""" ro'yhat elementiga murojaat """

ruyhatElementi = sonlar[3]

print(ruyhatElementi)
# xulosa elementga murojaat indeks orqali ham amalga oshiriladi


""" ro'yhat elementini yangilash """

mashinalar = ["Nexia", "Laceti", "Malibu"]

# yangilanish
mashinalar[0] = "Cobalt"
print(mashinalar)   # endi:  mashinalar = ["Cobalt", "Laceti", "Malibu"]

""" Ro'yhat uzunligi yoki elementlari soni """

mevalar = ['olma', 'anor']
print(len(mevalar))  # uzunligi -> 2

""" metod yozish -> .metod(parametri) """

""" Ro'yhatga element qo'shish -> append() metodi"""

mevalar = ['olma', 'anor']

mevalar.append("gilos")  # mevalar = ['olma', 'anor', "gilos"]
print(mevalar)
# xulosa: append ro'yhatni oxiriga element qo'shadi

""" Ro'yhatni tozalash -> hamma elementni o'chirish -> clear methodi"""
sonlar = [1, 2, 3, 4]
sonlar.clear()  # parametr qabul qilmaydi
print(sonlar)


""" bir ro'yhatni boshqaisiga nusxalash copy() methodi"""
sonlar = [1, 2, 3, 4]
sonlar1 = sonlar.copy()  # parametr qabul qilmaydi
print(sonlar1)

""" Ro'yhatda bir xil elementlarni sanash -> count() methodi """
sonlar = [1, 2, 2, 3, 4, 4, 0, 5, 4]

print(sonlar.count(4))  # berilgan ro'yhatda 4 soni 3 ta

""" extend() bu ro'yhatga boshqa ro'yhatni ulash """
sonlar = [1, 2, 2, 3, 4, 4, 0, 5, 4]
sonlar1 = [9, 8, 2]

sonlar.extend(sonlar1)

print(sonlar)

""" index() -> bu elementni ro'yhatdagi indeksini qaytaradi """

sonlar = [1, 2, 3, 'salom', True, [1, 2.3]]
# index->[0, 1, 2,  3,      4,     5      ]

print(sonlar.index("salom"))  # javobi -> 3

""" insert methodi  -> bu elmentni o'zingiz hohlagan ro'yhat indeksiga kiritish """
sonlar = [9, 8, 2]
sonlar.insert(2, 3)   # insert(indeks, kiritilayotgan_son)

print(sonlar)


""" pop -> berilgan indeksdagi elemrentni o'chirish"""
sonlar = [9, 8, 2, 5, 6]
sonlar.pop(1)  # 1 - indeks o'chadi
print(sonlar)  # sonlar = [9, 2]

""" remove -> berilgan elementni nomi bo'yicha o'chiradi yani birinchi kelganini"""
mashinalar = ["Nexia", "Laceti", "Laceti", "Malibu"]
mashinalar.remove("Laceti")
print(mashinalar)

# masala 2. ro'yhatdan bir xil nomli elementlarni hammasini o'chiring.
# count, remove
