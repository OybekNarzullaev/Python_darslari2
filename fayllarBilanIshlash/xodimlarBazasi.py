from random import randint as ri

salt = ri(1, 1000)
f = open("baza.txt", 'w')
username = "Narzullayev"
password = "1234"
f.write(username + '\n' + str(hash(password) + salt))
f.close()

print("Tizimga kirish: ")
username = input("Login: ")
password = input("password: ")

f = open("baza.txt", 'r')

login = username in f.readline()
passw = str(hash(password) + salt) in f.readline()

if login and passw:
    print("tizimdan o'tdingiz!")
else:
    print("login yoki parol xato!")
