from pathlib import Path


fail = Path(__file__).parent / "hinded.txt"
opilased = []
with open(fail, encoding="utf-8") as sisend:
    for rida in sisend:
        nimi, hinne = rida.split()
        opilased.append((nimi, int(hinne)))

hinded = [hinne for _, hinne in opilased]
print(f"Keskmine hinne: {sum(hinded) / len(hinded):.2f}")
print(f"Kõrgeim hinne: {max(hinded)}")
print(f"Madalaim hinne: {min(hinded)}")
print("Õpilased hindega vähemalt 4:")
for nimi, hinne in opilased:
    if hinne >= 4:
        print(nimi)
