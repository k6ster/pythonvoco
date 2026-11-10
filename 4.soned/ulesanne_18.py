lause = input("Sisesta lause: ").lower()
kokku = 0
for taht in "aeiouõäöü":
    arv = lause.count(taht)
    print(taht + ":", arv)
    kokku = kokku + arv
print("Täishäälikuid kokku:", kokku)
