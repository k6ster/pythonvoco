from urllib.request import urlopen
import re


URL = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
otsitav = input("Otsitav sõna: ").strip().casefold()
try:
    with urlopen(URL, timeout=10) as vastus:
        tekst = vastus.read().decode("utf-8").casefold()
    sonad = re.findall(r"[^\W\d_]+", tekst, flags=re.UNICODE)
    print(f"Sõna esineb {sonad.count(otsitav)} korda.")
except (OSError, UnicodeError) as viga:
    print(f"Veebiteksti lugemine ebaõnnestus: {viga}")
