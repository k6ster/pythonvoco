esimene = [2, 4, 6, 8, 10, 12]
teine = [3, 6, 9, 12, 15]
yhised = []
ainult_esimeses = []
for arv in esimene:
    if arv in teine:
        yhised.append(arv)
    else:
        ainult_esimeses.append(arv)
print("Ühised arvud:", yhised)
print("Ainult esimeses:", ainult_esimeses)
