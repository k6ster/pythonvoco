cpu = float(input("CPU kasutus (%): "))
malu = float(input("Mälu kasutus (%): "))
ketas = float(input("Ketta kasutus (%): "))
if cpu > 90 or malu > 90 or ketas > 90:
    print("Serveri olek: KRIITILINE")
elif cpu > 75 or malu > 75 or ketas > 75:
    print("Serveri olek: HOIATUS")
else:
    print("Serveri olek: OK")
