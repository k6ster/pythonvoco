from urllib.request import urlopen


URL = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
try:
    with urlopen(URL, timeout=10) as vastus:
        read = vastus.read().decode("utf-8").splitlines()
    for number, rida in enumerate(read[:10], start=1):
        print(f"{number}: {rida}")
except (OSError, UnicodeError) as viga:
    print(f"Veebifaili lugemine ebaõnnestus: {viga}")
