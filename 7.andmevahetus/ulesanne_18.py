from pathlib import Path


failitee = Path(__file__).parent / "sisestatud_arvud.txt"
arvud = []
while len(arvud) < 5:
    try:
        arvud.append(int(input(f"Sisesta täisarv ({len(arvud) + 1}/5): ")))
    except ValueError:
        print("Palun sisesta täisarv.")

failitee.write_text("".join(f"{arv}\n" for arv in arvud), encoding="utf-8")
with open(failitee, encoding="utf-8") as fail:
    loetud = [int(rida) for rida in fail if rida.strip()]
print("Sisestatud arvud:", ", ".join(map(str, loetud)))
print("Summa:", sum(loetud))
print("Keskmine:", sum(loetud) / len(loetud))
