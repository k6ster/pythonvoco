from urllib.request import urlopen

otsitav = input("Otsitav sõna: ").casefold()
try:
    with urlopen("https://example.com/", timeout=5) as vastus:
        tekst = vastus.read().decode("utf-8").casefold()
    print(tekst.split().count(otsitav))
except OSError as viga:
    print(f"Päring ebaõnnestus: {viga}")
