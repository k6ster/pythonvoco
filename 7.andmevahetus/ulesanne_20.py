from pathlib import Path


kaust = Path(__file__).parent
sisend = kaust / "arvud.txt"
valjund = kaust / "paarisarvud.txt"
with open(sisend, encoding="utf-8") as fail:
    arvud = [int(rida) for rida in fail if rida.strip()]
paarisarvud = [arv for arv in arvud if arv % 2 == 0]
valjund.write_text("".join(f"{arv}\n" for arv in paarisarvud), encoding="utf-8")
print(f"Paarisarve kirjutati faili {len(paarisarvud)}.")
