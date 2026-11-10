kogus = 0
summa = 0
positiivsed = 0
negatiivsed = 0
paaris = 0
paaritud = 0
arv = int(input("Sisesta arv: "))
while arv != 0:
    kogus = kogus + 1
    summa = summa + arv
    if arv > 0:
        positiivsed = positiivsed + 1
    elif arv < 0:
        negatiivsed = negatiivsed + 1
    if arv % 2 == 0:
        paaris = paaris + 1
    else:
        paaritud = paaritud + 1
    arv = int(input("Sisesta arv: "))
if kogus == 0:
    print("Ühtegi arvu ei sisestatud.")
else:
    print("--- TULEMUSED ---")
    print("Sisestatud arve:", kogus)
    print("Summa:", summa)
    print(f"Keskmine: {summa / kogus:.2f}")
    print("Positiivseid arve:", positiivsed)
    print("Negatiivseid arve:", negatiivsed)
    print("Paarisarve:", paaris)
    print("Paarituid arve:", paaritud)
