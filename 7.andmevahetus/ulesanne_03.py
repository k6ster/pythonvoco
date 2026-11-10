from pathlib import Path

Path("readlines.txt").write_text("10\n20\n30\n", encoding="utf-8")
read = Path("readlines.txt").read_text(encoding="utf-8").splitlines()
print(len(read), read)
