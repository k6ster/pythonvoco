import tkinter as tk

sona = input("Sisesta sõna: ")
pikkus = len(sona)
laius = 800
aken = tk.Tk()
tahvel = tk.Canvas(aken, width=laius, height=250, bg="white")
tahvel.pack()
if pikkus > 0:
    samm = (laius - 20) / pikkus
    suurus = min(60, samm * 0.8)
    kiri = max(1, min(16, int(samm / 2)))
    for i in range(pikkus):
        taht = sona[i]
        x = 10 + i * samm + (samm - suurus) / 2
        if taht.lower() in "aeiouõäöü":
            tahvel.create_oval(x, 70, x + suurus, 70 + suurus, fill="blue")
        elif taht.isalpha():
            tahvel.create_rectangle(x, 70, x + suurus, 70 + suurus, fill="green")
        else:
            tahvel.create_line(x, 70, x + suurus, 70 + suurus, fill="black")
        tahvel.create_text(x + suurus / 2, 160, text=taht, font=("Arial", kiri))
aken.mainloop()
