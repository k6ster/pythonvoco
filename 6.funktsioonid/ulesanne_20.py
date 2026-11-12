def arvu_tyyp(arv):
    if arv > 0:
        return "Positiivne"
    if arv < 0:
        return "Negatiivne"
    return "Null"


for arv in (8, -3, 0):
    print(arv, arvu_tyyp(arv))
