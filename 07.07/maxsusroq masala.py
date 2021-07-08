# tasodiy sonlar bilan to'diring bir xillarini o'chiring

import random

a = []
for i in range(10):
    k = random.randint(1, 10)
    a.append(k)

print(a)
a = set(a)
print(a)

# matematika, fizika, informatika fanlaridan olimpiada bo'ldi. Olimpiadalar ketma ket bo'ldi.\
# olimpiadaga kirgan o'quvchilar ro'yhatini chiqaring:

matematika = ["Ibrohim", "Muhammad", "Abbos", "Bunyod"]
fizika = ["Oybek", "Ibrohim", "Shoxzod", "Abbos"]
informatika = ["Oybek", "Ibrohim", "Abbos", "Shoxzod"]

a = matematika + fizika + informatika
a = set(a)
print(len(a))

# matematika nechta borgan  # Javob: 4 ta
# fizikaga nechta borgan  # Javob: 4 ta
# informatikaga nechta borgan  # javob: 4 ta
# matematika va fizikaga nechta bola borgan  # Javob: 6 ta
# fizika va informatika nechta borgan  # Javob: 4 ta
# matematika va informatikaga nechta borgan  # Javob:  6 ta
# umuman o'zi nechta bola olimpiadaga borgan  # Javob: 6 ta
