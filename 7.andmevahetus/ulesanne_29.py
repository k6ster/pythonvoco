from pathlib import Path


kaust = Path(__file__).parent
allikas = kaust / "muuk.txt"
read = allikas.read_text(encoding="utf-8").splitlines()
tooted = []
for rida in read:
    nimi, hind, kogus = rida.split()
    tulu = float(hind) * int(kogus)
    tooted.append((nimi, tulu))

kokku = sum(tulu for _, tulu in tooted)
suurim = max(tooted, key=lambda kirje: kirje[1])
aruanne = [f"{nimi}: {tulu:.2f} €" for nimi, tulu in tooted]
aruanne.extend([f"Kogu müügitulu: {kokku:.2f} €", f"Suurima tuluga toode: {suurim[0]} ({suurim[1]:.2f} €)"])
tekst = "\n".join(aruanne)
(kaust / "muugiaruanne.txt").write_text(tekst, encoding="utf-8")
print(tekst)
