def rea_summa(hind, kogus):
    return hind * kogus


def lisa_kaibemaks(summa, maar):
    return summa * (1 + maar / 100)


def kuva_kokkuvote(summa, maar):
    koos_maksuga = lisa_kaibemaks(summa, maar)
    print(f"Ilma käibemaksuta: {summa:.2f} €")
    print(f"Koos käibemaksuga: {koos_maksuga:.2f} €")


tooted = [(4.50, 2), (1.80, 3), (12.00, 1)]
kokku = sum(rea_summa(hind, kogus) for hind, kogus in tooted)
kuva_kokkuvote(kokku, 22)
