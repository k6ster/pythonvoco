from pathlib import Path


sisend = Path(__file__).parent / "nimed.txt"
with open(sisend, encoding="utf-8") as fail:
    nimed = [rida.strip() for rida in fail if rida.strip()]
print(f"Failis on {len(nimed)} nime.")
