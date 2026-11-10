from pathlib import Path

Path("sonad.txt").write_text("koer kass koer lind", encoding="utf-8")
sonad = Path("sonad.txt").read_text(encoding="utf-8").split()
print(len(sonad), max(sonad, key=len))
