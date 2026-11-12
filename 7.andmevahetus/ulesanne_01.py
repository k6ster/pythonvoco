from pathlib import Path


sisend = Path(__file__).parent / "tervitus.txt"
with open(sisend, encoding="utf-8") as fail:
    print(fail.read())
