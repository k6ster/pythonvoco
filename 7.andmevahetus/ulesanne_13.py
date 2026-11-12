from pathlib import Path


fail = Path(__file__).parent / "opilased.txt"
opilased = []
with open(fail, encoding="utf-8") as sisend:
    for rida in sisend:
        osad = rida.split()
        opilased.append((osad[0], [int(hinne) for hinne in osad[1:]]))

for nimi, hinded in opilased:
    print(f"{nimi}: {len(hinded)} hinnet, keskmine {sum(hinded) / len(hinded):.2f}")
rohkem_hindeid = max(opilased, key=lambda opilane: len(opilane[1]))
print(f"Kõige rohkem hindeid: {rohkem_hindeid[0]}")
