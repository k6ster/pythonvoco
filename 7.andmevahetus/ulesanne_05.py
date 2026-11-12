from pathlib import Path


sisend = Path(__file__).parent / "arvud.txt"
with open(sisend, encoding="utf-8") as fail:
    arvud = [int(rida) for rida in fail if rida.strip()]
print("Arvud:", arvud)
print("Summa:", sum(arvud))
