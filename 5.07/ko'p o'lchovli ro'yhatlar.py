""" Ro'yhatlar (Ko'p o'lchovli ro'yhatlar) """
numbers = [1, 2, 3, 4, 5, 'ha', True]

# Ro'yhatni o'zi ham ro'yhat elementi bo'la oladimi?
# Javob: ha

""" chop etish """
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list1 = [[[1, 2, 3], 2, 3], [4, 5, 6]]

for element in matrix:
    print(element)

for element in matrix:
    for raqam in element:
        print(raqam)

# satrlar ham massiv bo'la oladi:

satr = "O'zbekiston"

for harf in satr:
    print(harf)

gap = ["Men", "Pythonda", "ishlayapman"]
for suz in gap:
    print(suz)

for suz in gap:
    for harf in suz:
        print(harf)

""" indekslar bilan ishlash """

numbersList = [[1, 2, 3], [4, 5, 6], [7, 8, [1, 2, 3, 4, [5, 6]]]]
print(numbersList[2][0])
print(numbersList[2][2][4][1])

""" ko'p o'lchovli ro'yhatni yaratishni maxsus usullari """
numbersList = [[[1, 2, 3] * 1] * 3] * 2
print(numbersList)

numbersList = [[0] * 4 for i in range(4)]
print(numbersList)

""" 1 - masala. 10 raqamini indeksi orqali print qiling """

numbersList = [[1, 2, 3, 4], [0, [1, 2, [4, 5, [10, 11]], 4], 5], 12]

""" 2 - masala. 5 ni chiqarib bering"""
numbersList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

""" 3 - masala 2 ta 2X2 matritsa tuzib ularni qo'shing va javobini yangi matrisaga o'zlashtirib
    print qiling. """

A1 = [[1, 2], [3, 4]]

A2 = [[5, 6], [7, 8]]

B = [[[], []], [[], []]]
# B[0][0] = A1[0][0] + A2[0][0]
# B[0][1] = A1[0][1] + A2[0][1]
# B[1][0] = A1[1][0] + A2[1][0]
# B[1][1] = A1[1][1] + A2[1][1]
# print(B)

for i in range(2):
    for j in range(2):
        B[i][j] = A1[i][j] + A2[i][j]

print(B)

# 00 10
# 01 11

""" 4 - masala. 3X3 matritsa tuzib bering """

matrix = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

"""3X2"""
matrix = [[1, 2], [3, 4], [5, 6]]

B = [[[], [], []], [[], [], []], [[], [], []]]

for i in range(3):
    for j in range(3):
        B[i][j] = int(input(f"B[{i}][{j}] = "))

print(B)
""" 5 - masala. 3X3 matritsa har bir elementini alohida qatorga chiqaring """
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # matrintsani tuzamiz
# 1 -usul
for element in a:  # a ni ichidan qavs to'plamlarni oladi masalan [1, 2, 3]
    for i in element:  # olingan qavs to'plam ichidagi elementlarni oladi masalan [1, 2, 3] dan 1 ni oladi
        print(i)

# 2 - usul
for i in range(3):
    for j in range(3):
        print(a[i][j])

""" 6 - masala 2x2 ro'yhat berilgan ana shu ro'yhatni 1 o'lovchili ro'yhatga o'zlashriting
    masalan:
    [[1,2], [3, 4]] -> [1, 2, 3, 4]
 """

c = []  # c = [1, 2, 3, 4]
a = [[1, 2], [3, 4]]


for j in a:  # a ning ichidagi ro'yhatchalarni oladi
    for g in j:  # olingan ro'yhatchani ichidagi elementni oladi
        c.append(g)  # olingan elementni c ga joylaydi

print(c)

c = a[0] + a[1]  # bu degani: [1, 2] + [3, 4] = [1, 2, 3, 4]
print(c)


