""" copy() parametri yo'q """

mevalar1 = {"Olma", "Anor"}

mevalar2 = mevalar1.copy()

print(f"{mevalar1} {mevalar2} ")

# nusxalashni o'zlashtirish amali bilan ham bajarsa bo'ladi

mevalar3 = mevalar1
mevalar1.clear()
print(mevalar3)  # bu o'chib ketadi chunki bu o'zlashtirishdan hosil bo'lgan
print(mevalar2)  # bu o'chmaydi chunki bu nusxalangan

""" difference() parametri bor u set qabul qiladi"""
mevalar1 = {"Olma", "Anor", "Olcha"}
mevalar2 = {"Apelsin", "Anor", "Ananas"}

print(mevalar1.difference(mevalar2))  # mevalar1 ni mevalar2 dan farqi

""" difference_update() parametr bor """
mevalar1 = {"Olma", "Anor", "Olcha"}
mevalar2 = {"Apelsin", "Anor", "Ananas"}

mevalar1.difference_update(mevalar2)  # mevalar1 ni mevalar2 dan farqini o'ziga o'zlashtiradi
print(mevalar1)

""" intersection() kesishma ikkisida ham borlarini oladi """
mevalar1 = {"Olma", "Anor", "Olcha"}
mevalar2 = {"Apelsin", "Anor", "Ananas"}

print(mevalar1.intersection(mevalar2))

""" intersection_update ikkisida ham borlarini o'ziga o'zlashtiradi"""
mevalar1 = {"Olma", "Anor", "Olcha"}
mevalar2 = {"Apelsin", "Anor", "Ananas"}

mevalar1.intersection_update(mevalar2)
print(mevalar1)

""" isdisjoin() bu agar bitta setni ikkinchi setda bir xil elementi 
    bo'lmasa True bo'lsa False qaytaradi"""
mevalar1 = {"Olma", "Anor", "Olcha"}
mevalar2 = {"Apelsin", "Anor", "Ananas"}

print(mevalar1.isdisjoint(mevalar2))  # hozirgi holarda False chunki ikkisida ham anor bor

""" issubset() -> set1.issubset(set2) - agar set2 ichida set1 bo'lsa True aks holsa False """
mevalar1 = {"Olma", "Anor", "Olcha", "Ananas"}
mevalar2 = {"Anor", "Olma"}

print(mevalar2.issubset(mevalar1))

""" issuperset() -> set1.issuperset(set2) agar set1 ni ichida set2 bo'lsa True aks holda False """
mevalar1 = {"Olma", "Anor", "Olcha", "Ananas"}
mevalar2 = {"Anor", "Olma"}

print(mevalar2.issuperset(mevalar1))  # hozirgi holatda False

""" symmetric_difference() set3 = set1.symmetric_difference(set2) set1 va set2 dagi bir xil 
    elementlarini olib tashlab qolganlarini set3 ga o'zlashtiradi"""

mevalar1 = {"Olma", "Anor", "Olcha", "Ananas"}
mevalar2 = {"Anor", "Olma", "Apelsin", "Mandarin"}

mevalar3 = mevalar1.symmetric_difference(mevalar2)
print(mevalar3)

""" symmetric_difference_update() set1.symmetric_difference(set2) set1 va set2 dagi bir xil 
    elementlarini olib tashlab qolganlarini set1 o'ziga o'zlashtiradi"""

mevalar1 = {"Olma", "Anor", "Olcha", "Ananas"}
mevalar2 = {"Anor", "Olma", "Apelsin", "Mandarin"}

mevalar1.symmetric_difference_update(mevalar2)
print(mevalar1)

""" union -> set1.union(set2) -> set1 va set2 ni birlashmasi"""
mevalar1 = {"Olma", "Anor", "Olcha", "Ananas"}
mevalar2 = {"Anor", "Olma", "Apelsin", "Mandarin"}

mevalar3 = mevalar1.union(mevalar2)

print(mevalar3)
