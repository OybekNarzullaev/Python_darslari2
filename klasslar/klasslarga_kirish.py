# class Son:
#     x = 1
#     y = 2
#
#
# son1 = Son()   # son1 -> bu obyekt, Son() -> klass
# print(son1.y, son1.x)
# son2 = Son()
# print(son2.x, son2.y)
#
# # xulosa. Bitta klassdan hohlagancha obyekt olish mumkin
#
# """ def __init__() funksiyasi: """
#
#
# class Son:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# son3 = Son(4, 5)
# print(son3.x, son3.y)
# son4 = Son(6, 7)
# print(son4.x, son4.y)

# class Avtomobil:
#     def __init__(self, rusumi, yili, rangi, firmasi):
#         self.rusumi = rusumi,
#         self.yili = yili,
#         self.rangi = rangi,
#         self.firmasi = firmasi
#
#
# malibu = Avtomobil("Malibu", 2022, "qora", "Chevrolet")
# lacetti = Avtomobil("lacetti", 2020, "oq", "Chevrolet")
#
# print(malibu.__dict__)
# print(lacetti.__dict__)

""" xususiyani o'zgartirish va o'chirish """

#
# class Son:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# son1 = Son(1, 2)
# son1.x = 3
# print(son1.__dict__)
#
# del son1.x  # son1.x ni o'chirish
# print(son1.__dict__)
#
# # obyektni o'zini o'chirish
# # del son1
# # print(son1)

""" classda metodlar """

#
# class Avtomobil:
#     def __init__(self, rusumi):
#         self.rusumi = rusumi
#
#     def signal(self):
#         print("Biiib!!!!")
#
#
# malibu = Avtomobil("Malibu")
# malibu.signal()


class Shaxs:
    def __init__(self, ism, fam, shahri, mahallasi):
        self.ism = ism
        self.fam = fam
        self.shahri = shahri
        self.mahallasi = mahallasi

    def tuliq_ism(self):
        return self.ism + ' ' + self.fam

    def tuliq_manzil(self):
        return f"{self.shahri} shahri; {self.mahallasi} mahalasi"


sh1 = Shaxs("Oybek", "Narzullaev", "Jizzax", "Uchariq")
print(sh1.tuliq_ism())
print(sh1.tuliq_manzil())

# 1 - masala. Xodim class yaratasiz undan 5 ta obyekt olasiz
# Xodim klasida -> ismi, manzili, maoshi
# maoshi 2 mln dan kamlarini ismini chiqarasiz


class Xodim:
    def __init__(self, ismi, manzili, maoshi):
        self.ismi = ismi
        self.manzili = manzili
        self.maoshi = maoshi

    def gap(abs):
        print(f"Mening ismi {abs.ismi}; maoshim {abs.maoshi}")
        if abs.maoshi < 1000000:
            print("mening maoshim kam!")


xodimlar = []
n = int(input("n = "))
for i in range(n):
    print(f"{i + 1} - xodim: ")
    ism = input("ismi: ")
    manzili = input("manzili: ")
    maoshi = int(input("maoshi: "))
    xodimlar.append(Xodim(ismi=ism, manzili=manzili, maoshi=maoshi))


# x1 = Xodim("Bunyod", "Lalmikor", 4000000)
# xodimlar.append(x1)
# x2 = Xodim("Sunnat", "Lalmikor", 400000)
# xodimlar.append(x2)
# x3 = Xodim("Doston", "Lalmikor", 3000000)
# xodimlar.append(x3)
# x4 = Xodim("Ilyos", "Lalmikor", 1500000)
# xodimlar.append(x4)
# x5 = Xodim("Shoxzod", "Lalmikor", 9000000)
# xodimlar.append(x5)

for xodim in xodimlar:
    xodim.gap()

# 1. dastlab xodimlar sonini kiriting.
# 2. har bir xodim ma'lumotlarini input qilib
# 3. gap() metodida agar oyligini 1mln dan past bo'lsa
# "mening oyligim kam degan yozuv ham chiqsin"
# 4. barcha xodim ma'lumotlarini gap metodi orqali konsolga chiqaring

""" uyga vazifa """
# 1. n sonini kiritib talaba klasidan n ta obyekt oling
