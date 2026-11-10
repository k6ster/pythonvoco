from pathlib import Path

read = Path("arvud.txt")
read.write_text("12\n8\n4\n32\n", encoding="utf-8")
arvud = [int(x) for x in read.read_text(encoding="utf-8").split()]
paaris = [str(x) for x in arvud if x % 2 == 0]
Path("paarisarvud.txt").write_text("\n".join(paaris), encoding="utf-8")
print(f"Kirjutati {len(paaris)} arvu")
