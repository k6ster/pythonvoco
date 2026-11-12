from collections import Counter
from pathlib import Path
import re


kaust = Path(__file__).parent
failinimi = input("Analüüsitava faili nimi: ").strip()
sisend = Path(failinimi)
if not sisend.is_absolute():
    sisend = kaust / sisend

try:
    tekst = sisend.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Viga: faili '{failinimi}' ei leitud.")
else:
    sonad = re.findall(r"[^\W\d_]+", tekst.casefold(), flags=re.UNICODE)
    laused = [osa for osa in re.split(r"[.!?]+", tekst) if osa.strip()]
    sagedus = Counter(sonad).most_common(5)
    aruanne = [
        f"Sõnu: {len(sonad)}",
        f"Lauseid ligikaudu: {len(laused)}",
        f"Pikim sõna: {max(sonad, key=len) if sonad else 'puudub'}",
        "Viis sagedasemat sõna:",
    ]
    aruanne.extend(f"{sona}: {kogus}" for sona, kogus in sagedus)
    kokkuvote = "\n".join(aruanne)
    print(kokkuvote)
    (kaust / "tekstianaluus.txt").write_text(kokkuvote, encoding="utf-8")
