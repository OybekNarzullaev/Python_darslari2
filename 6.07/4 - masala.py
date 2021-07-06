# 4 - masala.
# birinchi avval juft o'rindagilarini keyin toq o'rindagilarini chiqaring
a = (1, 4, 10, 6, 7)  # e'lon qilish
juft = []  # juft degan ro'yhat
toq = []  # toq degan ro'yhat
for i in range(len(a)):
    if (i + 1) % 2 == 0:
        juft.append(a[i])
    else:
        toq.append(a[i])
print(juft)
print(toq)

# 2 - usul
a = (1, 4, 10, 6, 7)  # e'lon qilish
for i in range(1, len(a), 2):
    print(a[i])
for i in range(0, len(a), 2):
    print(a[i])
