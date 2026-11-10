from urllib.request import urlopen
from pathlib import Path

try:
    with urlopen("https://example.com/", timeout=5) as vastus:
        Path("veebitekst.txt").write_bytes(vastus.read())
    read = Path("veebitekst.txt").read_text(encoding="utf-8").splitlines()
    print(read[0], read[-1])
except (OSError, UnicodeError) as viga:
    print(f"Salvestamine ebaõnnestus: {viga}")
