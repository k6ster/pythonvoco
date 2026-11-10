from pathlib import Path

Path("naidis.txt").write_text("Esimene rida\nTeine rida\n", encoding="utf-8")
print(Path("naidis.txt").read_text(encoding="utf-8"))
