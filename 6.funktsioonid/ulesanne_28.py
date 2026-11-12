def taishaalikuid(tekst):
    taishaalikud = "aeiouõäöü"
    return sum(taht.casefold() in taishaalikud for taht in tekst)


for sona in ("Tere", "Õunapuu", ""):
    print(sona, taishaalikuid(sona))
