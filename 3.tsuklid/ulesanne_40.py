kogus = 0
summa = 0
hind = float(input("Sisesta hind: "))
while hind != 0:
    kogus = kogus + 1
    summa = summa + hind
    hind = float(input("Sisesta hind: "))
print("Tooteid:", kogus)
print(f"Kokku: {summa:.2f} €")
