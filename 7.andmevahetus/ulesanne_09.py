from pathlib import Path

read = Path("read.txt").read_text(encoding="utf-8").splitlines()
Path("koopia.txt").write_text("\n".join(read), encoding="utf-8")
print("Koopia valmis")
