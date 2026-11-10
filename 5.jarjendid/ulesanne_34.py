muugid = [125.50, 210.00, 98.75, 340.20, 185.40, 420.00, 275.90]
paevad = ["Esmaspäev", "Teisipäev", "Kolmapäev", "Neljapäev", "Reede", "Laupäev", "Pühapäev"]
yle_200 = 0
for i in range(len(muugid)):
    print(f"{paevad[i]}: {muugid[i]:.2f} €")
    if muugid[i] > 200:
        yle_200 = yle_200 + 1
print(f"Nädala kogumüük: {sum(muugid):.2f} €")
print(f"Keskmine päevamüük: {sum(muugid) / len(muugid):.2f} €")
print("Suurima müügiga päev:", paevad[muugid.index(max(muugid))])
print("Üle 200 euro müügiga päevi:", yle_200)
