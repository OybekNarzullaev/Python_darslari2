# 3 - masala kortej elementlarini o'rta arifmetigini topish
numbers = (10, 2, 3, 4, 5, 6)

urta_arifmetik = sum(numbers)/len(numbers)

print(urta_arifmetik)

# maxsus usul
i = 0
summa = 0
for number in numbers:
    i += 1
    summa += number

urta_arifmetik = summa / i
print(urta_arifmetik)




