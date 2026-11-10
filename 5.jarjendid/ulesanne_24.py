laused = [
    "Täna õpime Pythonit",
    "Järjendid on väga kasulikud",
    "Programmeerimine nõuab harjutamist",
    "Tartu on ilus linn"
]
kokku = 0
pikim = laused[0]
for lause in laused:
    arv = lause.lower().count("a")
    print(lause, "– tähemärke:", len(lause), "a-tähti:", arv)
    kokku = kokku + arv
    if len(lause) > len(pikim):
        pikim = lause
print("a-tähti kokku:", kokku)
print("Kõige pikem lause:", pikim)
