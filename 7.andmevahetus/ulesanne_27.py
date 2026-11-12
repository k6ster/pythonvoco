from urllib.request import urlopen
from pathlib import Path


URL = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
valjund = Path(__file__).parent / "veebitekst.txt"
try:
    with urlopen(URL, timeout=10) as vastus:
        tekst = vastus.read().decode("utf-8")
    valjund.write_text(tekst, encoding="utf-8")
    read = valjund.read_text(encoding="utf-8").splitlines()
    print("Allalaadimine õnnestus.")
    if read:
        print("Esimene rida:", read[0])
        print("Viimane rida:", read[-1])
    else:
        print("Fail on tühi.")
except (OSError, UnicodeError) as viga:
    print(f"Allalaadimine ebaõnnestus: {viga}")
