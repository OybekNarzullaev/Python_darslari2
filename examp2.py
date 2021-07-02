# 2 - masala. butun sonlardan iborat ro'yhat berilgan juftlarni ekranga chiqaring:

sonlar = [1, 2, 3, 4, 5, 6]
for son in sonlar:
    if son % 2 == 0:
        print(son)

# 3 - masala. Butun sonlardan iborat ro'yhat berilgan
# oldin juftlarini keyin toqlarini yangi ro'yhatga o'zlashtrib konsolga chiqaring

sonlar = [1, 2, 3, 4, 5, 6]
sonlar1 = []

# birinchi juftlarini o'zlashtiramiz
for son in sonlar:
    if son % 2 == 0:
        sonlar1.append(son)

# ikkinchi toqlarini o'zlashtiramiz
for son in sonlar:
    if son % 2 == 1:
        sonlar1.append(son)

print(sonlar1)

# 4 - masala. Butun sonlardan iborat ro'yhat berilgan.
# Toq elementlarini kvadratlariga,
# juft elementlarini ikkilanganiga almashtiring

sonlar = [1, 2, 3, 4, 5, 6]

print(sonlar)
for son in sonlar:
    if son % 2 == 0:
        sonlar[sonlar.index(son)] = son * 2
    elif son % 2 == 1:
        print(sonlar.index(son))
        sonlar[sonlar.index(son)] = son ** 2

print(sonlar)
