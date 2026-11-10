def raha_eurodes(maasikakastide_arv, maasikakilo_hind):
    return round(maasikakastide_arv * 5 * maasikakilo_hind / 100, 1)


failinimi = input("Sisestage failinimi: ")
kilohind = int(input("Sisestage kilo hind sentides: "))

kokku = 0

with open(failinimi, "r", encoding="utf-8") as fail:
    for paev, rida in enumerate(fail, start=1):
        kastide_arv = int(rida.strip())
        raha = raha_eurodes(kastide_arv, kilohind)
        kokku += raha
        print(f"{paev}. päeval sai {raha:.1f} eurot.")

print(f"Kokku sai: {kokku:.1f} eurot.")