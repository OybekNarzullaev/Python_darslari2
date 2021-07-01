# tasodifiy sonlar: -> random numbers

import random
# import math
#
# # random (0, 1) haqiqiy sonni qaytaradi
# for i in range(10):
#     print(random.random())  # random 0 dan 1 gacha bo'lgan haqiqiy sonlarni tuzadi
#
# for i in range(10):
#     print(round(random.random(), 2))
#
# for i in range(10):
#     print(math.ceil(random.random() * 10))

# randint
# print(random.randint(1, 10))  # randint(a, b) a dan b gacha bo'lgan tasodifiy butun son chiqaradi

# 1 - masala. 1 dan 10 gacha bo'lgan butun son kiriting
# va randint bilan generatsiya qilingan son bilan solishtiring
# import random
#
# kiritilganSon = int(input("son -> "))
# tasodifiySon = random.randint(1, 10)
# if kiritilganSon == tasodifiySon:
#     print(tasodifiySon)
#     print("yutdingiz")
# else:
#     print(tasodifiySon)
#     print("Dam oling")

# 2 - masala. 1 dan 10 gacha bo'lgan butun son kiriting
# va randint bilan generatsiya qilingan son bilan solishtiring bu dasturda to yutmaguningizcha
# siklni to'xtatmang

# import random
# while True:
#     tasodifiySon = random.randint(1, 10)
#     kiritilganSon = int(input("son -> "))
#     if kiritilganSon == tasodifiySon:
#         print("yutdingiz")
#         break
#     else:
#         print("Dam oling")

import random

imkoniyat = 1
yutdimi = False

while imkoniyat <= 5:
    tasodifiySon = random.randint(1, 10)
    kiritilganSon = int(input("son -> "))
    if kiritilganSon == tasodifiySon:
        print("yutdingiz")
        yutdimi = True
        break
    imkoniyat += 1

if not yutdimi:
    print("yutqazdingiz")

shaxslar = ["Oybek", "Shoxzod", "Ibrohim", "Muhammad", "Islombek"]

# Uyga vazifa. 5 shaxsni ismidan iborat ro'yhat tuzib tasodifiy son
# generatsiya qilib shaxsni
# indeksiga tenglab g'olibni aniqlang

