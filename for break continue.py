# # continue
#
# # 1 - masala 1 dan 10 gacha bo'lgan sonlar orasidan faqat 7 chiqmasin
# for i in range(1, 11):
#     if i == 7:
#         continue
#     print(i)
#
# # 2 - masala 1 dan 10 gacha bo'lgan sonlar orasidan faqat 7 va 9 chiqmasin
# for i in range(1, 11):
#     if i == 7 or i == 9:
#         continue
#     print(i)
#
# # 2 - masala 1 dan 30 gacha bo'lgan sonlar orasidan faqat 18 dan 22 gacha bo'lganlari chiqmasin
# for i in range(1, 31):
#     if i >= 18 and i <= 22:  # 18 dan katta yoki teng ammo 22 dan kichik yoki teng sonlarni olish
#         continue
#     print(i)
# xulosa: continue bu - siklda malumbir oraliq yoki qadamni tashlab o'tish degani

# break

# 3 - masala.
qidirilayotgan_son = int(input("qidirayotgan raqamingizni kiriting: "))
for i in range(1, 11):
    if qidirilayotgan_son == i:
        print("bor")
        break
    else:
        print("yo'q")

