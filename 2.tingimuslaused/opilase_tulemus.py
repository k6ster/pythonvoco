nimi = input("Nimi: ")
punktid = int(input("Punktisumma: "))
puudumised = int(input("Puudumiste arv: "))
tood = input("Kas kõik tööd on esitatud (jah/ei): ")
if punktid >= 90:
    hinne = 5
elif punktid >= 75:
    hinne = 4
elif punktid >= 50:
    hinne = 3
elif punktid >= 20:
    hinne = 2
else:
    hinne = 1
print("Õpilane:", nimi)
print("Hinne:", hinne)
if puudumised > 10:
    print("Hoiatus: liiga palju puudumisi.")
else:
    print("Puudumiste arv on lubatud.")
if tood == "jah":
    print("Kõik tööd on esitatud.")
else:
    print("Kõik tööd ei ole esitatud.")
if hinne >= 3 and puudumised <= 10 and tood == "jah":
    print("Aine on läbitud.")
elif hinne < 3 or puudumised > 10 or tood != "jah":
    print("Aine ei ole läbitud.")
