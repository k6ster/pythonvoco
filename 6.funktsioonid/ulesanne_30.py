def positiivsed(arvud):
    tulemus = []
    for arv in arvud:
        if arv > 0:
            tulemus.append(arv)
    return tulemus


arvud = [-4, 5, 0, 12, -2, 7]
print(positiivsed(arvud))
print(arvud)
