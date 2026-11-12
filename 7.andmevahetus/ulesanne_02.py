from pathlib import Path


sisend = Path(__file__).parent / "tervitus.txt"
with open(sisend, encoding="utf-8") as fail:
    for number, rida in enumerate(fail, start=1):
        print(f"{number}: {rida.rstrip()}")
