from pathlib import Path


sisend = Path(__file__).parent / "tekst.txt"
with open(sisend, encoding="utf-8") as fail:
    tekst = fail.read()
print(f"Tekstis on {len(tekst.split())} sõna.")
