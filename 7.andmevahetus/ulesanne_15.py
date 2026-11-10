from urllib.request import urlopen

try:
    with urlopen("https://example.com/", timeout=5) as vastus:
        tekst = vastus.read().decode("utf-8")
    print(tekst[:300])
    print("<title>" in tekst, tekst.count("<a "))
except OSError as viga:
    print(f"Päring ebaõnnestus: {viga}")
