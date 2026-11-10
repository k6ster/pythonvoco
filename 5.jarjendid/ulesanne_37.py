from pathlib import Path

read = []
tahemargid = 0
sonade_arv = 0
pikim_rida = ""
pikim_sona = ""
python_read = 0
with open(Path(__file__).with_name("tekst.txt"), encoding="utf-8") as fail:
    for rida in fail:
        read.append(rida.rstrip("\r\n"))
for rida in read:
    tahemargid = tahemargid + len(rida)
    sonad = rida.split()
    sonade_arv = sonade_arv + len(sonad)
    if len(rida) > len(pikim_rida):
        pikim_rida = rida
    leidub = False
    for sona in sonad:
        sona = sona.strip(".,!?;:()\"'–-")
        if len(sona) > len(pikim_sona):
            pikim_sona = sona
        if sona.lower() == "python":
            leidub = True
    if leidub:
        python_read = python_read + 1
print("Ridade arv:", len(read))
print("Tähemärkide arv:", tahemargid)
print("Sõnade arv:", sonade_arv)
print("Kõige pikem rida:", pikim_rida)
print("Kõige pikem sõna:", pikim_sona)
print("Sõnaga Python ridu:", python_read)
