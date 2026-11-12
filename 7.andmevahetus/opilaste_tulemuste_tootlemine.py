from pathlib import Path

LAHED = {90: 5, 75: 4, 60: 3, 50: 2, 0: 1}

def hinne(keskmine):
    for piir, tulemus in LAHED.items():
        if keskmine >= piir:
            return tulemus

def loe_andmed(fail):
    opilased = []
    with open(fail, encoding="utf-8") as allikas:
        for rida in allikas:
            osad = rida.strip().split(";")
            if len(osad) == 4:
                nimi = osad[0]
                tulemused = [int(x) for x in osad[1:]]
                keskmine = sum(tulemused) / len(tulemused)
                opilased.append((nimi, keskmine, hinne(keskmine)))
    return opilased

sisend = Path(__file__).with_name("tulemused.txt")
if not sisend.exists():
    print("Viga: lähtefaili tulemused.txt ei leitud.")
    raise SystemExit

opilased = loe_andmed(sisend)
read = ["ÕPILASTE TULEMUSTE ARUANNE", "------------------------------"]
for nimi, keskmine, hinne_nr in opilased:
    read.append(f"{nimi:<10} Keskmine: {keskmine:.2f}  Hinne: {hinne_nr}")
if opilased:
    parim = max(opilased, key=lambda x: x[1])
    norgim = min(opilased, key=lambda x: x[1])
    read.extend([
        "------------------------------",
        f"Klassi keskmine: {sum(x[1] for x in opilased) / len(opilased):.2f}",
        f"Parim õpilane: {parim[0]}",
        f"Nõrgim õpilane: {norgim[0]}",
        f"Positiivse hindega õpilasi: {sum(x[2] >= 3 for x in opilased)}",
    ])
print("\n".join(read))
Path(__file__).with_name("aruanne.txt").write_text("\n".join(read), encoding="utf-8")
