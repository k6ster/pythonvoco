kasutajad = ["mari", "juhan", "kati", "peeter", "anna"]
nimi = input("Kasutajanimi: ").lower()
if nimi in kasutajad:
    print("Kasutaja on registreeritud.")
else:
    print("Kasutajat ei leitud.")
