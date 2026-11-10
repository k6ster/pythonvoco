def loenda_paaris(arvud):
    return sum(arv % 2 == 0 for arv in arvud)

print(loenda_paaris([1, 2, 4, 7, 8]))
