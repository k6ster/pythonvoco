from pathlib import Path

nimed = []
punktid = []
hinded = []
with open(Path(__file__).with_name("kontrolltoo.csv"), encoding="utf-8") as fail:
    for rida in fail:
        nimi, punktisumma = rida.strip().split(";")
        nimed.append(nimi)
        punktid.append(int(punktisumma))
print("KONTROLLTÖÖ TULEMUSED")
for i in range(len(nimed)):
    print(f"{i + 1}. {nimed[i]} – {punktid[i]} punkti")
sooritas = 0
for punktisumma in punktid:
    if punktisumma >= 50:
        sooritas = sooritas + 1
    if punktisumma >= 90:
        hinne = 5
    elif punktisumma >= 75:
        hinne = 4
    elif punktisumma >= 50:
        hinne = 3
    elif punktisumma >= 20:
        hinne = 2
    else:
        hinne = 1
    hinded.append(hinne)
print("KONTROLLTÖÖ STATISTIKA")
print("Õpilasi kokku:", len(nimed))
print("Keskmine punktisumma:", sum(punktid) / len(punktid))
for i in range(len(nimed)):
    if punktid[i] == max(punktid):
        print(f"Parim tulemus: {nimed[i]} – {punktid[i]} punkti")
    if punktid[i] == min(punktid):
        print(f"Madalaim tulemus: {nimed[i]} – {punktid[i]} punkti")
print("Kontrolltöö sooritas:", sooritas, "õpilast")
print("Kontrolltööd ei sooritanud:", len(nimed) - sooritas, "õpilast")
print("HINDED")
for i in range(len(nimed)):
    print(f"{nimed[i]} – {punktid[i]} punkti – hinne {hinded[i]}")
print("ÕPILASE OTSIMINE")
otsitav = input("Sisesta õpilase nimi: ").lower()
leitud = False
for i in range(len(nimed)):
    if nimed[i].lower() == otsitav:
        print("Õpilane:", nimed[i])
        print("Punktid:", punktid[i])
        print("Hinne:", hinded[i])
        leitud = True
if not leitud:
    print("Sellist õpilast ei leitud.")
