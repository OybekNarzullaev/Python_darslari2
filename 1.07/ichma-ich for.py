# listlar -> ro'yhatlar
# masalan: mevalar = ["olma", "anor", "apelsin", 1, True]
# meva = "olma"

# ichma-ich for ga misol
mevalar = ["olma", "anor", "apelsin"]

# savol: yuqoridagi ro'yhatni har bir harfini alohida qatorga chiqaring!

for meva in mevalar:
    for harf in meva:
        print(harf)

# 1 - masala. mashinalar ro'yhati berilgan
# ularni har bir harfini alohida qatorga chiqaring

# 2 - masala. berilgan sonlar to'plami ichida eng kichikigini toping:

sonlar = [2, 8, 4, 5, 4, 1, 0, 9]

kichikSon = sonlar[0]  # kichikSon = 2

for son in sonlar:  # in (inglizcha) -> ichida
    if kichikSon > son:
        kichikSon = son

print(kichikSon)

# 3 - masala. sonlar to'plami berilgan bu to'plamni o'sish tartibida saralang:

sonlar = [2, 8, 4, 5, 4, 1, 0, 9]



# indert sort -> qo'yish orqali saralash
for index in range(len(sonlar)):  #len(sonlar) -> 8
    for key in range(len(sonlar)):
        if sonlar[index] < sonlar[key]:
            sonlar[index] = sonlar[key] + sonlar[index]
            sonlar[key] = sonlar[index] - sonlar[key]
            sonlar[index] = sonlar[index] - sonlar[key]
            print(sonlar)


sonlar.sort(reverse=False)
print(sonlar)

# 4 - masala. raqamlarni toplamida elementi nechiga teng bo'lsa shu elementni
# o'shancha chop eting

numbers = [2, 1, 6, 7]

# 2, 2
# 1
# 6, 6, 6, 6, 6, 6
# 7, 7, 7, 7, 7, 7, 7

for number in numbers:  # number = 2
    for i in range(number):  # 0, 1
        print(number)
else:
    print(f"Sikl {number} soni bilan Tugadi!")
