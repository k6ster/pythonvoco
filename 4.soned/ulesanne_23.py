tekst = input("Sisesta tekst: ")
taishaalikud = 0
numbrid = 0
for taht in tekst:
    if taht.lower() in "aeiouõäöü":
        taishaalikud = taishaalikud + 1
    if taht.isdigit():
        numbrid = numbrid + 1
print("Tähemärke kokku:", len(tekst))
print("Tähemärke ilma tühikuteta:", len(tekst.replace(" ", "")))
print("Sõnu:", len(tekst.split()))
print("Täishäälikuid:", taishaalikud)
print("Numbreid:", numbrid)
