vanus = int(input("Vanus: "))
opilane = input("Kas oled õpilane (jah/ei): ")
if vanus < 7:
    hind = 0
elif vanus < 18:
    hind = 5
elif opilane == "jah":
    hind = 8
elif vanus >= 65:
    hind = 6
else:
    hind = 12
print("Pileti hind:", hind, "eurot")
