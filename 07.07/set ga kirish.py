""" set ni yaratish """
# 1. gulli qavslar bilan
numbers = {1, 2, 3, 4, 5, 6}
print(type(numbers))

# 2. set() kosntruktori bilan
numbers = set([1, 2, 3, 4, 5])  # listni setga aylantirish
print(numbers)
print(type(numbers))

numbers = set((1, 2, 3, 4))
print(numbers)

""" elementlariga murojaat """
# Diqqat: setda indeks yo'q!!!
# setni listga aylantirish:
numbers = {1, 2, 3, 4, 5, 6}
numbers = list(numbers)  # endi numbers list ga aylandi
print(numbers)
print(numbers[0])


""" setni barcha elementlarini ko'rish """
numbers = {1, 2, 3, 4, 5, 6}
print(numbers)  # shunchaki setni o'zini print qilish
for i in numbers:
    print(i)


""" setda bir xil elementlar bo'lmadi """
fruits = {"apple", "orange", "banana", "apple"}
print(fruits)
# xulosa: set da bir xil element bo'lmaydi!


""" setda tarib muhimmas """
fruits = {"apple", "orange", "banana", "apple"}
fruits1 = {"orange", "apple", "banana"}
print(fruits1 == fruits)


""" element qo'shish """
mevalar = {"Olma", "Anor"}

# add funksiyasi bilan uning parametri mavjud bo'lishi shart! -> .metod(parametr)

mevalar.add("Shaftoli")
print(mevalar)
# set.method(parametr)

# update funksiyasi bilan  set.update(*element)
mevalar.update(["Gilos", "Olxori"])
print(mevalar)


""" elementni o'chirish:"""
# remove
fruits = {"apple", "orange", "banana", "Cherry"}
fruits.remove("banana")
print(fruits)

# pop
fruits.pop()
print(fruits)

# clear -> tozalash
fruits = {"apple", "orange", "banana", "Cherry"}
fruits.clear()  # bu bo'sh qiladi

print(fruits)

# del -> bu birato'la setni o'zini xotiradan o'chiradi
fruits = {"apple", "orange", "banana", "Cherry"}

del fruits
# print(fruits)
