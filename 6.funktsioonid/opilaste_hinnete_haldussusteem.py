def loe_opilased(nimed, punktid, fail="hinded.txt"):
    try:
        with open(fail, encoding="utf-8") as sisend:
            for rida in sisend:
                nimi, tulemus = rida.strip().split(";", 1)
                lisa_opilane(nimed, punktid, nimi, tulemus)
    except FileNotFoundError:
        pass


def salvesta_opilased(nimed, punktid, fail="hinded.txt"):
    with open(fail, "w", encoding="utf-8") as valjund:
        for nimi, tulemus in zip(nimed, punktid):
            valjund.write(f"{nimi};{tulemus}\n")


def normaliseeri_nimi(nimi):
    return " ".join(nimi.split()).casefold()


def lisa_opilane(nimed, punktid, nimi, tulemus):
    nimi = " ".join(nimi.split())
    if not nimi:
        return False
    if any(normaliseeri_nimi(olemasolev) == normaliseeri_nimi(nimi) for olemasolev in nimed):
        return False
    try:
        tulemus = int(tulemus)
    except ValueError:
        return False
    if not 0 <= tulemus <= 100:
        return False
    nimed.append(nimi)
    punktid.append(tulemus)
    return True


def arvuta_hinne(punktid):
    if not 0 <= punktid <= 100:
        return None
    if punktid >= 90:
        return 5
    if punktid >= 75:
        return 4
    if punktid >= 50:
        return 3
    if punktid >= 20:
        return 2
    return 1


def leia_keskmine(punktid):
    if not punktid:
        return None
    return sum(punktid) / len(punktid)


def leia_parim(nimed, punktid):
    if not nimed or not punktid:
        return None
    indeks = punktid.index(max(punktid))
    return nimed[indeks], punktid[indeks]


def leia_norgim(nimed, punktid):
    if not nimed or not punktid:
        return None
    indeks = punktid.index(min(punktid))
    return nimed[indeks], punktid[indeks]


def kuva_opilased(nimed, punktid):
    if not nimed:
        print("Õpilasi pole veel lisatud.")
        return
    for nimi, tulemus in zip(nimed, punktid):
        print(f"{nimi}: {tulemus} p, hinne {arvuta_hinne(tulemus)}")


def kuva_statistika(nimed, punktid):
    if not punktid:
        print("Statistikat pole: õpilasi pole veel lisatud.")
        return
    parim = leia_parim(nimed, punktid)
    norgim = leia_norgim(nimed, punktid)
    print(f"Õpilasi kokku: {len(nimed)}")
    print(f"Keskmine punktisumma: {leia_keskmine(punktid):.2f}")
    print(f"Parim tulemus: {parim[0]} ({parim[1]} p)")
    print(f"Nõrgim tulemus: {norgim[0]} ({norgim[1]} p)")
    print("Hinnete jaotus:")
    for hinne in range(5, 0, -1):
        kogus = sum(arvuta_hinne(tulemus) == hinne for tulemus in punktid)
        nimetus = "õpilane" if kogus == 1 else "õpilast"
        print(f"Hinne {hinne}: {kogus} {nimetus}")


def otsi_opilane(nimed, punktid, nimi):
    otsitav = normaliseeri_nimi(nimi)
    for nimi_loendis, tulemus in zip(nimed, punktid):
        if normaliseeri_nimi(nimi_loendis) == otsitav:
            return nimi_loendis, tulemus
    return None


def kuva_menuu(pealkiri="ÕPILASTE HINNETE SÜSTEEM"):
    print(f"\n{pealkiri}")
    print("1. Kuva kõik õpilased")
    print("2. Lisa õpilane")
    print("3. Otsi õpilast nime järgi")
    print("4. Kuva klassi statistika")
    print("5. Salvesta")
    print("6. Lõpeta")


def main():
    nimed = []
    punktid = []
    loe_opilased(nimed, punktid)
    while True:
        kuva_menuu()
        valik = input("Vali tegevus: ").strip()
        if valik == "1":
            kuva_opilased(nimed, punktid)
        elif valik == "2":
            nimi = input("Õpilase nimi: ")
            tulemus = input("Punktisumma (0–100): ")
            if lisa_opilane(nimed, punktid, nimi, tulemus):
                print("Õpilane lisatud.")
            else:
                print("Andmeid ei lisatud. Kontrolli nime, punktisummat ja duplikaate.")
        elif valik == "3":
            tulemus = otsi_opilane(nimed, punktid, input("Otsitav nimi: "))
            if tulemus is None:
                print("Õpilast ei leitud.")
            else:
                print(f"{tulemus[0]}: {tulemus[1]} p, hinne {arvuta_hinne(tulemus[1])}")
        elif valik == "4":
            kuva_statistika(nimed, punktid)
        elif valik == "5":
            salvesta_opilased(nimed, punktid)
            print("Andmed salvestatud.")
        elif valik == "6":
            break
        else:
            print("Tundmatu valik. Proovi uuesti.")


if __name__ == "__main__":
    main()
