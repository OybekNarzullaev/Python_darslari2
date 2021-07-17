import datetime as dt

n = int(input("Savollar sonini kiriting: "))
testVaqti = 0
testlar = []
testSavoli = {
    "savol": "",
    "javoblar": [
        '',
        '',
        ''
    ],
    "kalit": "A"
}

for i in range(n):
    print(i + 1, " - savolni tuzamiz:")
    print("Savolni kiriting: ", end=" ")
    testSavoli["savol"] = input()
    for j in range(3):
        print(f"Javob {j + 1} ni kiriting: ", end=' ')
        testSavoli["javoblar"][j] = input()
    print("to'g'ri javob indeksini kiriting yani A, B, C")
    testSavoli["kalit"] = input()
    testSavoli["kalit"] = testSavoli["kalit"].upper()
    testShablon = testSavoli.copy()
    testlar.append(testShablon)
testVaqti = int(input("Test vaqtini kiriting (sekund): "))
print("Tayyor!!!")

print("Boshlash uchun ixtiyoriy klavishni bosing")
vaqt = dt.datetime.now().second
z = input()
tugri_javoblar = 0
print("boshlandi omad!!!")

while True:
    if int(vaqt + testVaqti) == int(dt.datetime.now().second):
        print("vaqt tugadi")
        break
    for i in range(n):
        print(i + 1, " - savol. ", testlar[i]['savol'])
        for j in range(3):
            print(f"{j + 1} {testlar[i]['javoblar'][j]}")
        k = input("tog'ri javobni kiriting(A,B,C): ")
        if k == testlar[i]["kalit"]:
            tugri_javoblar += 1

print(f"siz {tugri_javoblar} ta to'g'ri ishlagansiz!")

