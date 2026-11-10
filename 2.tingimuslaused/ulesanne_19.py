a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
c = float(input("Kolmas arv: "))
if a >= b and a >= c:
    print("Suurim arv on", a)
elif b >= a and b >= c:
    print("Suurim arv on", b)
else:
    print("Suurim arv on", c)
