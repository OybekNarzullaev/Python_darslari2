# # ajdod klass
# class Nokia:
#     def __init__(self, markasi, gaplashish, sms, kamera):
#         self.markasi = markasi
#         self.gaplashish = gaplashish
#         self.sms = sms
#         self.kamera = kamera
#
#
# # voris olamiz:
# class Samsung(Nokia):
#     def yangilik(self, telegram, instagram, hdcamera):
#         self.telegram = telegram
#         self.instagram = instagram
#         self.hdcamera = hdcamera
#
#
# nokia6300 = Nokia('nokia6300', True, True, True)
# print(nokia6300.markasi)
#
#
# samsungJ2 = Samsung("samsungJ2", True, True, True)
#
# samsungJ2.yangilik("telegram bor", "istagram bor", "hd camera bor")
#
#
# print(nokia6300.__dict__)
# print(samsungJ2.__dict__)
#
#
# class SonAjdod:
#     def __init__(self, x):
#         self.x = x
#
#
# class Son1Voris(SonAjdod):
#     pass
#
#
# class Son2Voris(SonAjdod):
#     pass
#
#
# class Son3Voris(SonAjdod):
#     pass
#
#
#
# x1 = Son1Voris(5)
# x2 = Son2Voris(5)
# x3 = Son3Voris(5)
# y = SonAjdod(5)

# xulosa. bitta klasdan xohlagan voris olsa bo'ladi

# ixtiyoriy class tuzib undan voris oling hamda isbotlash uchun ikkalsini ham
# xususiyatlarini chiqaring

""" bitta klass xohlagancha klasslarga voris bo'la oladi """

#
# class Ota:
#     def __init__(self, x):
#         self.x = x
#
#
# class Ona:
#     def __init__(self, y):
#         self.y = y
#
#
# class Bola(Ota, Ona):
#     pass
#
#
# bola = Bola(5)
#
# bola.x = 5
# bola.y = 1
#
# print(f"{bola.x} {bola.y}")


# class Bobo:
#     def __init__(self, x):
#         self.x = x
#
#
# class Ota(Bobo):
#     def __init__(self, y):
#         self.y = y
#
#
# class Nabira(Ota):
#     def __init__(self, z):
#         self.z = z
#
#
# bobo = Bobo(1)
# ota = Ota(2)
# bola = Nabira(3)

# """ init """
#
#
# class Ota:
#     def __init__(self, z):
#         self.z = z
#
#
# class Bola(Ota):
#     def __init__(self, z, x):
#         self.x = x
#         Ota.__init__(self, z)
#
#
# x = Bola(5, 1)
# print(x.z)

""" super() """
class Ota:
    def __init__(self, z):
        self.z = z

class Ona:
    def __init__(self, y):
        self.y = y


class Bola(Ota, Ona):
    def __init__(self, x):
        super().__init__(x)


bola = Bola(5)
print(bola.y)
print(bola.z)
