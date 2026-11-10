valik = ""
while valik != "0":
    print("TEKSTITÖÖTLUS")
    print("1 - Muuda tekst suurtähtedeks")
    print("2 - Muuda tekst väiketähtedeks")
    print("3 - Kuva teksti pikkus")
    print("4 - Pööra tekst tagurpidi")
    print("0 - Välju")
    valik = input("Valik: ")
    if valik in ["1", "2", "3", "4"]:
        tekst = input("Sisesta tekst: ")
        if valik == "1":
            print(tekst.upper())
        elif valik == "2":
            print(tekst.lower())
        elif valik == "3":
            print(len(tekst))
        else:
            print(tekst[::-1])
    elif valik != "0":
        print("Tundmatu valik.")
