arvud = [7, 12, 19, 24, 31, 46, 53, 60, 72]
paaris = 0
paaritud = 0
paaris_summa = 0
paaritu_summa = 0
for arv in arvud:
    if arv % 2 == 0:
        paaris = paaris + 1
        paaris_summa = paaris_summa + arv
    else:
        paaritud = paaritud + 1
        paaritu_summa = paaritu_summa + arv
print("Paarisarve:", paaris)
print("Paarituid arve:", paaritud)
print("Paarisarvude summa:", paaris_summa)
print("Paaritute arvude summa:", paaritu_summa)
