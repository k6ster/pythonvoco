tooted = []
hinnad = []
nimi = input("Sisesta toote nimi (lõpetamiseks ENTER): ")
while nimi != "":
    hind = float(input("Hind: "))
    tooted.append(nimi)
    hinnad.append(hind)
    nimi = input("Sisesta toote nimi (lõpetamiseks ENTER): ")
for i in range(len(tooted)):
    print(f"{tooted[i]} – {hinnad[i]:.2f} €")
print("Toodete arv:", len(tooted))
print(f"Kogumaksumus: {sum(hinnad):.2f} €")
if len(tooted) > 0:
    print("Kõige kallim toode:", tooted[hinnad.index(max(hinnad))])
else:
    print("Ostukorv on tühi.")
allahindlus = float(input("Allahindlus (%): "))
print(f"Uus kogumaksumus: {sum(hinnad) * (1 - allahindlus / 100):.2f} €")
