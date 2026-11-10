from pathlib import Path

nimetused = []
hinnad = []
with open(Path(__file__).with_name("tooted.csv"), encoding="utf-8") as fail:
    for rida in fail:
        nimi, hind = rida.strip().split(";")
        nimetused.append(nimi)
        hinnad.append(float(hind))
for i in range(len(nimetused)):
    print(f"{nimetused[i]} – {hinnad[i]:.2f} €")
print("Tooteid kokku:", len(nimetused))
print(f"Kogumaksumus: {sum(hinnad):.2f} €")
kalleim = max(hinnad)
print(f"Kõige kallim toode: {nimetused[hinnad.index(kalleim)]} ({kalleim:.2f} €)")
