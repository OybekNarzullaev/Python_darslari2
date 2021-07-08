import random as rd

A = []
B = []
C = []
# A va b to'plamlarni birlashmasini olib C to'plam bilan kesishmasini olasiz

for i in range(10):
    A.append(rd.randint(1, 10))
    B.append(rd.randint(1, 10))
    C.append(rd.randint(1, 10))


print(A)
print(B)
AUB = set(A + B)
print(AUB)

AUB = list(AUB)
C = set(C)
print(C)

D = []

for i in C:
    if i in AUB:
        D.append(i)

D = set(D)
print(D)
