from pathlib import Path


sisend = Path(__file__).parent / "nimed.txt"
with open(sisend, encoding="utf-8") as fail:
    nimed = [rida.strip() for rida in fail if rida.strip()]
if nimed:
    print(f"Esimene nimi: {nimed[0]}")
    print(f"Viimane nimi: {nimed[-1]}")
else:
    print("Failis pole nimesid.")
