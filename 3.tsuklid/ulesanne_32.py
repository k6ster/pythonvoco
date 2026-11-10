from random import randint

salajane = randint(1, 10)
arv = int(input("Arva arv 1–10: "))
while arv != salajane:
    print("Vale!")
    arv = int(input("Arva arv 1–10: "))
print("Õige!")
