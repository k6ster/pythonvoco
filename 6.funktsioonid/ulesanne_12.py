def kuva_hind(toode, hind, valuuta="€"):
    print(f"{toode}: {hind:.2f} {valuuta}")


kuva_hind("Klaviatuur", 35)
kuva_hind("Hiir", 20, "$")
