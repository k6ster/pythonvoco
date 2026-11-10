from random import randint

i = 1
summa = 0
while i <= 10:
    vise = randint(1, 6)
    print(f"{i}. vise: {vise}")
    summa = summa + vise
    i = i + 1
print("Visete summa:", summa)
print("Keskmine tulemus:", summa / 10)
