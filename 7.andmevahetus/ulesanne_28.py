from pathlib import Path


kaust = Path(__file__).parent
allikas = kaust / "temperatuurid.txt"
with open(allikas, encoding="utf-8") as fail:
    paevad = []
    for rida in fail:
        osad = rida.split()
        if osad:
            paevad.append((osad[0], int(osad[1])))

keskmine = sum(temp for _, temp in paevad) / len(paevad)
soojem = max(paevad, key=lambda kirje: kirje[1])
kulmem = min(paevad, key=lambda kirje: kirje[1])
ule_15 = sum(temp > 15 for _, temp in paevad)
aruanne = [
    f"Nädala keskmine temperatuur: {keskmine:.1f} °C",
    f"Kõige soojem päev: {soojem[0]} ({soojem[1]} °C)",
    f"Kõige külmem päev: {kulmem[0]} ({kulmem[1]} °C)",
    f"Päevi üle 15 kraadi: {ule_15}",
]
tekst = "\n".join(aruanne)
(kaust / "temperatuuri_aruanne.txt").write_text(tekst, encoding="utf-8")
print(tekst)
