# """ 1. modullar bilan ishlash """
# # import qilish
# '1. modulni import qilish'
# import pygame
#
# '2. moduldagi funksiyani import qilish'
# from time import daylight
#
# '3. moduldan bir necha obyektni import qilish'
# from os import chdir, remove
#
# '4. moduldagi barcha obyektlarni import qilish'
# from math import *
# import math
#
# print(sin(0))
#
# """ o'zimiz yaratgan modulni import qilish """
# # from meningModulim import *
# # print(y, x)
#
# """ boshqa papkalardagi modullarni import qilish """
# from examp2 import sonlar
# print(sonlar)

# """ 1 - masala. matematika modulini tuzasiz o'shani ichida:
#     ikki son uchun
#  1. qushish
#  2. ayirish
#  3. ko'paytish
#  4. bulish
#
#  """
# from myFolder import matematika as mt
#
# print(mt.qushish(2, 3))
# print(mt.ayirish(5, 2))
# print(mt.kupaytirish(3, 2))
# print(mt.bulish(6, 2))

# """ dir -> funksiyasi - bu moduldagi barcha obyektlarni qaytaradigan funksiya """
# from myFolder import matematika
# import math
# print(dir(math))
# print(dir(matematika))
#
# from myFolder import uzbekcha as uz
# uz.chiqar("salom")
#
# x = uz.kirit("son kiriting: ")
#
# uz.chiqar(x)

""" bu lar teng kuchli chunki vaqt.py bilan modullar.py bitta papkada"""
# from modullarpapka import vaqt
# import vaqt

""" platform moduli """

"""
2 - masala. 
3 - ta modul yaratasiz. uchinchi modulda salom degan funksiya bor uni dastlab 2 - modulga
keyin ikkinchidan 1 - modulga import qilib chaqring
"""

from masala3 import modul2
y = modul2.x
y()

