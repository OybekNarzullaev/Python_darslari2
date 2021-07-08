# # maxsus masala:
# shaxslar = [
#     {
#         "ism": "Shoxzod",
#         "yoshi": 20,
#         "jinsi": "erkak"
#     },
#     {
#         "ism": "Oybek",
#         "yoshi": 22,
#         "jinsi": "erkak"
#     },
#     {
#         "ism": "Bunyod",
#         "yoshi": 22,
#         "jinsi": "erkak"
#     },
#     {
#         "ism": "Madinabonu",
#         "yoshi": 13,
#         "jinsi": "erkak"
#     }
# ]
#
# for shaxs in shaxslar:
#     if shaxs["yoshi"] > 20:
#         print(shaxs["ism"])
#
# maxsus masala 4

person1 = {
    "name": "John",
    "father": "Bill",
    "mother": "Anna",
    "married": 0
}
person2 = {
    "name": "Kate",
    "father": "Pet",
    "mother": "Maria",
    "married": 0
}

year1 = int(input("person1 was married"))
year2 = int(input("person2 was married"))

# 1) year1 va year2 ni personlarga kiritasiz
# 2) agar year1 == year2 bo'lsa
#   person3 ni yaratasiz
#   person3 ni ota onasi -> person1 va person2
# 3) agar year1 != year2 bo'sa
#   they were not married together
