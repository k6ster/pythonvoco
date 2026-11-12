from pathlib import Path


sisend = Path(__file__).parent / "arvud.txt"
with open(sisend, encoding="utf-8") as fail:
    arvud = [int(rida) for rida in fail if rida.strip()]
paaris = sum(arv % 2 == 0 for arv in arvud)
print(f"Paarisarve: {paaris}")
print(f"Paarituid arve: {len(arvud) - paaris}")
