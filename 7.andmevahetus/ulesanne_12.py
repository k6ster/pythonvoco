from urllib.request import urlopen

try:
    with urlopen("https://example.com/", timeout=5) as vastus:
        read = vastus.read().decode("utf-8").splitlines()
    for number, rida in enumerate(read[:10], 1):
        print(number, rida)
except OSError as viga:
    print(f"Päring ebaõnnestus: {viga}")
