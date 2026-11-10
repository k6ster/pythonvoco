sonad = ["arvuti", "programmeerimine", "hiir", "klaviatuur", "monitor"]
pikim = sonad[0]
lyhim = sonad[0]
for sona in sonad:
    if len(sona) > len(pikim):
        pikim = sona
    if len(sona) < len(lyhim):
        lyhim = sona
print("Kõige pikem:", pikim, len(pikim))
print("Kõige lühem:", lyhim, len(lyhim))
