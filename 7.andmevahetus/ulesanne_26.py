from urllib.request import urlopen


URL = "https://example.com/"
try:
    with urlopen(URL, timeout=10) as vastus:
        html = vastus.read().decode("utf-8")
    algus = html.find("<title>")
    lopp = html.find("</title>", algus + len("<title>")) if algus != -1 else -1
    pealkiri = html[algus + len("<title>"):lopp] if algus != -1 and lopp != -1 else "Pealkirja ei leitud"
    print("HTML-i algus:")
    print(html[:300])
    print("Sisaldab <title> märgendit:", "<title>" in html)
    print("Linke:", html.count("<a "))
    print("Lehe pealkiri:", pealkiri)
except (OSError, UnicodeError) as viga:
    print(f"Veebilehe lugemine ebaõnnestus: {viga}")
