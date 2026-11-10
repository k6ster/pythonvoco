from pathlib import Path

Path("numbrid.txt").write_text("3\n12\n8\n", encoding="utf-8")
arvud = [int(x) for x in Path("numbrid.txt").read_text(encoding="utf-8").split()]
Path("summa.txt").write_text(str(sum(arvud)), encoding="utf-8")
print("Salvestatud")
