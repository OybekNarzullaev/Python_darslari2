# """ xatolar bilan ishlash yoki istisnolar """
#
# # SyntaxError
# print("hello",,
#
# # IdentationError:
# for i in range(5):
# print(i)
# # NameError
# try:
#     ism = "Oybek"
#     print(ims)
# except:
#     print("xato -> NameError")
# # valueError
# try:
#     x = "1.2"
#     int(x)
# except:
#     print("ValueError")

# try -> urunib ko'rmoq
# except -> istisno qilish

# """ bir necha istisnolar """
# try:
#     # nameError
#     ism = "Oybek"
#     print(ism)
#     # valueError
#     i = '1.02'
#     int(i)
# except NameError:
#     print("ism o'zgaruvsini nomida xato")
# except ValueError:
#     print("qiymatda xatolik")

# """ else -> kodingiz to'g'ri ishlaganda chiqadigan natija"""
#
# try:
#     print("inson holati: ", end=" ")
#     print(x)
# except:
#     print("inson kasal")
# else:
#     print("soppa - sog'")

# """ finally -> try except jarayoni tagagundan so'ng ishlatiladi"""
# y = 0
# try:
#     y = 0
#
#     print("salom")
# except:
#     y += 1
#     print("try dagi nimadur xato")
# finally:
#     if y == 0:
#         print("dasturda xato yo'q")
#     else:
#         print("dasturda xato bor")

# """ raise -> xatolarni keltirib chiqarish"""
# try:
#     n = int(input("n = "))
#
#     if n < 0:
#         raise Exception()
# except:
#     print("xato")
# else:
#     print("xato yoq ")

# """ xato xabarini ko'rish """
# import sys
#
# try:
#     x = 21 / 0
# except:
#     print(sys.exc_info()[0])
#

# 3 - masala. x sonini kiriting agar son juft bo'lsa xato keltirib chiqaring
# va istisno qiling hamda juft son kiritlmasa to'gri ishlagani haqida xabar bering
# va finallyni ham ishlating.

import sys
try:
    n = int(input("n = "))
    if n % 2 == 0:
        raise Exception("Siz juft son kiritdingiz")
except:
    print(sys.exc_info()[1])
else:
    print("xato yo'q")
finally:
    print("dastur tugadi")
