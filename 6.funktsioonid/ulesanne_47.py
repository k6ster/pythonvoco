def keskmine(punktid):
    if not punktid:
        return None
    return sum(punktid) / len(punktid)


def parim_tulemus(punktid):
    if not punktid:
        return None
    parim = punktid[0]
    for tulemus in punktid[1:]:
        if tulemus > parim:
            parim = tulemus
    return parim


def norgim_tulemus(punktid):
    if not punktid:
        return None
    norgim = punktid[0]
    for tulemus in punktid[1:]:
        if tulemus < norgim:
            norgim = tulemus
    return norgim


def edukate_arv(punktid, piir=50):
    return sum(tulemus >= piir for tulemus in punktid)


punktid = [78, 45, 92, 67, 34, 100, 56, 81]
print(f"Keskmine: {keskmine(punktid):.2f}")
print("Parim tulemus:", parim_tulemus(punktid))
print("Nõrgim tulemus:", norgim_tulemus(punktid))
print("Vähemalt 50 punkti:", edukate_arv(punktid))
