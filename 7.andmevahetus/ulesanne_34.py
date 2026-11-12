from pathlib import Path


KAUST = Path(__file__).parent
ANDMEFAIL = KAUST / "hinded.txt"


def loe_opilased():
    opilased = []
    try:
        with open(ANDMEFAIL, encoding="utf-8") as fail:
            for rida in fail:
                osad = rida.rsplit(maxsplit=1)
                if len(osad) == 2:
                    nimi, hinne = osad
                    try:
                        hinne = int(hinne)
                    except ValueError:
                        continue
                    if 1 <= hinne <= 5:
                        opilased.append((nimi, hinne))
    except FileNotFoundError:
        pass
    return opilased


def salvesta_opilased(opilased):
    ANDMEFAIL.write_text("".join(f"{nimi} {hinne}\n" for nimi, hinne in opilased), encoding="utf-8")


def kuva_opilased(opilased):
    if not opilased:
        print("Õpilasi pole.")
        return
    for nimi, hinne in opilased:
        print(f"{nimi}: {hinne}")


def lisa_opilane(opilased):
    nimi = input("Õpilase nimi: ").strip()
    try:
        hinne = int(input("Hinne (1–5): "))
    except ValueError:
        print("Hinne peab olema täisarv.")
        return
    if not nimi or hinne not in range(1, 6):
        print("Sisesta nimi ja hinne vahemikus 1–5.")
        return
    opilased.append((nimi, hinne))
    salvesta_opilased(opilased)
    print("Õpilane lisatud.")


def otsi_opilast(opilased):
    nimi = input("Otsitav nimi: ").strip().casefold()
    leitud = [kirje for kirje in opilased if kirje[0].casefold() == nimi]
    if leitud:
        kuva_opilased(leitud)
    else:
        print("Õpilast ei leitud.")


def kuva_statistika(opilased):
    if not opilased:
        print("Statistikat pole: õpilasi pole.")
        return
    hinded = [hinne for _, hinne in opilased]
    print(f"Keskmine hinne: {sum(hinded) / len(hinded):.2f}")
    for hinne in range(1, 6):
        print(f"Hinne {hinne}: {hinded.count(hinne)}")


def salvesta_aruanne(opilased):
    read = ["ÕPILASTE HINNETE ARUANNE"]
    read.extend(f"{nimi}: {hinne}" for nimi, hinne in opilased)
    if opilased:
        hinded = [hinne for _, hinne in opilased]
        read.append(f"Keskmine hinne: {sum(hinded) / len(hinded):.2f}")
        read.extend(f"Hinne {hinne}: {hinded.count(hinne)}" for hinne in range(1, 6))
    (KAUST / "hinnete_aruanne.txt").write_text("\n".join(read), encoding="utf-8")
    print("Aruanne salvestati faili hinnete_aruanne.txt.")


def main():
    opilased = loe_opilased()
    while True:
        print("\n1. Kuva kõik õpilased")
        print("2. Lisa uus õpilane ja hinne")
        print("3. Otsi õpilast")
        print("4. Kuva hinnete statistika")
        print("5. Salvesta aruanne faili")
        print("6. Lõpeta")
        valik = input("Valik: ").strip()
        if valik == "1":
            kuva_opilased(opilased)
        elif valik == "2":
            lisa_opilane(opilased)
        elif valik == "3":
            otsi_opilast(opilased)
        elif valik == "4":
            kuva_statistika(opilased)
        elif valik == "5":
            salvesta_aruanne(opilased)
        elif valik == "6":
            break
        else:
            print("Tundmatu valik. Proovi uuesti.")


if __name__ == "__main__":
    main()
