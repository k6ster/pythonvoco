def liida(a, b):
    return a + b


def lahuta(a, b):
    return a - b


def korruta(a, b):
    return a * b


def jaga(a, b):
    if b == 0:
        return None
    return a / b


def kuva_menuu():
    print("1 Liida  2 Lahuta  3 Korruta  4 Jaga  0 Lõpeta")


while True:
    kuva_menuu()
    valik = input("Tehe: ")
    if valik == "0":
        break
    tehted = {"1": liida, "2": lahuta, "3": korruta, "4": jaga}
    if valik not in tehted:
        print("Tundmatu tehe.")
        continue
    try:
        a = float(input("Esimene arv: "))
        b = float(input("Teine arv: "))
    except ValueError:
        print("Sisesta arvud.")
        continue
    tulemus = tehted[valik](a, b)
    if tulemus is None:
        print("Nulliga ei saa jagada.")
    else:
        print(f"Tulemus: {tulemus:g}")
