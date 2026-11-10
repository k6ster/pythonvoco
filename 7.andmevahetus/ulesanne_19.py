from pathlib import Path

read = Path("kontaktid.txt")
read.write_text("Mari;mari@example.com;5551001\nAnna;anna@example.com;5551002\n", encoding="utf-8")
otsitav = input("Nimi: ").casefold()
for rida in read.read_text(encoding="utf-8").splitlines():
    nimi, email, telefon = rida.split(";")
    if nimi.casefold() == otsitav:
        print(email, telefon)
