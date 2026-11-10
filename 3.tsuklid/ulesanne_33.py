from random import randint

salajane = randint(1, 100)
arv = int(input("Arva arv 1–100: "))
while arv != salajane:
    if arv < salajane:
        print("Salajane arv on suurem.")
    else:
        print("Salajane arv on väiksem.")
    arv = int(input("Arva arv 1–100: "))
print("Õige!")
