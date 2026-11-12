from pathlib import Path


sisend = Path(__file__).parent / "tooted.txt"
with open(sisend, encoding="utf-8") as fail:
    tooted = [rida.strip() for rida in fail if rida.strip()]

otsitav = input("Sisesta toode: ").strip().casefold()
if any(toode.casefold() == otsitav for toode in tooted):
    print("Toode leiti nimekirjast.")
else:
    print("Toodet ei leitud.")
