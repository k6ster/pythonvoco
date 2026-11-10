from pathlib import Path

nimed = []
tulemused = []
with open(Path(__file__).with_name("tulemused.csv"), encoding="utf-8") as fail:
    for rida in fail:
        nimi, tulemus = rida.strip().split(";")
        nimed.append(nimi)
        tulemused.append(float(tulemus))
for i in range(len(nimed)):
    print(nimed[i], "–", tulemused[i], "m")
parim = max(tulemused)
keskmine = sum(tulemused) / len(tulemused)
print("Parim tulemus:", parim)
for i in range(len(nimed)):
    if tulemused[i] == parim:
        print("Võitja:", nimed[i])
print("Keskmine tulemus:", keskmine)
print("Üle keskmise tulemusega sportlased:")
for i in range(len(nimed)):
    if tulemused[i] > keskmine:
        print(nimed[i], tulemused[i])
