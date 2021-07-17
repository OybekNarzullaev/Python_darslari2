import datetime as dt
#
# while True:
#     print(datetime.datetime.now())

# vaqt = dt.datetime.now()
#
# print(vaqt.year)  # yil
# print(vaqt.month)  # oy
# print(vaqt.day)  # kun
# print(vaqt.weekday())  # hafta kuni 0 dan boshlanadi
# print(vaqt.hour)  # soat
# print(vaqt.minute)  # minut
# print(vaqt.second)  # sekund
# print(vaqt.microsecond)  # mikrosekund
# t = dt.datetime.now()
# def vaqt(t):
#     print(f"soat: {t.hour}:{t.minute} bo'ldi")
# vaqt(t)

""" vaqtni belgilash """

x = dt.datetime(2021, 7, 15, 2, 1, 3)
print(x.strftime("%a"))  # Thu
print(x.strftime("%A"))
print(x.strftime("%B"))
print(x.strftime("%b"))

import datetime as dt

x = dt.datetime.now().second
while True:
    print(dt.datetime.now().second - x)
    if x + 5 == dt.datetime.now().second:
        print("salom")
        x = dt.datetime.now().second
        break
