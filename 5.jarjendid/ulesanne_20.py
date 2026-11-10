arvud = [-12, 5, 0, 18, -7, 23, -3, 9]
positiivsed = 0
negatiivsed = []
nullid = 0
summa = 0
for arv in arvud:
    if arv > 0:
        positiivsed = positiivsed + 1
        summa = summa + arv
    elif arv < 0:
        negatiivsed.append(arv)
    else:
        nullid = nullid + 1
print("Positiivseid:", positiivsed)
print("Negatiivseid:", len(negatiivsed))
print("Nulle:", nullid)
print("Positiivsete summa:", summa)
print("Negatiivsed arvud:", negatiivsed)
