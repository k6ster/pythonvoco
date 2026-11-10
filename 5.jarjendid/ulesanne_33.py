hinded = [4, 5, 3, 4, 2, 5, 5, 3, 4, 5, 2, 4]
positiivsed = 0
mitterahuldavad = 0
sagedus = 0
sagedasemad = []
for hinne in hinded:
    if hinne >= 3:
        positiivsed = positiivsed + 1
    else:
        mitterahuldavad = mitterahuldavad + 1
for hinne in range(1, 6):
    arv = hinded.count(hinne)
    print(f"Hinne {hinne}: {arv} korda", "*" * arv)
    if arv > sagedus:
        sagedus = arv
        sagedasemad = [hinne]
    elif arv == sagedus:
        sagedasemad.append(hinne)
print("Hinnete koguarv:", len(hinded))
print("Keskmine hinne:", sum(hinded) / len(hinded))
print("Kõige sagedasemad hinded:", sagedasemad)
print("Positiivseid hindeid:", positiivsed)
print("Mitterahuldavaid hindeid:", mitterahuldavad)
