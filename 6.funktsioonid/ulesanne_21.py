def on_paaris(arv):
    return arv % 2 == 0


for arv in (8, 13, 0, -4):
    print(arv, on_paaris(arv))
