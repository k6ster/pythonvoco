from pathlib import Path


failitee = Path(__file__).parent / "ostunimekiri.txt"
print("Sisesta tooted, lõpetamiseks kirjuta STOP.")
with open(failitee, "a", encoding="utf-8") as fail:
    while True:
        toode = input("Sisesta toode: ").strip()
        if toode.casefold() == "stop":
            break
        if toode:
            fail.write(toode + "\n")
print("Ostunimekiri salvestatud.")
