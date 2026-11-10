from pathlib import Path

Path("filtreeri.txt").write_text("2\n5\n8\n11\n", encoding="utf-8")
arvud = [int(r) for r in Path("filtreeri.txt").read_text(encoding="utf-8").split()]
print([arv for arv in arvud if arv % 2 == 0])
