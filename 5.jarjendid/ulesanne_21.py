temperatuurid = [12, 18, 25, 9, 31, 22, 16, 28, 7]
soojad = []
jahedad = []
for temperatuur in temperatuurid:
    if temperatuur >= 20:
        soojad.append(temperatuur)
    else:
        jahedad.append(temperatuur)
print("Soojad:", soojad)
print("Jahedad:", jahedad)
