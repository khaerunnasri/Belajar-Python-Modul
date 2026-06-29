import random

print("Random 1 sampai 10 = ", random.randint(1, 10))
print("Random 1 sampai 100 = ", random.randint(1, 100))

list = ["Khaerun", "Nasri", "Siska", "Erika", "Jeni"]
pilih = random.choice(list)
print("Pilih dari list : ", pilih)

random.shuffle(list)
print("List random = ", list)