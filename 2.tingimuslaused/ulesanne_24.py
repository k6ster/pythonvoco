aasta = int(input("Sisesta aasta: "))
if aasta % 400 == 0:
    print("Liigaasta.")
elif aasta % 100 == 0:
    print("Ei ole liigaasta.")
elif aasta % 4 == 0:
    print("Liigaasta.")
else:
    print("Ei ole liigaasta.")
