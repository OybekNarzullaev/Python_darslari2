# 1 - masala.
# 1. o'quvchilar ro'yhatini e'lon qiling unga oxiriga yangi o'quvchi qo'shing (print qiling) append
# 2. keyin o'rtasiga yangi o'quvchi qo'shing (print qiling) insert
# 3. o'quvchilar sonini toping (print qiling) len
# 4. o'quvchilar ro'yhatiga yana bor ismlardan birini kiriting
#    va shu ismli o'quvchi nechtaligini toping (print qiling) append yoki insert , count
# 5. yangi o'quvchilar ro'yhatini e'lon qilib eski ro'yhatga ulang
#    va eski ro'yhatni (print qiling) extend
# 6. ixtiyoriy o'quvchini indeksini topib bering (print qiling) index
# 7. ro'yhatni tozalang (print qiling) clear

# maxsus masala 1. ro'yhat berilgan. input qilingan yangi o'zgaruvchini input qilingan
# yangi indeksga insert metodisiz joylashtiring
# masalan:
# sonlar = [1, 2, 3, 4] bo'lsin
# input -> element = 10, index = 2
# javobi ikkinchi indeksga 10 degan son kiritilsin
# sonlar = [1, 2, 10, 3, 4]

sonlar = [1, 2, 3, 4, 5, 6]

print(sonlar)
for son in sonlar:
    if son % 2 == 0:
        sonlar[sonlar.index(son)] = son * 2
    elif son % 2 == 1:
        print(sonlar.index(son))
        sonlar[sonlar.index(son)] = son ** 2

print(sonlar)

# 5 - masala
# raqamini kiritasiz va shu indeksgacha fibonachi sonlar ro'yhatini tuzasiz
# fibonachi sonlari -> 1, 1, 2, 3, 5, 8, 13, 21 ...

indeks = int(input("=>"))

a = []

for i in range(indeks + 1):
    if i == 0 or i == 1:
        a.append(1)
    else:
        a.append(a[i - 1] + a[i - 2])

print(a)

# 6 - masala. ro'yhat berilgan. Har bir elementini o'zidan keyingi elementiga almashtiring.
# oxirgi elementni nolga tenglang

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(a)):
    if i == len(a) - 1:
        a[i] = 0
    else:
        a[i] = a[i + 1]
print(a)

