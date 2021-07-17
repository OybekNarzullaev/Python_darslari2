# """ lambda funkdiya """
#
#
# def ikkilash(a):
#     return a * 2
#
#
# print(ikkilash(5))
#
#
# ikkilash1 = lambda a: a * 2  # return a * 2; a: nuqta esa ()
# print(ikkilash1(10))
#
# """
#     lambda -> def
#     ikkilash1 -> ikkilash
# """


# ikki va undan ortiq parameter

# def yigindi(a, b):
#     return a + b
#
#
# yigindi1 = lambda a, b: a + b
#
# print(yigindi(2, 3))
# print(yigindi1(1, 2))
#
# urt = lambda a, b, c, d: yigindi(yigindi1(a, b), yigindi1(c, d)) / 4
#
# urt1 = lambda a, b, c, d: (a + b + c + d) / 4
#
# print(urt1(1, 2, 3, 4))


# funksiyani ichida lambda

# masala. sonlar darajasini chiqarish:

def kvadrat(n):
    return lambda a: n ** 2


son = kvadrat(5)  # son = lambda a: a ** n

print(son(2))
print(kvadrat(5)(2))

# masala doirani uzunligini kiritish orqali funksiyani ichida lambdani qo'llab
# yuzsini chiqaring

# L = 2 * pi * R
# S = pi * (R ** 2)

def aynala(L):
    return lambda pi: pi * (L/(2 * pi))**2

x = aynala(10)

print(x(3.14))

# 2 - masala.


def paralelopiped(a, b):
    return lambda c: a * b * c

x = paralelopiped(2, 3)
print(x(5))

# ikki sonning ko'paytmasi


def kub(a):
    return lambda b: a * b


y = kub(5)
print(y(2))


def kub(a):
    return a


y = lambda b: kub(5) * b

# ikki sonni yig'indisini n - darajasini chiqaring


def yigindi(a, b):
    d = a + b
    return lambda n: d ** n

x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
k = yigindi(x, y)  # d = 5

print(k(z))

# ismingizni input qilasiz uni n marta chiqarasiz:


def ism(i):
    return lambda n: (i + ' ') * n


k = input("ismingizni kiriting: ")
n_ta_ism = ism(k)
print(n_ta_ism(5))