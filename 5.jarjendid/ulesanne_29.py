from pathlib import Path

arvud = []
with open(Path(__file__).with_name("arvud.txt"), encoding="utf-8") as fail:
    for rida in fail:
        arvud.append(int(rida.strip()))
print(arvud)
print("Suurim:", max(arvud))
print("Väikseim:", min(arvud))
print("Keskmine:", sum(arvud) / len(arvud))
print("Kasvavas järjekorras:", sorted(arvud))
