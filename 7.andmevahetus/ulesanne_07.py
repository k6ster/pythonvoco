from pathlib import Path


failinimi = input("Sisesta failinimi: ").strip()
failitee = Path(failinimi)
if not failitee.is_absolute():
    failitee = Path(__file__).parent / failitee
try:
    with open(failitee, encoding="utf-8") as fail:
        print(fail.read())
except FileNotFoundError:
    print("Viga: sellist faili ei leitud.")
