from pathlib import Path

Path("read.txt").write_text("üks\nkaks\nkolm\n", encoding="utf-8")
with open("read.txt", encoding="utf-8") as fail:
    for rida in fail:
        print(rida.strip())
