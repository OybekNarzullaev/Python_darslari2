# 8 - masala

n = int(input("n = "))
a = []

# massiv elementlarini kiritamiz
for i in range(n):  # 0 dan n (n kirmaydi) gacha qadam
    j = int(input(f"j{i} = "))
    a.append(j)  # joylash

juftIndex = []
for i in range(n):
    if a[i] % 2 == 0:
        juftIndex.append(i)

# kamayish tartibida saralaymiz
juftIndex.sort(reverse=True)  # reverse=True degani kamayish tartibini anglatadi
print(juftIndex)  # ekranga chqaramiz
print(f"Juft sonlar soni -> {len(juftIndex)}")
