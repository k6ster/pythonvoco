from pathlib import Path

kogus = 0
with open(Path(__file__).with_name("linnad.txt"), encoding="utf-8") as fail:
    for rida in fail:
        print(rida.strip())
        kogus = kogus + 1
print("Linnade arv:", kogus)
