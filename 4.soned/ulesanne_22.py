aadress = input("Sisesta e-post: ")
sobib = False
if aadress.count("@") == 1 and " " not in aadress:
    nimi, domeen = aadress.split("@")
    if len(nimi) > 0 and "." in domeen and not domeen.startswith(".") and not domeen.endswith("."):
        sobib = True
if sobib:
    print("Aadressi kuju on sobiv.")
else:
    print("Aadressi kuju ei ole sobiv.")
