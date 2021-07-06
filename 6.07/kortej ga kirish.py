""" kortejlar (tuple) """

numbers = (1, 2, 3, 4)  # bu kortej -> tuple
numbers1 = [1, 2, 3, 4]  # bu ro'yhat -> list

print(type(numbers))
print(type(numbers1))

# ! kortejni yangilab bo'lmaydi
# numbers[4] = 4 # bu xato ish

print('-------------------------------------')
""" konstruktor """
a = tuple([1, 2, 3, 4])
print(type(a))

""" kortej elementlariga murojaat """
numbers = (1, 2, 3, 4)
print(numbers[1])
# bu amallar index lar orqali amalga oshiriladi

print('-------------------------------------')
""" kortejda yangilashni faqat ro'yhatga o'tkazib keyin bajarsa bo'ladi """
numbers = (1, 2, 3, 4)

# avval kortejni ro'yhatga aylantiramiz
numbers = list(numbers)

# endi yangilaymiz
numbers[1] = 9

# endi ro'yhatni kortejga aylantiraman
numbers = tuple(numbers)
print(numbers)

print('-------------------------------------')
""" kortej elementlarini looplar (for, while) yordamida alohida qilib chiqarish """
numbers = (1, 2, 3, 4)
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

for i in numbers:
    print(i)

# fordan indeks bo'yicha foydalanish
for i in range(len(numbers)):
    print(numbers[i])

print('-------------------------------------')
""" kortejlarni qo'shish """
numbers1 = (1, 2, 3)
numbers2 = (4, 5, 6)

# qo'shish
numbersAll = numbers1 + numbers2

print(numbersAll)
print('-------------------------------------')

""" ko'rtejlarni songa ko'paytirish """
numbers = (1, 2, 3, 4)
myNumbers = numbers * 2

print(myNumbers)
print('-------------------------------------')

""" Kortej metodlari """
numbers = (1, 2, 3, 4, 4, 3, 2, 2)

# count()
print(numbers.count(2))

# index()
print(numbers.index(2))
print('-------------------------------------')

# masala:
x = (1)
y = (1,)

print(type(x))
print(type(y))

# yo'qlik qiymatlar
a = None
b = ''
c = []
d = ()
e = 0
h = False
print(f" {bool(a)} {bool(b)} {bool(c)} {bool(d)} {bool(e)} {bool(h)}")

