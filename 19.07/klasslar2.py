# """ konstruktor """
#
# # 1. parametrsiz konstruktor
#
#
# class Son:
#     x = 5
#
#
# a = Son()  # Son klassi konstruktor
#
# # 2. parametrli konstruktor
#
#
# class Son1:
#     def __init__(self, x):
#         self.x = x
#
#
# b = Son1(7)
# print(b.x)
#
# # 1 - topshiriq. Ixtiyoriy parametrli va parametrsiz
# # konstruktorlar tuzib undan obyekt oling

# class Gap:
#     def __init__(self):
#         print("no paramter")
#
#
# class Person:
#     pass
#
#
# x = Person


""" sanagich o'rnatish yoki obyetlarni sanash """


class Student:
    sanagich = 0

    def __init__(self):
        Student.sanagich += 1


s1 = Student()
s2 = Student()
s3 = Student()
Student()
Student()

print(Student.sanagich)

