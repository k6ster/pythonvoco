def arvuta_kogus(hind, kogus):
    return round(hind * kogus, 2)

hind = float(input("Hind: "))
kogus = int(input("Kogus: "))
print(arvuta_kogus(hind, kogus))
