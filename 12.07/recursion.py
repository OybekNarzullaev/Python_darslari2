# a = 1
# b = 2
#
#
# def qushish(a, b):
#     return a + b
#
#
# def ayirish(a, b):
#     return a - b
#
#
# def ikkilash(a):
#     return 2 * a
#
#
# def perimetr(a, b):
#     n = qushish(a, b)
#     return ikkilash(n)
#
#
# def urt(a, b):
#     return qushish(a, b) / 2
#
# # P = 2 * (a + b)
#
#
# print(qushish(a, b))
# print(ayirish(a, b))
# print(perimetr(a, b))
# print(urt(a, b))
#
# # 1 - masala
# from math import factorial as f
#
#
# def myFunction(n, k):
#     return f(n) / (f(k) * f(n - k))
#
#
# print(myFunction(6, 4))
#
# # 2 - masala
# n = int(input("n = "))
#
#
# def myFunction2(n):
#     qiymat = []
#     for i in range(1, n):
#         if i ** 2 < n:
#             qiymat.append(i)
#     return qiymat
#
#
# print(myFunction2(n))
#
# 3 - masala
# n = int(input("n = "))
#
#
# def n_chiziq(paramatr):  # e'lon qilish
#     txt = ''  # bo'sh satr e'lon qilish
#     for i in range(paramatr):  # qadamlarni tuzish
#         txt += '-'  # nechta qadan bo'lsa o'shancha qadamni txt ga qo'shish
#     print(txt)  # natini print qilish
#
#
# # 2 - usul oson va tez
# # def n_chiziq(paramatr):
# #     print('-' * paramatr)
#
# n_chiziq(n)  # funksiyani chaqirish
#
# # 3 - masala
# n = int(input("n = "))
#
#
# def nYulduz(n):
#     for i in range(n):
#         print(n * "*")
#
# """
#     2 - usul:
#     def nYulduz(n):
#     print((n * "*" + '\n') * n)
#
# """
#
# nYulduz(n)

# # 2 - masala
# n = int(input("n = "))
#
#
# def buluvchilar(a):
#     for i in range(1, a + 1):
#         if a % i == 0:
#             print(i, end=" ")  # print(i, end="\n") == print(i)
#
#
# buluvchilar(n)

# # 3 - masala. 200 ga teng va undan kichik sonlar uchun
# n = int(input("n = "))
#
# def rim(a):
#     txt = ''
#     if a // 100 > 0:
#         k = a // 100
#         txt += k * 'C'
#     if a // 10 % 10 >= 0:
#         k = a // 10 % 10
#         if k <= 3:
#             txt += k * 'X'
#         elif k == 4:
#             txt += 'XL'
#         elif k >= 5 and k < 9:
#             txt += 'L' + (k - 5) * 'X'
#         elif k == 9:
#             txt += 'XC'
#     if a % 10 > 0:
#         v = a % 10
#         if v < 4:
#             txt += 'I' * v
#         elif v == 4:
#             txt += 'IV'
#         elif v < 9 and v > 4:
#             txt += "V" + (v - 5) * "I"
#         elif v == 9:
#             txt += "IX"
#     print(txt)
#
#
# rim(n)
#

# # 4 - masala.
# n = int(input("n = "))
#
#
# # def xona_yigindi(a):
# #     yigindi = 0
# #     for i in range(len(str(a))):
# #         yigindi += a // (10 ** i) % 10
# #
# #     print(yigindi)
#
# def xona_yigindi(a):
#     summa = 0
#     a = str(a)
#     for i in a:
#         summa += int(i)
#     print(summa)
#
# xona_yigindi(n)

# # 5 - masala.
# ballar = []
#
# for i in range(5):
#     k = int(input(f"{i + 1} - hakam -> "))
#     ballar.append(k)
#
# eng_katta = max(ballar)
# eng_kichik = min(ballar)
#
# def urt(a):
#     summa = 0
#     for i in a:
#         if i == eng_katta or i == eng_kichik:
#             continue
#         else:
#             summa += i
#     return summa / (len(a) - 2)
#
#
# print(f"{eng_kichik} {eng_katta}")
# print(f"{urt(ballar)}")

# 6 - masala.

n = int(input("n = "))


def xona_soni(a):
    return len(str(a))


def xona_soni1(a):
    xonalar = 0
    d = 0
    while 10 ** d <= a:  # 1 <= 125; 10 <= 125;
        xonalar += 1
        d += 1

    return xonalar


print(xona_soni1(n))

