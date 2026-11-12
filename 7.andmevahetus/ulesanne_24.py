from urllib.request import urlopen


URL = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
try:
    with urlopen(URL, timeout=10) as vastus:
        tekst = vastus.read().decode("utf-8")
    read = tekst.splitlines()
    sonad = tekst.split()
    tyhjad_read = sum(not rida.strip() for rida in read)
    print("Veebiteksti statistika")
    print("----------------------")
    print(f"Ridu: {len(read)}")
    print(f"Sõnu: {len(sonad)}")
    print(f"Tähemärke: {len(tekst)}")
    print(f"Tühje ridu: {tyhjad_read}")
except (OSError, UnicodeError) as viga:
    print(f"Veebifaili lugemine ebaõnnestus: {viga}")
