# for range dan foydalanish

# 1 - masala. for yordamida 0 dan 9 gacha bo'lgan sonlarni va hafta kunlarini chiqaring

# range siz bajarish

sonlar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for son in sonlar:  # for bu sonlar degan ro'yhatni ichidagi har bir elementni har safar son ga tenglab chiqaradi
    print(son)

# range bilan bajarish

# 0 - 9 sonlari
for son in range(10):  # range(a) 0 dan a gacha bo'lgan sonlarni ketma-ket oladi
    print(son)

# 2 dan 7 gacha
for son in range(2, 8):  # range(a, b) a dan b gacha bo'lgan sonlarni ketma-ket oladi
    print(son)

# 2 dan 15 gacha bo'lgan har ikkitasidan bittasini chiqarish kerak bo'lsin
for son in range(2, 15, 2):
    print(son)

# xulosa -> range(boshlanishi, tugashi, qadam)
#           range(boshlanishi, tugashi)
#           range(tugashi) u holda noldan boshlanadi
