# faylni yaratish
# f = open("mening_faylim.txt", 'x')

# faylni o'qish uchun ochish
# f = open("mening_faylim.txt")  # 'r' -> read
# print(f.read())

# yozish uchun ochish
# f = open("mening_faylim.txt", 'w')  # white - yozish
# f.write("Salom")

# faylni ochish stillari:
# f = open("nomi.kengaytmasi", "stili")
# stillari:
# "r" -> read -> o'qish uchun
# "a" -> append -> bu oxiridan yozish uchun
# "w" -> write -> ustidan yozish uchun (overwrite)
# "x" -> Create -> yaratish uchun

# "t" -> text -> matn stili birlamchi holatda
# "b" -> binar still

# faylni yana o'qish uchun ochib ko'ramiz:
# f = open("mening_faylim.txt", 'r')
# print(f.read())

# "a" -> append
# f = open("mening_faylim.txt", "r")
# print(f.read())
# f.close()
#
# f = open("mening_faylim.txt", "a")
#
# f.write(" !!!")
# f.close()
#
# f = open("mening_faylim.txt", "r")
# print(f.read())
# close() -> bu muhim

# men_haqimda.txt degan txt yaratsiz, unga
# ismingizni yozasiz
# keyin o'qib konsolga chiqarasiz
# keyin familiyangizni qo'shib qo'yasiz
# va yana konsolga chiqarasiz

# "x" -> create
# "w"
# "r"
# "a"
# "r"

# yaratish
# f = open("men_haqimda.txt", "x")

# # isminni yozaman
# f = open("men_haqimda.txt", 'w')
# f.write("Oybek")
#
# # konsolga chiqarish
# f = open("men_haqimda.txt", 'r')
# print(f.read())
#
# # familiyamni yozaman
# f = open("men_haqimda.txt", "a")
# f.write("Narzullayev")
#
# # konsolga chiqarish
# f = open("men_haqimda.txt", 'r')
# print(f.read())

# """ faylni o'qish turlari """
# f = open("men_haqimda.txt", 'r')
# # print(f.read(3))
# # print(f.readline(1))
# # print(f.readline())
# # print(f.readline())
#
# for i in f:
#      print(i)
#
#
# # read() -> hammasini o'qish
# # read(3) -> boshidagi 3 ta element o'qiladi
# # readline() -> boshidan boshlab qatorlar o'qiladi

# f = open('men_haqimda.txt', 'w')
# f.write("Oybek\nNarzullayev")
# f.close()
#
# f = open('men_haqimda.txt', 'a')
# f.write('\nJizzax')
#
# f = open('men_haqimda.txt', 'r')
# print(f.read())

# faylni o'chirish

# f = open("mening_faylim.txt", 'x')
# f.close()

import os
if os.path.exists("mening_faylim.txt"):
    os.remove("mening_faylim.txt")
    print("fayl o'chdi")
else:
    print("Bunday fayl mavjud emas")



