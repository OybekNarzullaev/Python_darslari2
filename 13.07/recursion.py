# # rekursiya - o'ziga murojaat qiladigan funksiya ekan.
#
# # 1 - masala. k dan n gacha bo'lgan natural sonlarni ekranga chiqarish:
#
# def birDanNgacha(k, n):  # parameter kiradi
#     if n == k:
#         print(f"{k}, {n}")
#     else:
#         print(f"{k}, {n}")
#         birDanNgacha(k + 1, n)  # rekursiya
#
#
# birDanNgacha(1, 10)
#
# # 2 - masala. n dan 1 gacha teskari tartibda:
#
#
# def n_dan_1_gacha(n):
#     print(n)
#     n_dan_1_gacha(n - 1)
#
#
# n_dan_1_gacha(10)
#
# # 3 - masala. faktorial
# def fakt(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * fakt(n - 1)  # 5 * 4 * 3 * 2 * 1
#
#
# print(fakt(0))
#
# # 4 - masala.
# def yigindi(n):
#     if n == 1:
#         return 1
#     else:
#         return n + yigindi(n - 1)  # 5 + 4 + 3 + 2 + 1
#
#
# print(yigindi(5))
#
# # 5 - masala. 1 dan gacha bo'lgan sonlarni teskari tartibda chiqarish
# def yigindi_toq(n):
#     if n == 1:
#         print(n)
#     else:
#         if n % 2 == 0:
#             n = n - 1
#         print(n)
#         yigindi_toq(n - 2)
#
#
# print(yigindi_toq(7))

# 6 - masala. fibonachi sonlarini n - chi xadini topshish:
# 1, 1, 2, 3, 5, 8 ...
a = []


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_hadlari(n):
    for i in range(1, n + 1):
        print(fib(i), end=" ")


fib_hadlari(9)
