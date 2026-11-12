from pathlib import Path


fail = Path(__file__).parent / "algtekst.txt"
tekst = fail.read_text(encoding="utf-8")
read = tekst.splitlines()
sonad = tekst.split()
print(f"Ridu: {len(read)}")
print(f"Sõnu: {len(sonad)}")
print(f"Tähemärke: {len(tekst)}")
print(f"Mittetühje ridu: {sum(bool(rida.strip()) for rida in read)}")
print(f"Keskmiselt sõnu rea kohta: {len(sonad) / len(read):.2f}")
