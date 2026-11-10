from pathlib import Path

read = Path("muuk.txt")
read.write_text("Piim 2.50 10\nLeib 1.80 15\n", encoding="utf-8")
tulu = [nimi + " " + str(float(hind) * int(kogus)) for nimi, hind, kogus in (r.split() for r in read.read_text(encoding="utf-8").splitlines())]
Path("muugiaruanne.txt").write_text("\n".join(tulu), encoding="utf-8")
print("Aruanne valmis")
