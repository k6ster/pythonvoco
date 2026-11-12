from pathlib import Path


kaust = Path(__file__).parent
tekst = (kaust / "algtekst.txt").read_text(encoding="utf-8")
(kaust / "suured_tahed.txt").write_text(tekst.upper(), encoding="utf-8")
print("Suurte tähtedega tekst salvestati faili suured_tahed.txt.")
