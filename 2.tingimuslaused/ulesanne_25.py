a = float(input("Esimene arv: "))
tehe = input("Tehe: ")
b = float(input("Teine arv: "))
if tehe == "+":
    print("Tulemus:", a + b)
elif tehe == "-":
    print("Tulemus:", a - b)
elif tehe == "*":
    print("Tulemus:", a * b)
elif tehe == "/":
    if b == 0:
        print("Nulliga ei saa jagada.")
    else:
        print("Tulemus:", a / b)
else:
    print("Tundmatu tehe.")
