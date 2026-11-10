def loe_hinded(fail="hinded.txt"):
    andmed = {}
    try:
        with open(fail, encoding="utf-8") as f:
            for rida in f:
                nimi, hinne = rida.strip().split(";", 1)
                andmed[nimi] = int(hinne)
    except FileNotFoundError:
        pass
    return andmed

def kuva(andmed):
    for nimi, hinne in andmed.items():
        print(f"{nimi}: {hinne}")

def lisa(andmed):
    nimi = input("Nimi: ").strip()
    if nimi in andmed:
        print("Sama nimega õpilane on juba olemas.")
        return
    try:
        hinne = int(input("Hinne 1-5: "))
        if hinne not in range(1, 6):
            raise ValueError
    except ValueError:
        print("Vigane hinne.")
        return
    andmed[nimi] = hinne

def salvesta(andmed, fail="hinded.txt"):
    with open(fail, "w", encoding="utf-8") as f:
        for nimi, hinne in andmed.items():
            f.write(f"{nimi};{hinne}\n")

andmed = loe_hinded()
while True:
    print("1 Kuva  2 Lisa  3 Otsi  4 Statistika  5 Salvesta  6 Lõpeta")
    valik = input("Valik: ")
    if valik == "1":
        kuva(andmed)
    elif valik == "2":
        lisa(andmed)
    elif valik == "3":
        print(andmed.get(input("Nimi: ").strip(), "Ei leitud"))
    elif valik == "4":
        hinded = list(andmed.values())
        print(sum(hinded) / len(hinded) if hinded else "Andmeid pole")
    elif valik == "5":
        salvesta(andmed)
    elif valik == "6":
        break
    else:
        print("Tundmatu valik.")
