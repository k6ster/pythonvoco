from pathlib import Path

temperatuurid = []
miinus = 0
soe = 0
with open(Path(__file__).with_name("temperatuurid.txt"), encoding="utf-8") as fail:
    for rida in fail:
        temperatuur = int(rida.strip())
        temperatuurid.append(temperatuur)
        if temperatuur < 0:
            miinus = miinus + 1
        if temperatuur >= 5:
            soe = soe + 1
print("Mõõtmisi:", len(temperatuurid))
print("Keskmine temperatuur:", sum(temperatuurid) / len(temperatuurid), "°C")
print("Kõrgeim temperatuur:", max(temperatuurid), "°C")
print("Madalaim temperatuur:", min(temperatuurid), "°C")
print("Miinuskraadidega päevi:", miinus)
print("Vähemalt 5-kraadiseid päevi:", soe)
