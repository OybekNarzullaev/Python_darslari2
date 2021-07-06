# """ 8 - masala Doskaga qarang B mi generatsiya qiling.
# """
#
# # n = int(input("n = "))
# # a = [[0] * n] * n
# #
# # print(a)
# # i = 0
# # for i in range(n):
# #     for j in range(n):
# #         a[i][j] = i
# #         i += 1
# #
# # print(a)
#
#
# """ maxsus masala 2. 3X3 matritsa berilgan for
#     yordamida ustunlarini satrga satrlarini ustunga almashtiring
#     Masalan:
#
#     [[1, 2, 3], [4, 5, 6], [7, 8, 9]] shunday bo'lsa
#     [[1, 4, 7], [2, 5, 8], [3, 6, 9]] Bunday bo'lsin
#
#     """
#
# """ masala 8. ikki o'lchovli matritsani juft elementlarini chiqaring """
# a = [[1, 2], [3, 4]]
#
# for ruyhatcha in a:
#     for element in ruyhatcha:
#         if element % 2 == 0:
#             print(element)


""" masala 9. ikki o'lchovli matritsani toq elementlarini ikkiga ko'paytirib qo'ying
              juft elmentlarini 2 ga bo'lib qo'ying
              Masalan:
                [[1, 2], [3, 4]] -> [[2, 1], [6, 2]]"""

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(3):
    for j in range(3):
        if i == 2 - j:
            print(a[i][j])



""" masala 10. 3 o'lchovli matritsa berilgan uni dioganali elementlarini chiqaring """
