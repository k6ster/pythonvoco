from pathlib import Path


sisend = Path(__file__).parent / "arvud.txt"
with open(sisend, encoding="utf-8") as fail:
    arvud = [int(rida) for rida in fail if rida.strip()]
suurim = max(arvud)
vaikseim = min(arvud)
print(f"Suurim arv: {suurim}")
print(f"Väikseim arv: {vaikseim}")
print(f"Vahe: {suurim - vaikseim}")
