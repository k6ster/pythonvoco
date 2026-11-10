from urllib.request import urlopen

try:
    with urlopen("https://example.com/", timeout=5) as vastus:
        print(vastus.read().decode("utf-8")[:200])
except OSError as viga:
    print(f"Veebipäring ebaõnnestus: {viga}")
