def PowerA3(*n):
    k = []
    for i in range(len(n)):
        k.append(n[i] ** 3)
    return k


A = 1.1
B = 2.2
C = 3.3

D = 1
E = 2

a = PowerA3(A, B, C, D, E)

for i in a:
    print(i)

