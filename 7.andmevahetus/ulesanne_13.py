from urllib.request import urlopen

try:
    with urlopen("https://example.com/", timeout=5) as vastus:
        tekst = vastus.read().decode("utf-8")
    print("Ridu:", len(tekst.splitlines()), "Sõnu:", len(tekst.split()))
except OSError as viga:
    print(f"Päring ebaõnnestus: {viga}")
