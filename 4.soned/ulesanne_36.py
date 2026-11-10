import tkinter as tk

ringide_arv = 20
laius = 800
aken = tk.Tk()
tahvel = tk.Canvas(aken, width=laius, height=400, bg="white")
tahvel.pack()
samm = laius / (ringide_arv + 1)
for i in range(ringide_arv):
    raadius = min(samm / 2, 150) * (i + 1) / ringide_arv
    x = samm * (i + 1)
    y = 200
    if i % 2 == 0:
        varv = "blue"
    else:
        varv = "red"
    tahvel.create_oval(x - raadius, y - raadius, x + raadius, y + raadius, fill=varv)
aken.mainloop()
