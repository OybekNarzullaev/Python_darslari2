def minmax(x, y):
    if x > y:
        x = x + y
        y = x - y
        x = x - y
    return x, y


a = 1
b = 2
c = 3
d = 4


minmax(a, b)
minmax(a, d)
minmax(b, c)
minmax(d, b)

