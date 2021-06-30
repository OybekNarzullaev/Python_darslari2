# 1 dan 100 gacha bo'lgan sonlarni kirting lekin oxiri 0,1,2,3,4,5 bilan tugaydigan ikki xonali sonlar chiqmasin

for son in range(1, 101):
    if son % 10 <= 5 and son // 10 > 0:
        continue
    print(son)


# maxsus masala 2. matn va ism kiritasiz. Va siz kiritgan ismning hamma harflari ketma-ket matn tarkibi mavjudmi yoki yo'qmi tekshirasiz
# masalan: matn = Ozod vatan yashna gulla bo'stonli elim kelajagi buyuk. ism = Oybek
#                 O          y            b         e    k


