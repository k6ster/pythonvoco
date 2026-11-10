from pathlib import Path

kogus = 0
summa = 0
with open(Path(__file__).with_name("arvud.txt"), encoding="utf-8") as fail:
    for rida in fail:
        summa = summa + int(rida.strip())
        kogus = kogus + 1
print("Arvude arv:", kogus)
print("Arvude summa:", summa)
