from pathlib import Path


fail = Path(__file__).parent / "ostunimekiri.txt"
tooted = []
while True:
    toode = input("Sisesta toode (lõpetamiseks STOP): ").strip()
    if toode.casefold() == "stop":
        break
    tooted.append(toode)

fail.write_text("".join(f"{toode}\n" for toode in tooted), encoding="utf-8")
print("Ostunimekiri salvestatud.")
