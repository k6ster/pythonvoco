from pathlib import Path


kaust = Path(__file__).parent
allikas = kaust / "mootmised.txt"
kehtivad = []
vigased = 0
with open(allikas, encoding="utf-8") as fail:
    for rida in fail:
        try:
            kehtivad.append(int(rida.strip()))
        except ValueError:
            vigased += 1

keskmine = sum(kehtivad) / len(kehtivad) if kehtivad else None
(kaust / "korrektsed_mootmised.txt").write_text(
    "".join(f"{arv}\n" for arv in kehtivad), encoding="utf-8"
)
print(f"Kehtivaid arvväärtusi: {len(kehtivad)}")
print(f"Vigaseid kirjeid: {vigased}")
print(f"Kehtivate väärtuste keskmine: {keskmine if keskmine is not None else 'arvutamiseks pole andmeid'}")
