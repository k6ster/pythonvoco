from pathlib import Path

nimed = []
with open(Path(__file__).with_name("opilased.txt"), encoding="utf-8") as fail:
    for rida in fail:
        nimed.append(rida.strip())
otsitav = input("Otsitav nimi: ").lower()
leitud = False
for i in range(len(nimed)):
    if nimed[i].lower() == otsitav:
        print("Nimi leiti. Järjekorranumber:", i + 1)
        leitud = True
if not leitud:
    print("Nime ei leitud.")
