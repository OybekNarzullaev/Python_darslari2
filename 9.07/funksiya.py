# # namunaviy masala
# a = [1, 2, 3, 4]
# b = [1, 2, 3, 4]
# c = [1, 2, 3, 4]
#
#
# # ro'yhatlarni 2 dan katta elementlarini ekranga chiqaring
# def myFunction(x):
#     for i in x:
#         if i > 2:
#             print(i)
#
#
# myFunction(a)
# myFunction(b)
# myFunction(c)

""" funcksiyalar va protseduralar """
# funksiyani yaratish
# def <funksiya_nomi> (<parametrlari>):
#        <amallar>
#    return <o'zgaruvchi>

#
# def salom():
#     print("salom")
#
# # funskiyani chaqirish
# salom()
#
#
# # argument va parametr
# # 1) funksiyani e'lon qilish
# def salom(name):   # bu yerda name parameter
#     print(f"Salom {name}")
#
# # 2) funksiyani chaqirish
# ism = input("ismingizni kiritng: ")
# salom(ism)

# """ ko'p parameterli funksiya"""
#
#
# def tuliq_ism(ism, familiyani):
#     tuliq = ism + ' ' + familiyani
#     print(tuliq)
#
#
# tuliq_ism("Oybek", "Narzullayev")
# tuliq_ism("John", "Doe")
#
# """ *args -> bu parametrlar to'plami """
#
#
# def ismlar_ruyhati(*ism):
#     print(ism)
#
#
# ismlar_ruyhati("Oybek", "Shoxzod", "Muhammad", "Ibrohim")
#
#
# def fanlar_ruyhati(*fan):
#     print(fan)
#
#
# fanlar_ruyhati("Matematika", "Fizika", "Informatika")
#
# """ keyword -> kalit so'z """
#
#
# def tuliq_ism(ism, famliya):
#     print(f"{ism} {famliya}")
#
#
# firstname = input("ism : ")
# lastname = input("familiya : ")
# tuliq_ism(famliya=lastname, ism=firstname)

# """ many keyword  **args-> kalit so'zlar to'plami """
#
#
# def uquvchi(**x):
#     print(x)
#
#
# malumot = dict({})
# uquvchi(ismi="Ibrohim", yoshi=18, millati="O'zbek")
#
#
# def myfunction(tulov=0):
#     print(f"sizdan {tulov} so'm")
#
#
# myfunction(20000)
# myfunction(10000)
# myfunction()
#
#
# def rang(r="qora"):
#     print(f"men yoqtirgan rang: {r}")
#
#
# rang("oq")
# rang()

# """ ro'yhat argument sifatida """
#
#
# def uquvchilar(x):
#     for i in x:
#         print(i)
#
#
# uquvchi = ["Oybek", "Shoxzod", "Madinabonu"]
#
# uquvchilar(uquvchi)

# """ pass """
#
#
# def main1():
#     pass
#
#
# main1()
# print("salom")


