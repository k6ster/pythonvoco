from pathlib import Path

read = Path("temperatuurid.txt")
read.write_text("Esmaspäev 12\nTeisipäev 15\nKolmapäev 11\n", encoding="utf-8")
andmed = [r.split() for r in read.read_text(encoding="utf-8").splitlines()]
print(sum(int(r[1]) for r in andmed) / len(andmed))
