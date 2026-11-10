def vali_tegevus(arvud):
    return {"summa": sum(arvud), "keskmine": sum(arvud) / len(arvud)}

print(vali_tegevus([5, 7, 9]))
