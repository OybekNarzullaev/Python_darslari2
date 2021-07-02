sonlar = [1, 2, 3, 5, 4, 5, 6]

print(sonlar)
i = 0
while i < len(sonlar):
    if sonlar[i] % 2 == 0:
        sonlar[i] = sonlar[i] * 2
    else:
        sonlar[i] = sonlar[i] ** 2
    i += 1

print(sonlar)
