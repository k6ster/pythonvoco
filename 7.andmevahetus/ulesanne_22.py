from urllib.request import urlopen


URL = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
try:
    with urlopen(URL, timeout=10) as vastus:
        tekst = vastus.read().decode("utf-8")
    print(tekst)
except (OSError, UnicodeError) as viga:
    print(f"Veebifaili lugemine ebaõnnestus: {viga}")
