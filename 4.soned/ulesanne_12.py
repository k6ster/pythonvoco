lause = input("Lause: ")
otsitav = input("Otsitav: ")
indeks = lause.find(otsitav)
if indeks == -1:
    print("Tekstiosa ei leitud.")
else:
    print("Leitud indeksilt", indeks)
