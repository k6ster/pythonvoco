salasona = "python"
katsed = 0
vastus = ""
while katsed < 5 and vastus != salasona:
    vastus = input("Arva salasõna: ")
    katsed = katsed + 1
    if vastus == salasona:
        print("Õige vastus!")
    else:
        print("Vale vastus. Katseid jäänud:", 5 - katsed)
