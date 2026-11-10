from pathlib import Path

Path("arvud.txt").write_text("4\n7\n9\n", encoding="utf-8")
arvud = [int(r) for r in Path("arvud.txt").read_text(encoding="utf-8").split()]
print(sum(arvud), sum(arvud) / len(arvud))
