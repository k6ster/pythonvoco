from pathlib import Path


kaust = Path(__file__).parent
allikas = kaust / "kontaktid.txt"
with open(allikas, encoding="utf-8") as fail:
    kontaktid = [tuple(osa.strip() for osa in rida.split(";")) for rida in fail if rida.strip()]

while True:
    otsitav = input("Otsi nime (lõpetamiseks STOP): ").strip()
    if otsitav.casefold() == "stop":
        break
    leitud = [kontakt for kontakt in kontaktid if kontakt[0].casefold() == otsitav.casefold()]
    if leitud:
        for nimi, email, telefon in leitud:
            print(f"{nimi}: {email}, {telefon}")
    else:
        print("Kontakti ei leitud.")
