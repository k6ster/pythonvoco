from pathlib import Path


kaust = Path(__file__).parent
nimi = input("Nimi: ").strip()
vanus = input("Vanus: ").strip()
email = input("E-posti aadress: ").strip()
failitee = kaust / "kasutaja.txt"
failitee.write_text(f"{nimi}\n{vanus}\n{email}\n", encoding="utf-8")
print(failitee.read_text(encoding="utf-8"))
