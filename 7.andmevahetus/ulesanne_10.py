from pathlib import Path

Path("mõõtmised.txt").write_text("12\n18\n25\n", encoding="utf-8")
arvud = [int(x) for x in Path("mõõtmised.txt").read_text(encoding="utf-8").split()]
print(f"Miinimum: {min(arvud)}, maksimum: {max(arvud)}")
