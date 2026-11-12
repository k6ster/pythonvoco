from pathlib import Path
import re


sisend = Path(__file__).parent / "tekst.txt"
with open(sisend, encoding="utf-8") as fail:
    tekst = fail.read()
sonad = re.findall(r"[^\W\d_]+", tekst, flags=re.UNICODE)
if sonad:
    pikim = max(sonad, key=len)
    print(f"Kõige pikem sõna: {pikim}")
    print(f"Sõna pikkus: {len(pikim)}")
else:
    print("Failis pole sõnu.")
